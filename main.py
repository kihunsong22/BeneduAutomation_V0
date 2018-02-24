# BenEdu Test Sheets should be have word TEST in capital    ex) TEST2
#
# pyuic5 -x main.ui -o mainGUI.py
#

try:
    import Image
except ImportError:
    from PIL import Image

import os, time, pytesseract

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('chromedriver.exe')
pytesseract.pytesseract.tesseract_cmd = 'Tesseract-OCR/tesseract.exe'

mainUrl = 'http://benedu.co.kr/Index.aspx'
homeUrl = 'https://www.benedu.co.kr/Views/01_Students/00StdHome.aspx'
learnUrl = 'https://www.benedu.co.kr/Views/01_Students/03StdStudy02PaperTestList.aspx'
probUrl = 'https://www.benedu.co.kr/Views/01_Students/03StdStudy01Question.aspx'

def createtestsheet(loop, value):
    # try:
    driver.get(probUrl)
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id=\"tab_tag_1_1\"]')))
    while True:
        if EC.presence_of_all_elements_located:
            break
        else:
            continue

    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="body_rdoSbjCode_0"]')))
    driver.find_element_by_xpath('//*[@id="body_rdoSbjCode_0"]').click()
    time.sleep(1)
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="body_chkGrade1"]')))
    driver.find_element_by_xpath('//*[@id="body_chkGrade1"]').click()
    time.sleep(2)
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="body_chkSrc01"]')))
    driver.find_element_by_xpath('//*[@id="body_chkSrc01"]').click()
    time.sleep(2)
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="body_chkMonth03"]')))
    driver.find_element_by_xpath('//*[@id="body_chkMonth03"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="body_chkMonth06"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="body_chkMonth09"]').click()

    while True:
        if EC.visibility_of_element_located:
            break
        else:
            continue

    while driver.find_element_by_xpath('//*[@id="body_txtYearFrom"]').get_attribute("value") != '2016':
        time.sleep(0.2)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="body_txtYearFrom"]')))
        driver.find_element_by_xpath('//*[@id="body_txtYearFrom"]').clear()
        time.sleep(1)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="body_txtYearFrom"]')))
        driver.find_element_by_xpath('//*[@id="body_txtYearFrom"]').send_keys('2016')
        time.sleep(1)
        continue

    # ============================== 이부분은 2018년부터 사용하는걸로
    # WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="body_txtYearTo"]')))
    # driver.find_element_by_xpath('//*[@id="body_txtYearTo"]').clear()
    # time.sleep(1)
    # WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="body_txtYearTo"]')))
    # driver.find_element_by_xpath('//*[@id="body_txtYearTo"]').send_keys('2017')
    # time.sleep(1)

    driver.find_element_by_xpath('//*[@id="body_udpMain_1"]/div[1]/div[1]/table/tbody/tr[6]/td[1]').click()

    while driver.find_element_by_xpath('//*[@id="body_TextBox2"]').get_attribute("value") != '45':
        time.sleep(0.2)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="body_TextBox2"]')))
        driver.find_element_by_xpath('//*[@id="body_TextBox2"]').clear()
        time.sleep(1)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="body_TextBox2"]')))
        driver.find_element_by_xpath('//*[@id="body_TextBox2"]').send_keys('45')
        time.sleep(1)
        continue

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="body_btnExecute"]')))
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="body_btnExecute"]').send_keys(Keys.ENTER)

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="body_txtTestName"]')))
    driver.find_element_by_xpath('//*[@id="body_txtTestName"]').send_keys('TEST' + str(value * 1 + loop))
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btnSave2"]')))
    driver.find_element_by_xpath('//*[@id="btnSave2"]').click()
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="btnYES"]')))
    time.sleep(0.1)
    # except:
    #     print('DEBUG: CREATESHEET ERROR!')

    driver.get(learnUrl)


