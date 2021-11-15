import cv2
from PIL import Image
import skimage.measure as measure


def compare():
    imgFirst = cv2.imread(r"C:\Users\V Sangarya\Desktop\OriginalScreenshot.png")
    imgCheck = cv2.imread(r"C:\Users\V Sangarya\Desktop\screenshot.png")
    grayscaleImg1 = cv2.cvtColor(imgFirst, cv2.COLOR_BGR2GRAY)
    grayscaleImg2 = cv2.cvtColor(imgCheck, cv2.COLOR_BGR2GRAY)
    (similarity, difference) = measure.compare_ssim(grayscaleImg1, grayscaleImg2, full=True)
    return similarity

  
def show():
    im = Image.open(r"C:\Users\V Sangarya\Desktop\ResultsHomePage.png")
    width, height = im.size
    left = 5
    top = height / 4
    right = 164
    bottom = 3 * height / 4
    im1 = im.crop((left, top, right, bottom))
    im1.show()
