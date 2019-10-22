
# Classes: WnaderingCritter

# The code that was used in Kitchen Scraps to test mouse.
# mouse_folder = 'N:\\OneDrive\\8_GameDev\\AtelierPygmalia\\kitchen_scraps\\images\\mouse\\'
# mouse = WanderingCritter('mouse', mouse_folder, ks.bg, (150,100))
#
# def refresh_screen(self, opt_obj=''):
#     """Refresh all elements onto the screen during active gameplay."""
#     self.bg.refresh_screen()
#     if opt_obj:
#         opt_obj.refresh_img()
#
# mouse.wander_behavior()
# ks.refresh_screen()



class WanderingCritter():
    """An image of a critter randomly walks around the map in cardinal directions, but does not pass obstacles."""
    # Would like to add: Critter runs away at higher speed when too close to certain entities.
    # Critter navigates to specific spots.
    # Critter is attracted to certain items and 'consumes' them when touching.
    # When a flag is triggered, Critter runs to designated spot.

    def __init__(self, name, imgs_folder, bg, xy=(0, 0)):
        self.name = name
        self.imgs_folder = imgs_folder
        self.bg = bg
        self.directions = ['front', 'left', 'right', 'up', 'down']
        self.direction = 'front'
        self.random_countdown = 0
        self.speed = 0.1
        self.sprites = self.make_sprite_srfs()
        self.sprite_state = self.sprites['front']
        self.rect = self.sprite_state.get_rect()
        self.rect.move_ip(xy)

    def make_sprite_srfs(self):
        """Create a set of image srfs from a folder of images with front, back, and cardinal poses.
        Add the srfs to a sprites dict."""
        sprites = {}
        filenames = os.listdir(self.imgs_folder)
        for filename in filenames:
            print(filename)
            filename = filename.lower()
            for direction in self.directions:
                if direction in filename:
                    sprites[direction] = pygame.image.load(self.imgs_folder + filename)
        print(sprites)
        return sprites

    def wander_behavior(self):
        """Make the critter wander and pause in random directions.If it hits a wall, pause and change direction."""
        if self.random_countdown > 0:
            self.random_countdown -= 1
            self.change_direction_sense_collision()
            self.go_to_direction(self.direction)
        elif self.random_countdown <= 0:
            self.random_countdown = random.randint(100, 1000)
            print(self.random_countdown)
            self.direction = random.choice(self.directions)
            #self.change_direction_sense_collision()
            self.go_to_direction(self.direction)

    def change_direction_sense_collision(self):
        available_directions = self.directions.copy()
        no_removals = len(available_directions)
        # if critter hits left wall
        if self.rect[0] <= 8:
            available_directions.remove('left')
        # if critter hits right wall
        if self.rect[0] >= (self.bg.rect[2] - 72):
            available_directions.remove('right')
        # if critter hits top wall
        if self.rect[1] <= 8:
            available_directions.remove('up')
        # if critter hits bottom wall
        if self.rect[1] >= (self.bg.rect[3] - 72):
            available_directions.remove('down')
        if len(available_directions) < no_removals:
            self.direction = random.choice(available_directions)

    def go_to_direction(self, direction):
        """Move the sprite toward a cardinal direction and update the sprite to face in the correct position."""
        self.rect = [float(self.rect[0]), float(self.rect[1])]
        x = self.rect[0]
        y = self.rect[1]
        if direction == 'left':
            x -= self.speed
        elif direction == 'right':
            x += self.speed
        elif direction == 'up':
            y -= self.speed
        elif direction == 'down':
            y += self.speed
        self.sprite_state = self.sprites[self.direction]
        self.rect = [x, y]

    def move_keys(self):
        """Change the sprite's direction image based on input. Either WASD or arrow keys."""
        # This was split off from go_to_direction, and is not functional as-is.
        direction_keys = {
            'front': '',
            'left': (pygame.K_a, pygame.K_LEFT),
            'right': (pygame.K_d, pygame.K_RIGHT),
            'up': (pygame.K_w, pygame.K_UP),
            'down': (pygame.K_s, pygame.K_DOWN),
            }

    def refresh_img(self):
        """Refreshes the image srf and rect onto the background screen."""
        self.bg.screen.blit(self.sprite_state, self.rect)
