import pygame 
from pygame.sprite import Sprite
import os

class Alien(Sprite):
    """A class to represent a single alien in the fleet"""
    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load the alien image and set its rect attribute
        image_path = os.path.join(os.path.dirname(__file__), "images", "alien1.bmp")
        print(f"Loading alien image from: {image_path}")  # Debugging line
        try:
            self.image = pygame.image.load(image_path)
        except pygame.error:
            raise FileNotFoundError(f"Alien image not found at {image_path}. Please check the file path")
        
        # resize the alien image to 100*50 
        self.image = pygame.transform.scale(self.image, (100,100))
        
        self.rect = self.image.get_rect()

        # start each new alien near the top left of the screen
        self.rect.x = 0 
        self.rect.y = 0

        # store the alien's exact position
        self.x = float(self.rect.x)

    def check_edges(self):
        """return True if alien is at the edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """move the alien right or left"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        """draw the alien at its current location"""
        self.screen.blit(self.image, self.rect)