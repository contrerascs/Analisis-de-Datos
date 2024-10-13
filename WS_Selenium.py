#Extracción de datos con Selenium
from selenium import webdriver
#import para inicializar nuestro WebDriver
from selenium.webdriver.chrome.service import Service
import time

path = 'D:/Sam Contreras/Documents/Programacion/Python/ChromeDriver/chromedriver.exe'
servicio = Service(executable_path=path)
driver = webdriver.Chrome(service=servicio)
web = 'https://en.wikipedia.org/wiki/1982_FIFA_World_Cup'

driver.get(web)
matches = driver.find_elements(by='xpath', value='//td[@align="right"]/..')
time.sleep(10)
