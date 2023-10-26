import pygame, sys
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.button import Button

pygame.init()
import checkresult
import cv2
import numpy as np

# Window Name
pygame.display.set_caption("Illusion of Colour")

# Window Size
screen = pygame.display.set_mode((1280, 720))

def similarity_without_black(image1_path, image2_path, threshold=40):
    # โหลดภาพ
    img1 = cv2.imread(image1_path, cv2.IMREAD_COLOR)
    img2 = cv2.imread(image2_path, cv2.IMREAD_COLOR)
    
    # แปลงเป็น grayscale
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    
    # ใช้ thresholding เพื่อแยกสีดำ
    _, threshed1 = cv2.threshold(gray1, threshold, 255, cv2.THRESH_BINARY)
    _, threshed2 = cv2.threshold(gray2, threshold, 255, cv2.THRESH_BINARY)
    
    # นำส่วนของภาพที่ไม่ใช่สีดำมาคำนวณความคล้ายคลึง
    diff = cv2.absdiff(threshed1, threshed2)
    non_black_pixels = np.sum(diff != 0)
    total_pixels = np.sum(threshed1 != 0) + np.sum(threshed2 != 0)
    
    similarity = 1 - (non_black_pixels / total_pixels)
    
    return similarity


def result(stage):
    btmbut = pygame.image.load("image_UI/backToStart.png").convert_alpha()
    stagebg = "image_UI/backgroud-07.png"
    bgimg = pygame.image.load(stagebg).convert_alpha()
    image1 = "pictures/checkimgs/room-%d-with-obj-check.png" % stage
    image2 = "pictures/outputimgs/room-%d-with-obj-change.png" % stage

    similarity_percentage = similarity_without_black(image1, image2)
    #print(f"Similarity: {similarity_percentage * 100:.2f}%")
    Similarity = similarity_percentage * 100
    font = pygame.font.Font("freesansbold.ttf", 64)
    head = font.render("Your Score", True, (255, 255, 255))
    score = font.render('%.2f'%Similarity+"%", True, (255, 255, 255))
    #score = font.render(checkresult.run(stage), True, (255, 255, 255))
    while True:
        screen.fill((128, 128, 128))
        screen.blit(bgimg, (0, 0))
        screen.blit(head, (475, 165))
        screen.blit(score, (560, 299))
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
                    return   


        checkresult.run(stage)

        pygame_widgets.update(events)
        pygame.display.update()
