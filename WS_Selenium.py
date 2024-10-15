#Extracción de datos con Selenium
from selenium import webdriver
#import para inicializar nuestro WebDriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

years = [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974,
         1978, 1982, 1986, 1990, 1994, 1998, 2002, 2010, 2014,
         2018, 2022]

path = 'D:/Sam Contreras/Documents/Programacion/Python/ChromeDriver/chromedriver.exe'
servicio = Service(executable_path=path)
driver = webdriver.Chrome(service=servicio)

def obtener_data_faltante(year):
    web = f'https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup'

    driver.get(web)
    matches = driver.find_elements(By.XPATH, value='//tr[@style="font-size:90%"]')

    home = []
    score = []
    away = []

    for match in matches:
        home.append(match.find_element(By.XPATH, value='./td[1]').text)
        score.append(match.find_element(By.XPATH, value='./td[2]').text)
        away.append(match.find_element(By.XPATH, value='./td[3]').text)

    response = requests.get(web)
    content = response.text
    #Usamos BeautifulSoup para leer de mejor manera la información que obtuvimos como respuesta
    soup = BeautifulSoup(content, 'lxml')

    #Metodo 'find_all' para inspeccionar la página
    #Notamos que todos los partidos vienen en la clase 'fooballbox'
    matches = soup.find_all('div',class_='footballbox')
    #Método 'find_all' nos devuelve una lista

    for match in matches:
        home.append(match.find('th',class_='fhome').get_text())
        score.append(match.find('th',class_='fscore').get_text())
        away.append(match.find('th',class_='faway').get_text())

    dict_football = {'Home': home, 'Score': score, 'Away': away}
    df_football = pd.DataFrame(dict_football)
    df_football['Year'] = year
    time.sleep(2)
    return df_football

fifa = [obtener_data_faltante(year) for year in years]
driver.quit()
df_fifa = pd.concat(fifa,ignore_index=True)
df_fifa.to_csv('Datasets/FIFA_HISTORY_COMPLETE.csv', index=False)   
