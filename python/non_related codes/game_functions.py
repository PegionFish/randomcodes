import sys
import pygame

def check_keydown_events(event, ship):
    """Respond to keypresses"""
    if event.key == pygame.K_RIGHT:
        #Move the ship to the right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        #Move the ship to the left
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        #Move the ship to the top
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        #Move the ship to the bottom
        ship.moving_down = True
def check_keyup_events(event, ship):
    """Respond to key releases"""
    if event.key == pygame.K_RIGHT:
        #Stop moving the ship to the right
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        #Stop moving the ship to the left
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        #Stop moving the ship to the top
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        #Stop moving the ship to the bottom
        ship.moving_down = False

def check_events(ship):
    """React to keyboard&Mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
def update_screen(ai_settings, screen, ship):
    """Update images on the screnn & flip to the new screen"""
    #Redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    #Make the most recently drawn screnn visible
    pygame.display.flip()