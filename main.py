# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# https://youtu.be/ad0Ts8xdR-8

import sys
import time
from time import sleep

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

# Change 'firefox' to the browser you have installed. For example "selenium.webdriver.chrome.options" for chrome, you may check https://www.selenium.dev/documentation/webdriver/browsers/ for more information
from selenium.webdriver.firefox.options import Options

start = time.time()
print("\n\tTask has started... Please wait.")

options = Options()
options.page_load_strategy = "normal"
# Change 'firefox' to the browser you have installed
browser = webdriver.Firefox(options=options)
print("\n\tLoading website...")
browser.get(
    "https://ubpxcellerator.apptitude.xyz/course/blockchain-development-program-576"
)

# You can change these details to hardcode your login details
# username = input("\n\tEnter your username: ")
# password = input("\n\tEnter your password: ")
username = "Crept6114"
password = "Childcare-Harbor-Ethically7"

loginButton = browser.find_element(By.CLASS_NAME, "button-app")
loginButton.click()

sleep(1)

usernameField = browser.find_element(By.NAME, "username")
usernameField.send_keys(username)

passwordField = browser.find_element(By.NAME, "password")
passwordField.send_keys(password)

submitButton = browser.find_element(By.CLASS_NAME, "auth-button")
submitButton.click()

sleep(3)

resumeButton = browser.find_element(By.XPATH, '//button[text()="Resume Learning"]')
resumeButton.click()

sleep(3)

try:
    if browser.find_element(By.TAG_NAME, "video"):
        video = browser.find_element(By.TAG_NAME, "video")
        video.click()
except Exception as e:
    print("\n\tNo video detected.")


def endProcess():
    browser.quit()
    sys.exit()


def writeToTextAndPlay(video):
    video.click()
    # get src attribute of video
    videoSrc = video.get_attribute("src")
    textFile = open("videoURLs.txt", "a", encoding="utf-8")
    textFile.write(videoSrc)
    textFile.write("\n")
    textFile.close()


def checkIfTest():
    try:
        if browser.find_element(By.XPATH, '//h2[text()="Test My Learning"]'):
            print(
                "\n\tTest detected, please accomplish the test manually before resuming the script."
            )
            option = input("\n\tContinue running task? [ Y / N ] Default is yes.\n\t")
            match option.lower():
                case "n":
                    print("\n\tClosing browser...")
                    endProcess()
                case "y":
                    print("\n\tContinuing process...")
                    return
                case _:
                    print("\n\tContinuing process...")
                    return
    except:
        print("\n\tNo test detected.")
        return False


def checkForNewCourseware(initCoursewareList):
    newCoursewareList = []
    # Get the list of current coursewares and append it to the list
    courseware = browser.find_elements(By.XPATH, '//li[@style="cursor: pointer;"]')
    for course in courseware:
        newCoursewareList.append(course.text)
    # Check if there is a new courseware
    if len(initCoursewareList) < len(newCoursewareList):
        print("\n\tNew courseware detected.")
        clickCourseware = browser.find_element(
            By.XPATH, f'//p[text()="{initCoursewareList[-1]}"]'
        )
        clickCourseware.click()

        sleep(3)

        try:
            if browser.find_element(By.TAG_NAME, "video"):
                video = browser.find_element(By.TAG_NAME, "video")
                writeToTextAndPlay(video)
        except Exception as e:
            print("\n\tNo video detected.")
        return newCoursewareList
    else:
        print("\n\tNo new courseware detected.")
        return newCoursewareList


def runTask():
    # Initiate the list of currently available coursewares
    initCoursewareList = []
    courseware = browser.find_elements(By.XPATH, '//li[@style="cursor: pointer;"]')
    for course in courseware:
        initCoursewareList.append(course.text)
    # Check if there is a new courseware
    newCoursewareList = checkForNewCourseware(initCoursewareList)

    sleep(3)

    # Check if there is a test
    checkIfTest()

    if len(initCoursewareList) == len(newCoursewareList):
        print("\n\tVideo is currently playing.")
        sleep(60)
        runTask()


print("\n\tProcess started.")
runTask()

print("\n\tProcess is ending.")
browser.quit()

end = time.time()
print(
    "\n\tTask finished successfully. \n\t" + str(end - start) + " seconds has elapsed."
)