def solveTest(loop, value, delay):
    # --------------------------------------------------HTML Parsing
    prob1 = str('987')
    prob2 = str('987')
    prob3 = str('987')
    prob4 = str('987')
    prob5 = str('987')
    answerSheet = []

    html = driver.page_source
    parpage = str(BeautifulSoup(html, 'html.parser'))

    print('DEBUG: parsing through HTML')

    prob1source = parpage[parpage.find('출처 : '):parpage.find('분류 : ')]
    leftpage = parpage[parpage.find('<b>' + str(value * 5 - 3) + '번'):]
    prob2source = leftpage[leftpage.find('출처 : '):leftpage.find('분류 : ')]
    leftpage = leftpage[leftpage.find('<b>' + str(value * 5 - 2) + '번'):]
    prob3source = leftpage[leftpage.find('출처 : '):leftpage.find('분류 : ')]
    leftpage = leftpage[leftpage.find('<b>' + str(value * 5 - 1) + '번'):]
    prob4source = leftpage[leftpage.find('출처 : '):leftpage.find('분류 : ')]
    leftpage = leftpage[leftpage.find('<b>' + str(value * 5) + '번'):]
    prob5source = leftpage[leftpage.find('출처 : '):leftpage.find('분류 : ')]

    # TEXT 잘라내기 -> 연도/번호 저장
    prob1l = prob1source.split()
    prob2l = prob2source.split()
    prob3l = prob3source.split()
    prob4l = prob4source.split()
    prob5l = prob5source.split()

    # 연도/번호 저장
    print(prob1l)

    num1.year = int(list(filter(lambda x: "년" in x, prob1l))[1][:list(filter(lambda x: "년" in x, prob1l))[1].find("년")])
    num1.month = int(list(filter(lambda x: "월" in x, prob1l))[0][:list(filter(lambda x: "번" in x, prob1l))[0].find("월")])
    num1.num = int(list(filter(lambda x: "번" in x, prob1l))[0][:list(filter(lambda x: "번" in x, prob1l))[0].find("번")])

    print()
    print(list(filter(lambda x: "번" in x, prob1l))[0][:list(filter(lambda x: "번" in x, prob1l))[0].find("번")])
    print()

    num2.year = int(list(filter(lambda x: "년" in x, prob2l))[1][:list(filter(lambda x: "년" in x, prob2l))[1].find("년")])
    num2.month = int(list(filter(lambda x: "월" in x, prob2l))[0][:list(filter(lambda x: "번" in x, prob2l))[0].find("월")])
    num2.num = int(list(filter(lambda x: "번" in x, prob2l))[0][:list(filter(lambda x: "번" in x, prob2l))[0].find("번")])

    num3.year = int(list(filter(lambda x: "년" in x, prob3l))[1][:list(filter(lambda x: "년" in x, prob3l))[1].find("년")])
    num3.month = int(list(filter(lambda x: "월" in x, prob3l))[0][:list(filter(lambda x: "번" in x, prob3l))[0].find("월")])
    num3.num = int(list(filter(lambda x: "번" in x, prob3l))[0][:list(filter(lambda x: "번" in x, prob3l))[0].find("번")])

    num4.year = int(list(filter(lambda x: "년" in x, prob4l))[1][:list(filter(lambda x: "년" in x, prob4l))[1].find("년")])
    num4.month = int(list(filter(lambda x: "월" in x, prob4l))[0][:list(filter(lambda x: "번" in x, prob4l))[0].find("월")])
    num4.num = int(list(filter(lambda x: "번" in x, prob4l))[0][:list(filter(lambda x: "번" in x, prob4l))[0].find("번")])

    num5.year = int(list(filter(lambda x: "년" in x, prob5l))[1][:list(filter(lambda x: "년" in x, prob5l))[1].find("년")])
    num5.month = int(list(filter(lambda x: "월" in x, prob5l))[0][:list(filter(lambda x: "번" in x, prob5l))[0].find("월")])
    num5.num = int(list(filter(lambda x: "번" in x, prob5l))[0][:list(filter(lambda x: "번" in x, prob5l))[0].find("번")])

    # ----------------------------------------------------------------------------------------------------정답안 입력
    # try:
    time.sleep(0.2)
    if(num1.year==2017 and num1.month==3):
        answerSheet = list(y2017m3)
    elif(num1.year==2017 and num1.month==6):
        answerSheet = list(y2017m6)
    elif(num1.year==2017 and num1.month==9):
        answerSheet = list(y2017m9)
    elif(num1.year==2016 and num1.month==3):
        answerSheet = list(y2016m3)
    elif(num1.year==2016 and num1.month==6):
        answerSheet = list(y2016m6)
    elif(num1.year==2016 and num1.month==9):
        answerSheet = list(y2016m9)

    # if not(1<=int(num1.num)<=5):
    #     num1.num = 3
    time.sleep(0.1)
    driver.find_element_by_xpath(
        '//*[@id=\"btn_' + str((value - 1) * 5 + 1) + '_' + str(answerSheet[int(num1.num) - 1]) + '\"]').click()
    print(num1.num)

    if(num2.year==2017 and num2.month==3):
        answerSheet = list(y2017m3)
    elif(num2.year==2017 and num2.month==6):
        answerSheet = list(y2017m6)
    elif(num2.year==2017 and num2.month==9):
        answerSheet = list(y2017m9)
    elif(num2.year==2016 and num2.month==3):
        answerSheet = list(y2016m3)
    elif(num2.year==2016 and num2.month==6):
        answerSheet = list(y2016m6)
    elif(num2.year==2016 and num2.month==9):
        answerSheet = list(y2016m9)

    # if not(1<=int(num2.num)<=5):
    #     num2.num = 3
    time.sleep(0.1)
    driver.find_element_by_xpath(
        '//*[@id=\"btn_' + str((value - 1) * 5 + 2) + '_' + str(answerSheet[int(num2.num) - 1]) + '\"]').click()
    print(num2.num)

    if(num3.year==2017 and num3.month==3):
        answerSheet = list(y2017m3)
    elif(num3.year==2017 and num3.month==6):
        answerSheet = list(y2017m6)
    elif(num3.year==2017 and num3.month==9):
        answerSheet = list(y2017m9)
    elif(num3.year==2016 and num3.month==3):
        answerSheet = list(y2016m3)
    elif(num3.year==2016 and num3.month==6):
        answerSheet = list(y2016m6)
    elif(num3.year==2016 and num3.month==9):
        answerSheet = list(y2016m9)

    # if not(1<=int(num3.num)<=5):
    #     num3.num = 3
    time.sleep(0.1)
    driver.find_element_by_xpath(
        '//*[@id=\"btn_' + str((value - 1) * 5 + 3) + '_' + str(answerSheet[int(num3.num) - 1]) + '\"]').click()
    print(num3.num)

    if(num4.year==2017 and num4.month==3):
        answerSheet = list(y2017m3)
    elif(num4.year==2017 and num4.month==6):
        answerSheet = list(y2017m6)
    elif(num4.year==2017 and num4.month==9):
        answerSheet = list(y2017m9)
    elif(num4.year==2016 and num4.month==3):
        answerSheet = list(y2016m3)
    elif(num4.year==2016 and num4.month==6):
        answerSheet = list(y2016m6)
    elif(num4.year==2016 and num4.month==9):
        answerSheet = list(y2016m9)

    # if not(1<=int(num4.num)<=5):
    #     num4.num = 3
    time.sleep(0.1)
    driver.find_element_by_xpath(
        '//*[@id=\"btn_' + str((value - 1) * 5 + 4) + '_' + str(answerSheet[int(num4.num) - 1]) + '\"]').click()
    print(num4.num)

    if(num5.year==2017 and num5.month==3):
        answerSheet = list(y2017m3)
    elif(num5.year==2017 and num5.month==6):
        answerSheet = list(y2017m6)
    elif(num5.year==2017 and num5.month==9):
        answerSheet = list(y2017m9)
    elif(num5.year==2016 and num5.month==3):
        answerSheet = list(y2016m3)
    elif(num5.year==2016 and num5.month==6):
        answerSheet = list(y2016m6)
    elif(num5.year==2016 and num5.month==9):
        answerSheet = list(y2016m9)

    # if not(1<=int(num5.num)<=5):
    #     num5.num = 3
    time.sleep(0.1)
    driver.find_element_by_xpath(
        '//*[@id=\"btn_' + str((value - 1) * 5 + 5) + '_' + str(answerSheet[int(num5.num) - 1]) + '\"]').click()
    print(num5.num)

    # delay = delay + random.random(-3, 3)
    time.sleep(delay)
    bypassocr()

    return 0

