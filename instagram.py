# Well, this answers the question, "Why didn't the instagrabbers automate their instagram posts?", because it's ducking painful to do

import os

filesToUpload = []
with open("submitted.txt", "r") as f:
    filesAlreadyUploaded = f.readlines()

for files in os.listdir():
    if files + "\n" not in filesAlreadyUploaded and files.split(".")[-1] == "png":
        filesToUpload.append(files)
        with open("submitted.txt", "a") as f:
            f.write(files + "\n")

from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui as pog

driver = webdriver.Chrome("C:\\Users\\take2\\Desktop\\chromedriver_win32 (2)\\chromedriver.exe")
driver.get("https://www.instagram.com/")

username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
username.send_keys("lmao@gmail.com")

password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
password.send_keys("sendhelp")

i = 0
for element in driver.find_elements(By.TAG_NAME, "button"):
    if i == 1:
        element.click()
    i += 1

sleep(5)

forlackofsecurity = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "button")))
forlackofsecurity.click()

sleep(5)

notificationsdiv = driver.find_element(By.CLASS_NAME, "_a9-z")
notifications = notificationsdiv.find_element(By.TAG_NAME, "button")
notifications.click()

# LOGIN FREAKING COMPLETE!!! LET'S GOOOOOOOOOOOOOOO!!

print("a")
print(filesToUpload)
print("b")

for files in filesToUpload:
    sleep(2)

    uploaddiv = driver.find_element(By.CLASS_NAME, "_acub")
    upload = uploaddiv.find_element(By.TAG_NAME, "button")
    upload.click()

    clickupload = driver.find_element(By.XPATH, "//*[contains(text(), 'Select from computer')]")
    clickupload.click()

    sleep(2)

    pog.hotkey("ctrl", "l")
    pog.typewrite(r"C:\Users\take2\Documents\The Reddit Heist")
    pog.press("enter")

    pog.press("tab")
    pog.press("tab")
    pog.press("tab")
    pog.press("tab")
    pog.press("tab")

    pog.typewrite(files)
    pog.press("enter")

    sleep(2)

    next1 = driver.find_element(By.XPATH, "//*[contains(text(), 'Next')]")
    next1.click()

    sleep(2)

    next2 = driver.find_element(By.XPATH, "//*[contains(text(), 'Next')]")
    next2.click()

    sleep(2)

    share = driver.find_element(By.XPATH, "//*[contains(text(), 'Share')]")
    share.click()

    sleep(10)

    pog.press("escape")

driver.close()
