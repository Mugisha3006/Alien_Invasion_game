import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
    # initialize pygame, settings, and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # make a ship
    ship = Ship(ai_settings, screen)

    # make a group to store aliens
    aliens = Group()

    # create a single alien and add it to the group
    # alien = Alien(ai_settings, screen)
    # aliens.add(alien)

    # create a fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # make a group to store bullets in
    bullets = Group()

    # start the main loop for the game 
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()