


"""This module is meant to hold classes related to menu screens. Examples include: Play menu, pause/options, levels."""

import pygame
from ks_environment import Grid, Background
from ks_buttons import Button



class Menu():
    """A menu page with buttons to click that trigger various effects."""
    # TODO This isn't functional yet.
    def __init__(self, name, music):
        """Initialize Menu attributes."""
        self.bg = Background('images/' + name + '.png')
        self.music = ('sound/' + music)
        self.buttons = {}
        xy_newgame = (self.bg.center)
        Button('new game', self.bg, xy_newgame)

    def refresh(self):
        """Refresh the screen."""
        self.screen.fill(0, 0, 0)
        self.screen.blit(self.img, self.rect)

    def display_buttons(self):
        """"Arrange the buttons for the screen."""
        self.buttons = {
            'new game': insertbuttonobjhere,
            'credits': ss,
            'save file': xx,
            }



class LevelMenu():
    """Contain a a book-chapter of levels."""
    def __init__(self, bg, title, recipes):
        """Initiate attributes for LevelMenu."""
        self.bg = bg
        self.title = title
        self.recipes = recipes
        self.grid = Grid(title, rows=5, columns=2)
        self.grid.make_grid((self.grid.origin[0]+200, self.grid.origin[1]))
        z = 0
        for coord in self.grid.grid.items():
            try:
                self.grid.grid[coord] = Button(self.recipes[z], self.bg)
                z += 1
            except IndexError:
                break
        self.locked_recipes = [self.recipes[0]]
        self.unlocked_recipes = []

    def refresh_button(self):
        self.bg.refresh_screen()
        mouse_xy = pygame.mouse.get_pos()
        for button in self.grid.grid.values():
            if button and button.unlocked:
                if button.rect.collidepoint(mouse_xy):
                    button.img_srf = button.hvr_srf
                else:
                    button.img_srf = button.def_srf
            elif button and button.locked:
                if button.rect.collidepoint(mouse_xy):
                    button.img_srf = button.gry_hvr_srf
                else:
                    button.img_srf = button.gry_srf
            self.bg.screen.blit(button.img_srf, button.rect)

    def get_level(self):
        """Check the mouse clicks to see if they click a level.
        If so, return the level name (a string) to be used to redirect to the level."""
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_xy = pygame.mouse.get_pos()
                for button in self.grid.grid.values():
                    if button:
                        collide = button.check_collide(mouse_xy)
                        if collide:
                            return button.name

    def goto_level(self, settings, level):
        """Change the screen and active states to the level play setup."""
        settings.state = 'play'
        settings.set_level(level)

    def flip_page(self):
        """Flip the 'page' by clicking on the corners or arrows on opposite ends of the screen.
        music/sfx/mute button
        x button - close book, go to library. book spines or book covers. ghost spots for hidden books.
        have them be library spines, BUT show off the faces upon hover.
        show hidden books as just grayed outlines, but maybe a line like 'hm, smells like the sea...' to give a hint?"""