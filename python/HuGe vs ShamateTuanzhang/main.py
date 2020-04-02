# Main program of Alien Invasion
import sys
import pygame

def run_game():
    pygame.init()
    settings = Settings()
    # Configuring screen res and title
    screen =  pygame.display.set_mode((1440, 900))
    pygame.display.set_caption("虎哥大战杀马特团长")

    while True:

        #Monitoring Keyboard & Mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit
        
        screen.fill(settings.bg_color)
        pygame.display.flip()

run_game()