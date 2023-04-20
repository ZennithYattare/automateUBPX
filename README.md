<!-- @format -->
**You need to accomplish the Privacy Notice or mark it as complete first before running this.**

**For the best chance of running without bugs/issues, don't run this script while you are on a Test. It should work for the most part...**

# automateUBPX for UBP Xcellerator Courses

Made and tested using the Blockchain Development Program on Firefox.
I made this as I don't like the video player they used and the inconsistent video naming scheme. It also saves the video URLs to a text file so you can copy and paste them and download them with a download manager for offline viewing. It was made in a short amount of time that works for my use case.

## Function(s) of the automateUBPX for UBP Xcellerator Courses Script

-   Hardcode your username and password credentials (or uncomment the input in the code)
-   Shows time elapsed of the program runtime at the end of program execution
-   Saves the video URLs to a text file

## Modules used:

-   [time()](https://docs.python.org/3/library/time.html)
-   [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
-   [Selenium WebDriver](https://www.selenium.dev/documentation/webdriver/)

## Installation:

```
pip install selenium
pip install beautifulsoup4
```

## Instruction:
Change 'firefox' to the browser you have installed. You may check https://www.selenium.dev/documentation/webdriver/browsers/ for more information
For example, I use Firefox:
```
from selenium.webdriver.firefox.options import Options
browser = webdriver.Firefox(options=options)
```
But for Chrome, it would be:
```
from selenium.webdriver.chrome.options import Options
browser = webdriver.Chrome(options=options)
```