# except:
#     value += 1
#     return 1


def bypassocr():
    driver.find_element_by_xpath('//*[@id=\"btnSubmit\"]').click()
    time.sleep(0.5)
    # -------------------------스크린샷 저장 후 OCR 처리.입력

    WebDriverWait(driver, 8).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="body_imgMacro"]')))

    driver.get_screenshot_as_file('screenshots/captcha.png')
    time.sleep(0.2)
    pilimg = Image.open('screenshots/captcha.png')
    time.sleep(0.2)
    pilimg.size = 1920, 1080
    pilimg.crop((850, 340, 1050, 400)).save('screenshots/captcha.png')

    captcha = pytesseract.image_to_string(Image.open('screenshots/captcha.png'))
    captcha = captcha.replace(' ', '')

    time.sleep(0.1)
    driver.find_element_by_xpath('//*[@id=\"body_txtMacro\"]').send_keys(captcha)
    driver.find_element_by_xpath('//*[@id=\"AntiMacroForm\"]/div/div/div[3]/div/div[2]/button').click()

    time.sleep(0.2)
    driver.get(learnUrl)


# --------------------------------------------------답안 데이터 입력


class ProbData:
    year = 0
    month = 0
    num = 0
    answer = 0


answerSheet = []

loop = 1
value = 1
revalue = 1

