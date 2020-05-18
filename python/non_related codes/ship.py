import pygame

class Ship():
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
# Load image for the ship and get outside rect
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

# Place new ship at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

# Store a decimal value for the ship's center
        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)

# Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def update(self):
        """Update the ship's position based on the moving flag"""
        # Update the ship's center value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        elif self.moving_up and self.rect.top < self.screen_rect.top:
            self.bottom += self.ai_settings.ship_speed_factor
        elif self.moving_down and self.rect.bottom > 0:
            self.bottom -= self.ai_settings.ship_speed_factor
        # Update rect object from self.center
        self.rect.centerx = self.center
        self.rect.bottom = self.bottom

    def blitme(self):
        """Draw ship at given location"""
        self.screen.blit(self.image, self.rect)