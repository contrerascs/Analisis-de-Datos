#Extracción de datos con Selenium
from selenium import webdriver
#import para inicializar nuestro WebDriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time

path = 'D:/Sam Contreras/Documents/Programacion/Python/ChromeDriver/chromedriver.exe'
servicio = Service(executable_path=path)
driver = webdriver.Chrome(service=servicio)
web = 'https://en.wikipedia.org/wiki/1990_FIFA_World_Cup'

driver.get(web)
matches = driver.find_elements(By.XPATH, value='//tr[@style="font-size:90%"]')

home = []
score = []
away = []

for match in matches:
    home.append(match.find_element(By.XPATH, value='./td[1]').text)
    score.append(match.find_element(By.XPATH, value='./td[2]').text)
    away.append(match.find_element(By.XPATH, value='./td[3]').text)

dict_football = {'home': home, 'score': score, 'away': away}
df_football = pd.DataFrame(dict_football)
df_football['Year'] = 1990
df_football_no_first = df_football.iloc[:, 1:]
time.sleep(2)
print(df_football_no_first.index[0])
#df_football_no_first.to_csv('Datasets/test_1990.csv')    
driver.quit()