num1 = ProbData()
num2 = ProbData()
num3 = ProbData()
num4 = ProbData()
num5 = ProbData()

# 답안 데이터 저장 _ 2016.03
temp = '1 ② 2 ④ 3 ④ 4 ⑤ 5 ③ 6 ② 7 ④ 8 ③ 9 ④ 10 ④ 11 ① 12 ④ 13 ② 14 ⑤ 15 ③ 16 ⑤ 17 ④ 18 ③ 19 ' \
       '① 20 ③ 21 ① 22 ② 23 ① 24 ⑤ 25 ② 26 ① 27 ⑤ 28 ⑤ 29 ⑤ 30 ② 31 ③ 32 ③ 33 ④ 34 ⑤ 35 ⑤ 36 ' \
       '④ 37 ⑤ 38 ③ 39 ① 40 ① 41 ② 42 ② 43 ③ 44 ④ 45 ① '
temp = temp.split()
temp = list(temp)
y2016m3 = list(temp)

for i in range(0, 90):
    if temp[i].isdigit():
        try:
            del y2016m3[i]
        except:
            pass

for i in range(1, 51):
    y2016m3 = [w.replace('①', '1') for w in y2016m3]
    y2016m3 = [w.replace('②', '2') for w in y2016m3]
    y2016m3 = [w.replace('③', '3') for w in y2016m3]
    y2016m3 = [w.replace('④', '4') for w in y2016m3]
    y2016m3 = [w.replace('⑤', '5') for w in y2016m3]


# 답안 데이터 저장 _ 2016.06
temp = '1 ④ 2 ③ 3 ④ 4 ⑤ 5 ① 6 ⑤ 7 ⑤ 8 ⑤ 9 ① 10 ① 11 ④ 12 ① 13 ② 14 ④ 15 ⑤ 16 ③ 17 ④ 18 ① 19 ' \
       '② 20 ① 21 ② 22 ③ 23 ③ 24 ② 25 ② 26 ① 27 ③ 28 ② 29 ④ 30 ② 31 ② 32 ④ 33 ① 34 ① 35 ⑤ 36 ' \
       '② 37 ③ 38 ① 39 ④ 40 ③ 41 ⑤ 42 ⑤ 43 ③ 44 ④ 45 ③ '
temp = temp.split()
temp = list(temp)
y2016m6 = list(temp)

for i in range(0, 90):
    if temp[i].isdigit():
        try:
            del y2016m6[i]
        except:
            pass

for i in range(1, 51):
    y2016m6 = [w.replace('①', '1') for w in y2016m6]
    y2016m6 = [w.replace('②', '2') for w in y2016m6]
    y2016m6 = [w.replace('③', '3') for w in y2016m6]
    y2016m6 = [w.replace('④', '4') for w in y2016m6]
    y2016m6 = [w.replace('⑤', '5') for w in y2016m6]

# 답안 데이터 저장 _ 2016.09
temp = '1 ③ 2 ① 3 ③ 4 ① 5 ③ 6 ④ 7 ② 8 ⑤ 9 ④ 10 ③ 11 ② 12 ⑤ 13 ③ 14 ⑤ 15 ② 16 ④ 17 ③ 18 ⑤ 19 ' \
       '④ 20 ② 21 ⑤ 22 ① 23 ③ 24 ⑤ 25 ⑤ 26 ④ 27 ① 28 ① 29 ② 30 ① 31 ③ 32 ② 33 ④ 34 ④ 35 ② 36 ' \
       '② 37 ④ 38 ④ 39 ⑤ 40 ② 41 ① 42 ② 43 ⑤ 44 ③ 45 ③ '
