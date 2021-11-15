from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from ImgCompare import compare, show
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import playsound
from TextExtract import crop,textExtract


firefox_browser = webdriver.Firefox(executable_path=r'C:\Program Files\gecko\geckodriver.exe')


def runResultCheck():

    firefox_browser.get("http://results.drait.in/")
    time.sleep(2)
    print("Opening firefox")
    login_form = firefox_browser.find_element_by_xpath("//*[contains(text(), 'Student')]").click()
    time.sleep(6)
    delay = 80

    try:
        myElem = WebDriverWait(firefox_browser, delay).until(EC.presence_of_element_located((By.ID, 'ugpg')))
        print("Page is ready!")
        select = Select(firefox_browser.find_element_by_id('ugpg'))
        select.select_by_visible_text('UG-SEE')
        usn = firefox_browser.find_element_by_css_selector("#usn")
        submitButton = firefox_browser.find_element_by_css_selector("#submit")
        enterText = firefox_browser.find_element_by_css_selector("#captcha")

        text=textExtract()
        usn.send_keys("1DA17IS0xx")
        enterText.send_keys(text)

        firefox_browser.get_screenshot_as_file(r"C:\Users\V Sangarya\Desktop\ResultsHomePage.png")
        submitButton.send_keys(Keys.ENTER)
        show()

        
    except TimeoutException:
        print ("Loading took too much time!")
        runResultCheck()
    delay = 180

    
    try:
        myElem = WebDriverWait(firefox_browser, delay).until(EC.presence_of_element_located((By.ID, 'tableData')))
        print ("Page is ready!")
        firefox_browser.get_screenshot_as_file(r"C:\Users\V Sangarya\Desktop\screenshot.png")
        
    except TimeoutException:
        print ("Loading took too much time!")
        runResultCheck()

        
    print("Done")
    x=compare()
    
    if(x==1.0):
       print("Results not out")
       print(x)
       runResultCheck()
        
    else:
        print("Results out")
        print(x)
        playsound.playsound(r'C:\Users\V Sangarya\Downloads\AlertSound.mp3', True)

runResultCheck()
