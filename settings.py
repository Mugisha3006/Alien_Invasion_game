class Settings():
    """A class to store all settings for the Alien Invasion"""

    def __init__(self):
        """initialize the game settings"""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (75,83,32)

        # ship settings
        self.ship_speed_factor = 1.5