temp = temp.split()
temp = list(temp)
y2016m9 = list(temp)

for i in range(0, 90):
    if temp[i].isdigit():
        try:
            del y2016m9[i]
        except:
            pass

for i in range(1, 51):
    y2016m9 = [w.replace('①', '1') for w in y2016m9]
    y2016m9 = [w.replace('②', '2') for w in y2016m9]
    y2016m9 = [w.replace('③', '3') for w in y2016m9]
    y2016m9 = [w.replace('④', '4') for w in y2016m9]
    y2016m9 = [w.replace('⑤', '5') for w in y2016m9]

# 답안 데이터 저장 _ 2017.03
temp = '1 ③ 2 ③ 3 ⑤ 4 ⑤ 5 ③ 6 ② 7 ③ 8 ⑤ 9 ② 10 ① 11 ④ 12 ④ 13 ① 14 ⑤ 15 ① 16 ⑤ 17 ① 18 ③ 19 ' \
       '② 20 ① 21 ③ 22 ② 23 ③ 24 ① 25 ④ 26 ③ 27 ③ 28 ① 29 ⑤ 30 ① 31 ⑤ 32 ③ 33 ② 34 ④ 35 ⑤ 36 ' \
       '⑤ 37 ④ 38 ④ 39 ④ 40 ① 41 ② 42 ② 43 ② 44 ⑤ 45 ②'
temp = temp.split()
temp = list(temp)
y2017m3 = list(temp)

for i in range(0, 90):
    if temp[i].isdigit():
        try:
            del y2017m3[i]
        except:
            pass

for i in range(1, 51):
    y2017m3 = [w.replace('①', '1') for w in y2017m3]
    y2017m3 = [w.replace('②', '2') for w in y2017m3]
    y2017m3 = [w.replace('③', '3') for w in y2017m3]
    y2017m3 = [w.replace('④', '4') for w in y2017m3]
    y2017m3 = [w.replace('⑤', '5') for w in y2017m3]

# 답안 데이터 저장 _ 2017.06
temp = '1 ② 2 ④ 3 ① 4 ④ 5 ⑤ 6 ③ 7 ③ 8 ① 9 ⑤ 10 ③ 11 ① 12 ① 13 ② 14 ② 15 ④ 16 ⑤ 17 ① 18 ③ 19 ' \
       '⑤ 20 ⑤ 21 ② 22 ③ 23 ④ 24 ④ 25 ③ 26 ③ 27 ② 28 ④ 29 ⑤ 30 ③ 31 ① 32 ① 33 ④ 34 ③ 35 ④ 36 ' \
       '④ 37 ⑤ 38 ③ 39 ② 40 ⑤ 41 ① 42 ⑤ 43 ② 44 ⑤ 45 ②'
temp = temp.split()
temp = list(temp)
y2017m6 = list(temp)

for i in range(0, 90):
    if temp[i].isdigit():
        try:
            del y2017m6[i]
        except:
            pass

for i in range(1, 51):
    y2017m6 = [w.replace('①', '1') for w in y2017m6]
    y2017m6 = [w.replace('②', '2') for w in y2017m6]
    y2017m6 = [w.replace('③', '3') for w in y2017m6]
    y2017m6 = [w.replace('④', '4') for w in y2017m6]
    y2017m6 = [w.replace('⑤', '5') for w in y2017m6]

# 답안 데이터 저장 _ 2017.09
temp = '1 ② 2 ⑤ 3 ④ 4 ④ 5 ② 6 ④ 7 ④ 8 ① 9 ① 10 ⑤ 11 ⑤ 12 ⑤ 13 ③ 14 ① 15 ② 16 ① 17 ④ 18 ③ 19 ' \
       '④ 20 ③ 21 ③ 22 ⑤ 23 ① 24 ③ 25 ① 26 ④ 27 ② 28 ⑤ 29 ④ 30 ② 31 ⑤ 32 ③ 33 ② 34 ③ 35 ④ 36 ' \
       '② 37 ⑤ 38 ⑤ 39 ② 40 ④ 41 ② 42 ③ 43 ① 44 ⑤ 45 ⑤ '
temp = temp.split()
temp = list(temp)
y2017m9 = list(temp)

