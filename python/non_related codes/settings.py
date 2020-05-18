class Settings():
#A Class to store all settings for the game
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (40, 80, 100)

        # Ship speed
        self.ship_speed_factor = 1.5