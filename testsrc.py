try:
    import Image
except ImportError:
    from PIL import Image

import os, time, pytesseract

# from time import gmtime, strftime
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


delay = 9020//test

curtime = str(datetime.now())
dehour = delay / 3600
demin = (delay - dehour * 3600) / 60
desec = ((delay - dehour * 3600) - demin * 60)

curdate = curtime.split()[0]
curtime = curtime.split()[1]
curtime = curtime.split(":")

print(curtime)
curtime[2] = int(float(curtime[2])) + int(desec)
print(curtime[2])
while int(curtime[2]) > 60:
    curtime[1] += 1
    curtime[2] -= 60


curtime[1] += demin
while int(curtime[1]) > 60:
    curtime[0] += 1
    curtime[1] -= 60
