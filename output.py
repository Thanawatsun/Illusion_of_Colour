import pygame
import pygame_widgets
import cv2
import numpy as np

def output(b_h, b_s, b_l, t_h, t_s, t_l, stage):
    baseimg = "pictures/baseimgs/room-%d-with-obj.png" % stage
    changeimg = "pictures/outputimgs/room-%d-with-obj-change.png" % stage

    cv_img = cv2.imread(baseimg)
    lower = np.array([b_h, b_s, b_l])
    upper = np.array([t_h, t_s, t_l])
    mask = cv2.inRange(cv_img, lower, upper)
    res = cv2.bitwise_and(cv_img, cv_img, mask=mask)
    cv2.imwrite(changeimg, res)


def setimg(stage, mode):
    if mode == 1:
        changeimg = "pictures/baseimgs/room-%d-with-obj.png" % stage
        img = pygame.image.load(changeimg).convert_alpha()
        return img
    elif mode == 2:
        changeimg = "pictures/outputimgs/room-%d-with-obj-change.png" % stage
        img = pygame.image.load(changeimg).convert_alpha()
        return img
