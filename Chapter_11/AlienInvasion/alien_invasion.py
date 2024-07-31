import sys
import pygame
from settings import Settings
from ship import Ship
import games_function as GF

def run_game():
    #intiliaze the screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen)

    #setting background color
    bg_color = (ai_settings.bg_color)

    while True:
        GF.check_events()

        #redraw th screen during each pass through
        GF.update_screen(ai_settings, screen, ship)

        # make sure the most recently drawn screen visible
        pygame.display.flip()

run_game()