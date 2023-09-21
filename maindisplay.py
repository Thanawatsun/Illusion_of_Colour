import pygame
import pygame_widgets
import cv2
import numpy as np
from pygame_widgets.slider import Slider
from pygame_widgets.button import Button

#HSL
top_hue = 0

def output(top_hue):
    img = cv2.imread('pictures/room-1-with-obj.png')
    lower = np.array([0, 50, 0])
    upper = np.array([top_hue, 255, 255])
    mask = cv2.inRange(img, lower, upper)
    res = cv2.bitwise_and(img, img, mask= mask)
    cv2.imshow('img', res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    pygame.init()
    
    #Window Name
    pygame.display.set_caption("test")

    #Window Size
    screen = pygame.display.set_mode((1280, 720))

    #Slider
    slider = Slider(screen, 100, 100, 800, 40, min=0, max=179, step=1)

    #Make button | (window, location-X, location-Y, Width, Height)
    button = Button(screen, 1060, 650, 200, 50, text='Submit', inactiveColour=(200, 50, 0), onClick=lambda: output(top_hue))
    
    #Load image
    img = pygame.image.load("pictures/room-1-with-obj.png").convert_alpha()
    
    running = True

    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
        
        #Screen color | RGB
        screen.fill((128, 128, 128))
        
        #Place image in to screen
        screen.blit(img, (20, 20))

        top_hue = slider.getValue()

        print(top_hue)
        
        pygame_widgets.update(events)
        pygame.display.update()

main()
