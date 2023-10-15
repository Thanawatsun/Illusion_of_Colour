from skimage.metrics import structural_similarity
import cv2


def run(stage):
    ansimg = "pictures/checkimgs/room-%d-with-obj-check.png" % stage
    checkimg = "pictures/outputimgs/room-%d-with-obj-change.png" % stage

    first = cv2.imread(ansimg)
    second = cv2.imread(checkimg)

    # Convert images to grayscale
    first_gray = cv2.cvtColor(first, cv2.COLOR_BGR2GRAY)
    second_gray = cv2.cvtColor(second, cv2.COLOR_BGR2GRAY)

    # Compute SSIM between two images
    score, diff = structural_similarity(first_gray, second_gray, full=True)
    return "{:.3f}%".format(score * 100)
