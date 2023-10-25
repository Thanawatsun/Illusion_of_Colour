import pygame_widgets
import pygame
import cv2
import numpy as np
from pygame_widgets.toggle import Toggle
#from menus import menu
def test():
        # Example usage:
        image1 = remove_black("pictures/checkimgs/room-2-with-obj-check.png")
        image2 = remove_black("pictures/outputimgs/room-2-with-obj-change.png")

        similarity_percentage = compare_images_in_percentage(image1, image2)
        print(f"The similarity between the images is: {similarity_percentage}%")

def remove_black(image_path, threshold=40):
    # โหลดภาพ
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # กำหนดสีในภาพที่จะถูกถือว่าเป็น "ดำ" 
    threshed = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)
    
    return threshed

def compare_images_in_percentage(imageA, imageB):
            # The 'compare_ssim' function is part of 'scikit-image' so make sure to install it with pip
            from skimage.metrics import structural_similarity as ssim

            # Convert images to grayscale
            imageA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
            imageB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

            # Compute SSIM between two images
            similarity = ssim(imageA, imageB)
            
            # Convert the similarity to percentage and round it to 2 decimal places
            percentage_similarity = round(similarity * 100, 2)
            
            return percentage_similarity
test()