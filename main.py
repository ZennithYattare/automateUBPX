# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# https://youtu.be/ad0Ts8xdR-8

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

# Initiate the list of currently available coursewares
initCoursewareList = []
courseware = browser.find_elements(By.XPATH, '//li[@style="cursor: pointer;"]')
for course in courseware:
    initCoursewareList.append(course.text)

# currentCourseware = browser.find_element(
#     By.XPATH,
#     '//li[@style="cursor: pointer; background-color: rgba(249, 141, 38, 0.24);"]',
# )
# Clicking Resume Learning button will automatically go to the most recent courseware so currentCourseware will be the last element in the list
# initCoursewareList.append(currentCourseware.text)


def writeToTextAndPlay(video):
    video.click()
    # get src attribute of video
    videoSrc = video.get_attribute("src")
    textFile = open("videoURLs.txt", "a", encoding="utf-8")
    textFile.write(videoSrc)
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
                    sleep(2)
                    browser.quit()
                case "y":
                    print("\n\tContinuing process...")
                case _:
                    print("\n\tContinuing process...")
    except:
        print("\n\tNo test detected.")
        return


def checkForNewCourseware(initCoursewareList):
    newCoursewareList = []
    # Get the list of current coursewares and append it to the list
    courseware = browser.find_elements(By.XPATH, '//li[@style="cursor: pointer;"]')
    for course in courseware:
        newCoursewareList.append(course.text)
    # Check if there is a new courseware
    if len(initCoursewareList) < len(newCoursewareList):
        print("\n\tNew courseware detected.")
        return newCoursewareList
    else:
        print("\n\tNo new courseware detected.")


def runTask(initCoursewareList):
    while True:
        initCoursewareList = checkForNewCourseware(initCoursewareList)
        clickCourseware = browser.find_element(
            By.XPATH, f'//p[text()="{initCoursewareList[-1]}"]'
        )
        clickCourseware.click()
        checkIfTest()

        try:
            if browser.find_element(By.TAG_NAME, "video"):
                video = browser.find_element(By.TAG_NAME, "video")
                writeToTextAndPlay(video)
        except Exception as e:
            print("\n\tNo video detected.")


sleep(10)
browser.quit()

end = time.time()
print(
    "\n\tTask finished successfully. \n\t" + str(end - start) + " seconds has elapsed."
)

# clickCourseware = browser.find_element(
#     By.XPATH, f'//p[text()="{initCoursewareList[1]}"]'
# )
# clickCourseware.click()


# counter = 0
# while True:
#     if browser.find_elements(By.CLASS_NAME, "map-title"):
#         # Click the first element found to close it as it is open when going to the webpage
#         buttonExpand = browser.find_element(By.CLASS_NAME, "map-title")
#         buttonExpand.click()
#         break
#     else:
#         # Sleep is needed to have time to load the webpage
#         if counter > 3:
#             break
#         sleep(1)
#     counter += 1

# # sleep(random.randint(180, 240) / 1000), uncomment this for input delay incase of undesirable result
# buttonExpand = browser.find_elements(By.CLASS_NAME, "map-title")
# for button in buttonExpand:
#     button.click()

# page = browser.page_source
# soup = BeautifulSoup(page, "html.parser")

# try:
#     # Create a text file to store the items for copy & paste
#     # Option to overwrite or append to tasks.txt
#     chmod = input("\n\tAppend? It will overwrite if not. [ Y / N ]\n\t")
#     match chmod:
#         case "N":
#             textFile = open("tasks.txt", "w", encoding="utf-8")
#             print("\n\tOverwriting tasks.txt...")
#         case "n":
#             textFile = open("tasks.txt", "w", encoding="utf-8")
#             print("\n\tOverwriting tasks.txt...")
#         case "Y":
#             textFile = open("tasks.txt", "a", encoding="utf-8")
#             print("\n\tAppending to tasks.txt...")
#         case "y":
#             textFile = open("tasks.txt", "a", encoding="utf-8")
#             print("\n\tAppending to tasks.txt...")
#         case _:
#             textFile = open("tasks.txt", "a", encoding="utf-8")
#             print("\n\tAppending to tasks.txt...")

#     # Get the titles of each div block
#     h3Titles = soup.find_all("h3", class_="big-block-title")
#     for _title in h3Titles:
#         textFile.write(_title.get_text())
#         textFile.write("\n")
#     textFile.write("\n\n")

#     # Looping through the Python List of unorderedList to find all of the child lists
#     unorderedList = soup.find_all("ul", class_="map-challenges-ul")
#     for _unorderedList in unorderedList:
#         childLists = _unorderedList.find_all("li")
#         # Loop through the child lists to find all of the anchor tags with the texts
#         for _list in childLists:
#             anchorTags = _list.find("a")
#             textFile.write(anchorTags.find(text=True, recursive=False))
#             textFile.write("\n")
#         textFile.write("\n")
#     textFile.write(
#         "____________________________________________________________________________________________________________"
#     )
#     textFile.write(
#         "____________________________________________________________________________________________________________\n\n\n"
#     )
# except Exception as e:
#     print(e)
#     textFile.close()
#     browser.quit()

# textFile.close()
# browser.quit()
