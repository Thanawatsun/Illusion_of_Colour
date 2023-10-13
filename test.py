class GFG: 
	
	# methods 
	def add(self, a, b): 
		return a + b 
	def sub(self, a, b): 
		return a - b 

# explicit function	 
def method(): 
	print("GFG")

from skimage.metrics import structural_similarity
import cv2

def run():
    first = cv2.imread('pictures/checkimgs/room-1-with-obj-check.png')
    second = cv2.imread('pictures/outputimgs/room-1-with-obj-change.png')

    # Convert images to grayscale
    first_gray = cv2.cvtColor(first, cv2.COLOR_BGR2GRAY)
    second_gray = cv2.cvtColor(second, cv2.COLOR_BGR2GRAY)

    # Compute SSIM between two images
    score = structural_similarity(first_gray, second_gray, full=True)
    print("Similarity Score: {:.3f}%".format(score * 100))
