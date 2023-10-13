import pygame, sys
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.button import Button
from output import *
import checkresult

pygame.init()

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


def main():
    # HSL
    top_hue = 0
    bottom_hue = 0
    top_Saturation = 0
    bottom_Saturation = 0
    top_Lightness = 0
    bottom_Lightness = 0

    # Slider
    t_h_slider = Slider(screen, 725, 50, 500, 30, min=0, max=255, step=1, initial=255)
    b_h_slider = Slider(screen, 725, 150, 500, 30, min=0, max=255, step=1, initial=0)
    t_s_slider = Slider(screen, 725, 250, 500, 30, min=0, max=255, step=1, initial=255)
    b_s_slider = Slider(screen, 725, 350, 500, 30, min=0, max=255, step=1, initial=0)
    t_l_slider = Slider(screen, 725, 450, 500, 30, min=0, max=255, step=1, initial=255)
    b_l_slider = Slider(screen, 725, 550, 500, 30, min=0, max=255, step=1, initial=0)
    button_positions = (1060, 650)
    button_size = (200, 50)

    # Make button | (window, location-X, location-Y, Width, Height)
    button = Button(
        screen,
        button_positions[0],
        button_positions[1],
        button_size[0],
        button_size[1],
        text="Submit",
        inactiveColour=(200, 50, 0),
    )
    running = True

    while running:
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
        
        # Screen color | RGB
        screen.fill((128, 128, 128))

        # Get value from slider
        top_hue = t_h_slider.getValue()
        bottom_hue = b_h_slider.getValue()
        top_saturation = t_s_slider.getValue()
        bottom_saturation = b_s_slider.getValue()
        top_lightness = t_l_slider.getValue()
        bottom_lightness = b_l_slider.getValue()

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


main()
