import pygame
import pygame_widgets
import cv2
import numpy as np
def output(b_h, b_s, b_l, t_h, t_s, t_l):
    cv_img = cv2.imread("pictures/baseimgs/room-1-with-obj.png")
    lower = np.array([b_h, b_s, b_l])
    upper = np.array([t_h, t_s, t_l])
    mask = cv2.inRange(cv_img, lower, upper)
    res = cv2.bitwise_and(cv_img, cv_img, mask= mask)
    cv2.imwrite("pictures/outputimgs/room-1-with-obj-change.png", res)
    
def setimg():
    img = pygame.image.load("pictures/outputimgs/room-1-with-obj-change.png").convert_alpha()
    return img