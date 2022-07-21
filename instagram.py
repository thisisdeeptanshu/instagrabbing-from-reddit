# Well, this answers the question, "Why didn't the instagrabbers automate their instagram posts?", because it's ducking painful to do

hashtags = "#wholesomememes #wholesome #wholesomegfmemes #wholesomememe #wholesomebfmemes #mood #cutememe #lovememes #memes #softmemes #loveandaffectionmemes #loveandaffection #purememes #wholesomeness #couplememes #crush #positivememes #crushmemes #couple #feelgood #relationshipmemes #sendthistoyourboyfriend #sendthistoyourgirlfriend #sendthistoyourcrush #relationships #couplegoals #memes #meme"

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

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://www.instagram.com/")

username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
username.send_keys("theofficialepicgames")

password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
password.send_keys("money")

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

pog.press("esc")

driver.get("https://www.instagram.com/theofficialepicgames/")
sleep(4.5)

for files in filesToUpload:
    uploaddiv = driver.find_element(By.CLASS_NAME, "_acub")
    upload = uploaddiv.find_element(By.TAG_NAME, "button")
    upload.click()

    clickupload = driver.find_element(By.XPATH, "//*[contains(text(), 'Select from computer')]")
    clickupload.click()

    sleep(2)

    pog.typewrite(os.getcwd() + "\\" + files)
    pog.press("enter")

    sleep(2)

    driver.find_element(By.XPATH, "//div[@class='_ab8w  _ab94 _ab95 _ab9f _ab9m _ab9p _abcm']").find_element(By.TAG_NAME, "button").click()
    sleep(0.5)
    driver.find_element(By.XPATH, "//*[contains(text(), 'Original')]").click()

    next1 = driver.find_element(By.XPATH, "//*[contains(text(), 'Next')]")
    next1.click()

    sleep(2)

    next2 = driver.find_element(By.XPATH, "//*[contains(text(), 'Next')]")
    next2.click()

    sleep(2)

    textarea = driver.find_element(By.TAG_NAME, "textarea")
    textarea.click()

    sleep(1)

    pog.typewrite("Tag your Bestie!")
    pog.press("enter")
    pog.typewrite("Follow for more!")
    pog.press("enter")

    sleep(1)

    pog.typewrite(hashtags)

    sleep(10)

    share = driver.find_element(By.XPATH, "//*[contains(text(), 'Share')]")
    share.click()

    sleep(10)

    pog.press("escape")

driver.close()
