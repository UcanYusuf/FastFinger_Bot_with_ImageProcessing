# Libraries
import time
import cv2
import keyboard
import numpy as np
import pyautogui
import win32api
import win32con
from pytesseract import *
import pyperclip
from selenium.webdriver.support import expected_conditions as E
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ChromeOptions

def process(flag):
    if flag == False:
        wait_variable.until(E.presence_of_element_located((By.ID, "inputfield")))
        text_area = driver.find_element(By.ID, 'inputfield')
    else:
        wait_variable.until(E.presence_of_element_located((By.ID, "word-input")))
        text_area = driver.find_element(By.ID, 'word-input')

    pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'  # Change with your tesseract.exe path
    image = cv2.imread('text.png', 0)
    thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    if flag == False:
        data = pytesseract.image_to_string(thresh, lang='eng', config='--psm 6')
    else:
        data = pytesseract.image_to_string(thresh, lang='eng', config='--psm 1')

    print(data)
    words = data.split()
    for i in words:
        pyperclip.copy(i)
        spam = pyperclip.paste()
        if flag == False:
            text_area.send_keys(spam)
            text_area.send_keys(" ")
            time.sleep(0.25)  #If you decrease this value, bot will write faster but you can be banned. 
        else:
            text_area2.send_keys(spam)
            text_area2.send_keys(" ")
            time.sleep(0.20)  #If you decrease this value, bot will write faster but you can be banned.


service = ChromeService(executable_path="chromedriver.exe")
options = ChromeOptions()
options.add_argument("--kiosk")
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://10fastfingers.com//typing-test/english')  # Change with your language

wait_variable = W(driver, 20)

while True:
    try:
        x, y = pyautogui.locateCenterOnScreen('cookieButton.png', confidence=0.7)
        pyautogui.click(x, y)
        break
    except:
        pass

wait_variable.until(E.presence_of_element_located((By.XPATH, '//*[@id="speedtest-main"]/div[6]/div[1]/div[1]/a')))
driver.find_element(By.XPATH, '//*[@id="speedtest-main"]/div[6]/div[1]/div[1]/a').click()

wait_variable.until(E.presence_of_element_located((By.NAME, "data[User][email]")))
email_area = driver.find_element(By.NAME, 'data[User][email]')
email_area.send_keys("fastfinger2541@gmail.com")  # Change with your e-mail

wait_variable.until(E.presence_of_element_located((By.NAME, "data[User][password]")))
pass_area = driver.find_element(By.NAME, "data[User][password]")
pass_area.send_keys("25415434Aa.")  # Change with your password

wait_variable.until(E.presence_of_element_located((By.ID, "login-form-submit")))
driver.find_element(By.ID, "login-form-submit").click()

start_time = time.time()
timeValue = (time.time() - start_time)

region = [323, 267, 1180, 59]  # This values can change for different resolutions. Default 1920x1080

time.sleep(3)

while timeValue < 62.00:
    pic = pyautogui.screenshot(region=region)
    pic.save(r"text.png")
    img = cv2.imread("text.png")
    img = cv2.resize(img, None, fx=3.0, fy=3.0)
    cv2.imwrite("text.png", img)
    process(False)
    timeValue = (time.time() - start_time)

wait_variable.until(E.presence_of_element_located((By.XPATH, '//*[@id="notification-minibox"]/a')))
driver.find_element(By.XPATH, '//*[@id="notification-minibox"]/a').click()

start_time = time.time()
timeValue = (time.time() - start_time)

notification_flag = False

while timeValue < 10.00:
    try:
        x, y = pyautogui.locateCenterOnScreen('notifications_eng.png', confidence=0.7)  #Change it with notifications_tr.png to use in turkish.
        pyautogui.click(x, y)
        notification_flag = True
        break
    except:
        timeValue = (time.time() - start_time)

if notification_flag:
    wait_variable.until(E.presence_of_element_located((By.XPATH, '//*[@id="main-content"]/div[1]/table/tbody/tr[1]/td[1]/a')))
    driver.find_element(By.XPATH, '//*[@id="main-content"]/div[1]/table/tbody/tr[1]/td[1]/a').click()

    wait_variable.until(E.presence_of_element_located((By.XPATH, '//*[@id="start-btn"]')))
    driver.find_element(By.XPATH, '//*[@id="start-btn"]').click()

    time.sleep(1)
    region2 = [485, 290, 740, 205]  # This values can change for different resolutions. Default 1920x1080

    text_area2 = driver.find_element(By.ID, "word-input")
    pic = pyautogui.screenshot(region=region2)
    pic.save(r"text.png")
    img = cv2.imread("text.png", 0)
    img = cv2.resize(img, None, fx=3.0, fy=3.0)
    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    img = cv2.medianBlur(img, 11)
    cv2.imwrite("text.png", img)
    time.sleep(1)
    process(True)

    driver.find_element(By.ID, "submit-anticheat").click()
