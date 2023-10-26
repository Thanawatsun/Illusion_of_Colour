import pygame, sys
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.button import Button
from output import *
from results import *
pygame.init()
import checkresult

# Window Name

pygame.display.set_caption("Illusion of Colour")

# Window Size
screen = pygame.display.set_mode((1280, 720))
def play(stage):
    # Main background
    stagebg = "image_UI/backgroud-0%d.png" % stage
    bgimg = pygame.image.load(stagebg).convert_alpha()
    bgimgframe = pygame.image.load("image_UI/imageFrame.png").convert_alpha()
    bgwantframe = pygame.image.load("image_UI/wantFrame.png").convert_alpha()
    bgsliderframe = pygame.image.load("image_UI/sliderFrame.png").convert_alpha()
    submitbut = pygame.image.load("image_UI/submit.png").convert_alpha()

    # HSL
    top_hue = 0
    bottom_hue = 0
    top_Saturation = 0
    bottom_Saturation = 0
    top_Lightness = 0
    bottom_Lightness = 0

    # Slider
    t_h_slider = Slider(screen, 825, 75, 400, 25, min=0, max=255, step=1, initial=255)
    b_h_slider = Slider(screen, 825, 175, 400, 25, min=0, max=255, step=1, initial=0)
    t_s_slider = Slider(screen, 825, 275, 400, 25, min=0, max=255, step=1, initial=255)
    b_s_slider = Slider(screen, 825, 375, 400, 25, min=0, max=255, step=1, initial=0)
    t_l_slider = Slider(screen, 825, 475, 400, 25, min=0, max=255, step=1, initial=255)
    b_l_slider = Slider(screen, 825, 575, 400, 25, min=0, max=255, step=1, initial=0)

    # Load Font
    font = pygame.font.Font("freesansbold.ttf", 24)
    obj_font = pygame.font.Font("freesansbold.ttf", 64)

    if stage == 1:
        obj = "Wooden Chair"
    elif stage == 2:
        obj = "Clock"
    elif stage == 3:
        obj = "Statue of man"

    while True:
        # Get value from slider
        top_hue = t_h_slider.getValue()
        bottom_hue = b_h_slider.getValue()
        top_saturation = t_s_slider.getValue()
        bottom_saturation = b_s_slider.getValue()
        top_lightness = t_l_slider.getValue()
        bottom_lightness = b_l_slider.getValue()

        # Text Render
        top_hue_show = font.render("Highest Hue : %d" %top_hue, True, (255, 255, 255))
        bottom_hue_show = font.render("Lowest Hue : %d" %bottom_hue, True, (255, 255, 255))
        top_saturation_show = font.render("Highest Saturation : %d" %top_saturation, True, (255, 255, 255))
        bottom_saturation_show = font.render("Lowest Saturation : %d" %bottom_saturation, True, (255, 255, 255))
        top_lightness_show = font.render("Highest Lightness : %d" %top_lightness, True, (255, 255, 255))
        bottom_lightness_show = font.render("Lowest Lightness : %d" %bottom_lightness, True, (255, 255, 255))
        obj_show = obj_font.render(obj, True, (255, 255, 255))

        output(
            bottom_hue,
            bottom_saturation,
            bottom_lightness,
            top_hue,
            top_saturation,
            top_lightness,
            stage
        )
        img = setimg(stage)

        # Screen color | RGB
        screen.fill((128, 128, 128))
        screen.blit(bgimg, (0, 0))
        screen.blit(bgimgframe, (23, 25))
        screen.blit(bgwantframe, (45, 492))
        screen.blit(bgsliderframe, (792, 26))
        screen.blit(submitbut, (820, 620))

        # Place image in to screen
        screen.blit(img, (73, 50))

        # Place text
        screen.blit(top_hue_show, (825, 40))
        screen.blit(bottom_hue_show, (825, 140))
        screen.blit(top_saturation_show, (825, 240))
        screen.blit(bottom_saturation_show, (825, 340))
        screen.blit(top_lightness_show, (825, 440))
        screen.blit(bottom_lightness_show, (825, 540))
        screen.blit(obj_show, (100, 560))

        mouse_location = pygame.mouse.get_pos()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_press = pygame.mouse.get_pressed()
                if (
                    mouse_press[0]
                    and mouse_location[0] >= 820
                    and mouse_location[0] <= 1230
                    and mouse_location[1] >= 620
                    and mouse_location[1] <= 686
                ):
                    
                    t_h_slider.hide()
                    b_h_slider.hide()
                    t_s_slider.hide()
                    b_s_slider.hide()
                    t_l_slider.hide()
                    b_l_slider.hide()
                    result(stage)
                    return

        pygame_widgets.update(events)
        pygame.display.update()

