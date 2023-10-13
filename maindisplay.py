import pygame, sys
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.button import Button
#from output import *
from menu import*
#pygame.init()
from gameplay import*

"""
# Window Name
pygame.display.set_caption("test")

# Window Size
screen = pygame.display.set_mode((1280, 720))


def test():
    screen.fill((0, 0, 0))
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    main()
        pygame_widgets.update(events)
        pygame.display.update()
"""

def main():

    running = True

    while running:
        menu()
        gameplay()
        """
        mouse_location = pygame.mouse.get_pos()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_SPACE:
                    checkresult.run()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_press = pygame.mouse.get_pressed()
                if mouse_press[0] and mouse_location[0] >= 1060 and mouse_location[0] <= 1260 and mouse_location[1] >= 650 and mouse_location[1] <= 700:
                    running = False
                    test()
        
        
        
        # Change output image
        
        output(
            bottom_hue,
            bottom_saturation,
            bottom_lightness,
            top_hue,
            top_saturation,
            top_lightness,
        )
        img = setimg()

        # Place image in to screen
        screen.blit(img, (20, 20))

        pygame_widgets.update(events)
        pygame.display.update()
        print("re")"""

main()
