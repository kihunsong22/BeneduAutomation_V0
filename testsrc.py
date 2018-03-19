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


delay = 9050 #test

curtime = str(datetime.now())
dehour = int(delay / 3600)
demin = int((delay - dehour * 3600) / 60)
desec = int(((delay - dehour * 3600) - demin * 60))

# print(dehour)
# print(demin)
# print(desec)

curdate = curtime.split()[0]
curtime = curtime.split()[1]
curtime = curtime.split(":")

curtime[0] = int(float(curtime[0]))
curtime[1] = int(float(curtime[1]))
curtime[2] = int(float(curtime[2]))

# print("INIT : " + str(curtime))

curtime[2] -= desec  # 초단위 추가
while int(curtime[2]) < 0:
    curtime[1] -= 1
    curtime[2] += 60

curtime[1] -= demin  # 분단위 추가
while int(curtime[1]) < 0:
    curtime[0] -= 1
    curtime[1] += 60

curtime[0] -= dehour  # 시단위 추가
while int(curtime[0]) < 0:
    # 날짜를 다음으로 넘겨야 하는데 너무 귀찮아서 안했어
    curtime[0] += 1

restime = str(curtime[0]) + ":" + str(curtime[1]) + ":" + str(curtime[2]) + "  "
# print("RES : " + str(restime))
# IBU_BEGIN_DATE 는 curdate, IBU_BEGIN_TIME은 restime 변수에 저장되어 있음