import pygame, sys
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.button import Button
from output import *
from gameplay import *
import checkresult

pygame.init()

# Window Name
pygame.display.set_caption("Illusion of Colour")
pygame_icon = pygame.image.load('image_UI\logo.png')
pygame.display.set_icon(pygame_icon)
# Window Size
screen = pygame.display.set_mode((1280, 720))
def chosestage():
    backbut = pygame.image.load("image_UI/back.png").convert_alpha()
    stage1 = pygame.image.load("image_UI/stage01.png").convert_alpha()
    stage2 = pygame.image.load("image_UI/stage02.png").convert_alpha()
    stage3 = pygame.image.load("image_UI/stage03.png").convert_alpha()
    stagebg = "image_UI/backgroud-04.png"
    bgimg = pygame.image.load(stagebg).convert_alpha()
    while True:
        screen.fill((128, 128, 128))
        screen.blit(bgimg, (0, 0))
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
                    play(1)
                    
                elif (
                    mouse_press[0]
                    and mouse_location[0] >= 515
                    and mouse_location[0] <= 765
                    and mouse_location[1] >= 235
                    and mouse_location[1] <= 485
                ):
                    play(2)
                    
                elif (
                    mouse_press[0]
                    and mouse_location[0] >= 799
                    and mouse_location[0] <= 1049
                    and mouse_location[1] >= 235
                    and mouse_location[1] <= 485
                ):
                    play(3)
                    

        pygame_widgets.update(events)
        pygame.display.update()

def help():
    returnbut = pygame.image.load("image_UI/return.png").convert_alpha()
    stagebg = "image_UI/backgroud-05.png"
    bgimg = pygame.image.load(stagebg).convert_alpha()
    font = pygame.font.Font("freesansbold.ttf", 36)
    help_1 = font.render("In this game, you need to get the object out of the picture by changing", True, (255, 255, 255))
    help_2 = font.render("the color range. You will get instructions about what object we need.", True, (255, 255, 255))
    help_3 = font.render("After that, you need to change the slider, which indicates the range of", True, (255, 255, 255))
    help_4 = font.render("hue, saturation, and lightness. If you do it right, the background will", True, (255, 255, 255))
    help_5 = font.render("fade to black, leaving only the object we want on the screen. If you are", True, (255, 255, 255))
    help_6 = font.render("sure about the result, press submit, and then the game will check how", True, (255, 255, 255))
    help_7 = font.render("good your result is, ranging from 0 to 100.", True, (255, 255, 255))

    while True:
        screen.fill((128, 128, 128))
        screen.blit(bgimg, (0, 0))
        screen.blit(returnbut, (490, 568))

        screen.blit(help_1, (20, 20))
        screen.blit(help_2, (20, 60))
        screen.blit(help_3, (20, 100))
        screen.blit(help_4, (20, 140))
        screen.blit(help_5, (20, 180))
        screen.blit(help_6, (20, 220))
        screen.blit(help_7, (20, 260))

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
    
    BACK_TO_MENU = pygame.USEREVENT + 1
    stagebg = "image_UI/backgroud-06.png"
    bgimg = pygame.image.load(stagebg).convert_alpha()
    logo = pygame.image.load("image_UI/Illusion-of-Colour.png").convert_alpha()
    playbut = pygame.image.load("image_UI/start.png").convert_alpha()
    helpbut = pygame.image.load("image_UI/help.png").convert_alpha()
    exitbut = pygame.image.load("image_UI/exit.png").convert_alpha()
    
    while True:
        
        screen.fill((128, 128, 128))
        screen.blit(bgimg, (0, 0))
        screen.blit(logo, (300, 30))
        screen.blit(playbut, (490, 273))
        screen.blit(helpbut, (490, 420))
        screen.blit(exitbut, (490, 577))
        

        mouse_location = pygame.mouse.get_pos()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == BACK_TO_MENU:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_press = pygame.mouse.get_pressed()
                if (
                    mouse_press[0]
                    and mouse_location[0] >= 490
                    and mouse_location[0] <= 790
                    and mouse_location[1] >= 273
                    and mouse_location[1] <= 397
                ):
                    chosestage()
                elif (
                    mouse_press[0]
                    and mouse_location[0] >= 490
                    and mouse_location[0] <= 790
                    and mouse_location[1] >= 420
                    and mouse_location[1] <= 524
                ):
                    help()
                elif (
                    mouse_press[0]
                    and mouse_location[0] >= 490
                    and mouse_location[0] <= 790
                    and mouse_location[1] >= 577
                    and mouse_location[1] <= 701
                ):
                    pygame.quit()
                    sys.exit()
        pygame_widgets.update(events)
        pygame.display.update()

