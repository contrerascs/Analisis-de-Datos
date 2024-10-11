#Extracción de datos con Selenium
from selenium import webdriver
#import para inicializar nuestro WebDriver
from selenium.webdriver.chrome.service import Service

path = 'Sam Contreras/Documents/Programacion/Python/ChromeDriver'
servicio = Service(executable_path=path)
driver = webdriver.Chrome(service=servicio)
web = 'https://en.wikipedia.org/wiki/1982_FIFA_World_Cup'

driver.get(web)
