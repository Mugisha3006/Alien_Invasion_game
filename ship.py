import pygame

class Ship:
    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and get its rect
        self.image = pygame.image.load("C:\\Users\\Administrator\\Desktop\\projects\\Alien_Invasion\\Alien_Invasion_game\\images\\ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom

        # store a decimal value for the ship's center
        self.center = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)

        # movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False

    def update(self):
        """update the ship's position based on the movement flags"""
        # update the ship's center value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.center_y -= self.ai_settings.ship_speed_factor

        
        
        # update rect object from self.center
        self.rect.centerx = self.center
        self.rect.centery = self.center_y


    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)