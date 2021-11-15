import numpy as np
import time
from selenium import webdriver
from PIL import Image
import cv2
import pytesseract


def crop():
    try:
        firefox_browser = webdriver.Firefox(executable_path=r'C:\Program Files\gecko\geckodriver.exe')
        time.sleep(2)
        firefox_browser.get("http://results.drait.in/")
        time.sleep(2)
        login_form = firefox_browser.find_element_by_xpath("//*[contains(text(), 'Student')]").click()
        time.sleep(4)
        firefox_browser.get_screenshot_as_file(r"C:\Users\V Sangarya\Desktop\ResultsHomePage.png")
        im = Image.open(r"C:\Users\V Sangarya\Desktop\ResultsHomePage.png")
        im1 = im.crop((600, 235, 1050, 280))
        im1.show()
        im1.save(r"C:\Users\V Sangarya\Desktop\CaptchaCropped.png")
        return "Success",
      
    except:
        return "Failed"

      
def textExtract():
    cropCode=crop()
    
    if cropCode == "Success":
        img = cv2.imread(r"C:\Users\V Sangarya\Desktop\CaptchaCropped.png")
        config = ('-l eng --oem 1 --psm 3')
        pytesseract.pytesseract.tesseract_cmd = r'C:\Users\V Sangarya\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        kernel = np.ones((1, 1), np.uint8)
        img = cv2.dilate(img, kernel, iterations=1)
        img = cv2.erode(img, kernel, iterations=1)
        img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
        text = pytesseract.image_to_string(img, config=config)
        return text
      
    else:
        print("Retry, image crop failed")
