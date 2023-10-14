import pygame, sys
import pygame_widgets
from pygame_widgets.button import Button
import maindisplay

pygame.init()

# Window Name
pygame.display.set_caption("menu")

# Window Size
screen = pygame.display.set_mode((1280, 720))

   
def menu():
    
    button_positions = (560, 650)
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
    # Screen color | RGB
    screen.fill((128, 128, 128))
    while running:
        mouse_location = pygame.mouse.get_pos()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_press = pygame.mouse.get_pressed()
                if mouse_press[0] and mouse_location[0] >= 560 and mouse_location[0] <= 760 and mouse_location[1] >= 650 and mouse_location[1] <= 700:
                    # The button is clicked, perform your action
                    button.hide()  # Hide the button
                    
        pygame_widgets.update(events)
        pygame.display.update()

menu()
