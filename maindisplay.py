import pygame, sys
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.button import Button
from output import *
import checkresult

pygame.init()

# Window Name
pygame.display.set_caption("Illusion of Colour")

# Window Size
screen = pygame.display.set_mode((1280, 720))


def result(stage):
    btmbut = pygame.image.load("image_UI/backToStart.png").convert_alpha()

    font = pygame.font.Font("freesansbold.ttf", 64)
    head = font.render("Your Score", True, (255, 255, 255))
    score = font.render(checkresult.run(stage), True, (255, 255, 255))

    while True:
        screen.fill((128, 128, 128))
        screen.blit(head, (475, 165))
        screen.blit(score, (491, 299))
        screen.blit(btmbut, (393, 433))

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
                    and mouse_location[0] >= 393
                    and mouse_location[0] <= 886
                    and mouse_location[1] >= 433
                    and mouse_location[1] <= 558
                ):
                    menu()

        checkresult.run(stage)

        pygame_widgets.update(events)
        pygame.display.update()


def main(stage):
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

    while True:
        # Screen color | RGB
        screen.fill((128, 128, 128))
        screen.blit(bgimg, (0, 0))
        screen.blit(bgimgframe, (23, 25))
        screen.blit(bgwantframe, (45, 492))
        screen.blit(bgsliderframe, (792, 26))
        screen.blit(submitbut, (820, 620))

        img = setimg(stage)

        # Place image in to screen
        screen.blit(img, (73, 50))

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
            stage
        )

        pygame_widgets.update(events)
        pygame.display.update()

def chosestage():
    backbut = pygame.image.load("image_UI/back.png").convert_alpha()
    stage1 = pygame.image.load("image_UI/stage01.png").convert_alpha()
    stage2 = pygame.image.load("image_UI/stage02.png").convert_alpha()
    stage3 = pygame.image.load("image_UI/stage03.png").convert_alpha()

    while True:
        screen.fill((128, 128, 128))
        screen.blit(backbut, (19, 15))
        screen.blit(stage1, (231, 235))
        screen.blit(stage2, (515, 235))
        screen.blit(stage3, (799, 235))

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
                    and mouse_location[0] >= 19
                    and mouse_location[0] <= 94
                    and mouse_location[1] >= 15
                    and mouse_location[1] <= 93
                ):
                    menu()
                elif (
                    mouse_press[0]
                    and mouse_location[0] >= 231
                    and mouse_location[0] <= 481
                    and mouse_location[1] >= 235
                    and mouse_location[1] <= 485
                ):
                    main(1)
                elif (
                    mouse_press[0]
                    and mouse_location[0] >= 515
                    and mouse_location[0] <= 765
                    and mouse_location[1] >= 235
                    and mouse_location[1] <= 485
                ):
                    main(2)
                elif (
                    mouse_press[0]
                    and mouse_location[0] >= 799
                    and mouse_location[0] <= 1049
                    and mouse_location[1] >= 235
                    and mouse_location[1] <= 485
                ):
                    main(3)

        pygame_widgets.update(events)
        pygame.display.update()

def help():
    returnbut = pygame.image.load("image_UI/return.png").convert_alpha()
    while True:
        screen.fill((128, 128, 128))
        screen.blit(returnbut, (490, 568))

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
                    and mouse_location[0] >= 490
                    and mouse_location[0] <= 790
                    and mouse_location[1] >= 568
                    and mouse_location[1] <= 692
                ):
                    menu()

        pygame_widgets.update(events)
        pygame.display.update()

def menu():
    playbut = pygame.image.load("image_UI/start.png").convert_alpha()
    helpbut = pygame.image.load("image_UI/help.png").convert_alpha()
    exitbut = pygame.image.load("image_UI/exit.png").convert_alpha()
    
    while True:
        screen.fill((128, 128, 128))
        screen.blit(playbut, (490, 153))
        screen.blit(helpbut, (490, 300))
        screen.blit(exitbut, (490, 447))

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
                    and mouse_location[0] >= 490
                    and mouse_location[0] <= 790
                    and mouse_location[1] >= 153
                    and mouse_location[1] <= 277
                ):
                    chosestage()
                elif (
                    mouse_press[0]
                    and mouse_location[0] >= 490
                    and mouse_location[0] <= 790
                    and mouse_location[1] >= 300
                    and mouse_location[1] <= 424
                ):
                    help()
                elif (
                    mouse_press[0]
                    and mouse_location[0] >= 490
                    and mouse_location[0] <= 790
                    and mouse_location[1] >= 447
                    and mouse_location[1] <= 571
                ):
                    pygame.quit()
                    sys.exit()

        pygame_widgets.update(events)
        pygame.display.update()


menu()
