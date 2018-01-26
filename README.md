## 베네듀 자동화 스크립트


#### TDL
	> PyQT활용하여 GUI로 구성하기
	> 선택적으로 암호화하여 계정 및 설정 저장하기
	> 캡차 이미지를 캡처하는 대신 다운로드 이후 배경 채우기를 통해 OCR 인식하기


#### info
	> PyInstaller로 EXE추출 가능
	> Exe추출시 PyTesseract모듈과 chromedriver.exe는 직접 추가해줘야함
	> chrome 버전이 업데이트될때마다 chromedriver.exe도 업데이트 해줘야함

Python을 기반으로 하는 베네듀 자동화 스크립트입니다.
Selenium Webdriver, BeautifulSoup를 사용하며 OCR인식에는 PyTesseract가 사용되었습니다.


EXE로 추출하려 했으나, OCR인식에 사용되는 PyTesseract부분이 정상작동하지 않아 수정할 계획입니다.

## Benedu automation script
Benedu-automated is based on Python along with Selenium Webdriver, BeautifulSoup and PyTesseract for OCR initialization.
