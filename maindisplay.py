import pygame
import pygame_widgets
import cv2
import numpy as np
from pygame_widgets.slider import Slider
from pygame_widgets.button import Button
from output import *

pygame.init()
    
#Window Name
pygame.display.set_caption("test")

#Window Size
screen = pygame.display.set_mode((1280, 720))\

#Load image
img = pygame.image.load("pictures/room-1-with-obj.png").convert_alpha()

#HSL
top_hue = 0
bottom_hue = 0
top_Saturation = 0
bottom_Saturation = 0
top_Lightness = 0
bottom_Lightness = 0

def main():
    #Slider
    t_h_slider = Slider(screen, 725, 50, 500, 30, min=0, max=179, step=1)
    b_h_slider = Slider(screen, 725, 150, 500, 30, min=0, max=179, step=1)
    t_s_slider = Slider(screen, 725, 250, 500, 30, min=0, max=255, step=1)
    b_s_slider = Slider(screen, 725, 350, 500, 30, min=0, max=255, step=1)
    t_l_slider = Slider(screen, 725, 450, 500, 30, min=0, max=255, step=1)
    b_l_slider = Slider(screen, 725, 550, 500, 30, min=0, max=255, step=1)

    #Make button | (window, location-X, location-Y, Width, Height)
    button = Button(screen, 1060, 650, 200, 50, text='Submit', inactiveColour=(200, 50, 0), onClick=lambda: output(bottom_hue, bottom_Saturation, bottom_Lightness, top_hue, top_Saturation, top_Lightness))
    running = True
    
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # get MOUSEBUTTONDOWN positions
                if 650 <= pygame.mouse.get_pos()[1] <= 700 and 1060 <= pygame.mouse.get_pos()[0] <= 1260:
                    # set img when Submit
                    global img
                    img = setimg()
        
        #Screen color | RGB
        screen.fill((128, 128, 128))
        
        #Place image in to screen
        screen.blit(img, (20, 20))

        top_hue = t_h_slider.getValue()
        bottom_hue = b_h_slider.getValue()
        top_Saturation = t_s_slider.getValue()
        bottom_Saturation = b_s_slider.getValue()
        top_Lightness = t_l_slider.getValue()
        bottom_Lightness = b_l_slider.getValue()
        
        pygame_widgets.update(events)
        pygame.display.update()

main()
