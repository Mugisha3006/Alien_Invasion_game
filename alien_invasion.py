import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
    # initialize pygame, settings, and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # make the play button
    play_button = Button(ai_settings, screen, "Play")

    # create an instance to store game statistics and create a scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

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
        gf.check_events(ai_settings, screen, ship, bullets, play_button, stats, sb, aliens)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()