for i in range(0, 90):
    if temp[i].isdigit():
        try:
            del y2017m9[i]
        except:
            pass

for i in range(1, 51):
    y2017m9 = [w.replace('①', '1') for w in y2017m9]
    y2017m9 = [w.replace('②', '2') for w in y2017m9]
    y2017m9 = [w.replace('③', '3') for w in y2017m9]
    y2017m9 = [w.replace('④', '4') for w in y2017m9]
    y2017m9 = [w.replace('⑤', '5') for w in y2017m9]

answerSheet = list(y2017m3)
# ------------------------- 드라이버 시작
print()
print('--------------------------------')
print('--BenEdu Automative Script 1.1.0')
print('---------------Made by Angrypig7')
print('--------------------------------')
print('-----OCR works in FHD resolution')
print('requires chrome to be accessible')
print('--------------------------------')
print()


driver.get(mainUrl)

print('-----Type in your BenEdu email')
print('------------------------------')
email = str(input())
print('------------------------------')
print('----Type in your BenEdu passwd')
print('------------------------------')
passwd = str(input())
os.system('cls')

print('------------------------------')
print('Delay for each test in seconds')
print('------------------------------')

delay = int(input())
os.system('cls')
print('------------------------------')
print('------------RUNNING-----------')
print('------------------------------')

try:
    os.makedirs('./screenshots')
except:
    print('DEBUG: Screenshot folder already exists')
    print()

# 자동 로그인
while True:
    time.sleep(0.2)
    driver.find_element_by_xpath('//*[@id="liLogin"]/a').click()
    elementLogin = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="inputEmail"]')))
    driver.find_element_by_xpath('//*[@id="inputEmail"]').send_keys(email)
    driver.find_element_by_xpath('//*[@id="inputPassword"]').send_keys(passwd)
    driver.find_element_by_xpath('//*[@id="btnLogin"]').click()
    time.sleep(4)

    if driver.current_url == homeUrl:
        break
    else:
        # driver.get(mainUrl)
        # os.system('cls')
        # print()
        # print('Login info incorrect - please try again')
        # print()
        # print('-----Type in your BenEdu email')
        # print('------------------------------')
        # email = str(input())
        # print('------------------------------')
        # print('----Type in your BenEdu passwd')
        # print('------------------------------')
        # passwd = str(input())
        # os.system('cls')
        continue

# --------------------------------------------------시험지 풀기
driver.maximize_window()

driver.get(learnUrl)

while 1:
    try:
        print('DEBUG: Main Loop Started. Value = ' + str(value))

        try:
            driver.find_element_by_xpath('//*[text()[contains(.,\'TEST\')]]').click()
        except:
            print('DEBUG: Creating new testSheet')
            loop += 1
            value = 0
            createtestsheet(loop, value)
            continue

        # 응시하기
        while value <= 9:
            url1 = driver.current_url
            try:
                WebDriverWait(driver, 5).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, '//*[@id=\"Table_Boot\"]/tbody/tr[' + str(revalue) + ']/td[3]')))
                driver.find_element_by_xpath('//*[@id=\"Table_Boot\"]/tbody/tr[' + str(revalue) + ']/td[3]').click()

            except:
                value += 1
                revalue += 1
                print('DEBUG: test already completed | value = ' + str(value))
                continue

            if url1 == driver.current_url:
                revalue += 1
                continue
            else:
                value = revalue

            solveResult = solveTest(loop, value, delay)
            if solveResult:
                print('DEBUG: SOLVE ERROR')
                value += 1
                revalue = 1
                driver.get(learnUrl)
                time.sleep(0.2)
                driver.find_element_by_xpath('//*[text()[contains(.,\'TEST\')]]').click()
                continue
            elif solveResult == 0:
                print('DEBUG: SOLVE SUCCESS')
                value += 1
                print('qwer = ' + str(value))
                revalue = 1
                driver.get(learnUrl)
                time.sleep(0.2)
                driver.find_element_by_xpath('//*[text()[contains(.,\'TEST\')]]').click()
                continue

        if int(value) > 9:
            createtestsheet(loop, value)
            loop += 1
            value = 0
            print('DEBUG: tried all 9 tests. resetting')
            continue

    except:
        print('--------------------------------------------------')
        print('---------------------------DEBUG: BROAD LOOP ERROR')
        print('--------------------------------------------------')
        continue
