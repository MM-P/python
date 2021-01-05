'''
Napisz program, który po uruchomieniu wyświetla w czytelnej formie aktualną datę, godzinę, dzień tygodnia i pogodę/temperaturę/ciśnienie 
w zadanym mieście (wykorzystaj np. https://rapidapi.com/commu.../api/open-weather-map/endpoints - pamiętaj o poprawnym przeliczeniu jednostek 
np. temperatura z kelwinów na stopnie) oraz losowy cytat (np. https://type.fit/api/quotes ). Wykorzystaj requests i datetime.
Propozycja rozszerzenia: Wyświetl również bieżący czas dla miast w różnych strefach czasowych (np. Pekin, Sydney, Waszyngton, Londyn) - 
wykorzystaj np. pytz: https://pypi.org/project/pytz/ oraz wyświetl listę osób obchodzących imieniny 
(poszukaj otwartej bazy danych lub wykorzystaj prosty web scrapping np. z wykorzystaniem: https://imienniczek.pl/widget/js ).
'''


import requests
from datetime import datetime
from pytz import timezone
from  random import choice
from requests import get, request
import json
from bs4 import BeautifulSoup

print('Pogoda dla Warszawy\n\n')

url = "https://community-open-weather-map.p.rapidapi.com/weather"
querystring = {"q":"Warsaw,PL","lat":"0","lon":"0","id":"2172797","lang":"pl","units":"metric","mode":"xml, html"}

headers = {
    'x-rapidapi-key': "d54032fa0fmshffcd544c83a88c4p1d6440jsn7885f41a7f31",
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
    }

response = request("GET", url, headers=headers, params=querystring).json()

if response['name'] == 'Warszawa':
    print("Pogoda: {}".format(response["weather"][0]['description']))
    print("Temperatura: {:.2f} C".format(response["main"]["temp"]))
    print("Ciśnienie: {} hPa".format(response["main"]["pressure"]))
    print("Wilgotność: {} %".format(response["main"]["humidity"]))
    print("Wiatr: {} km/h".format(response["wind"]["speed"]))
    
time_global = '%d-%m-%Y %H:%M:%S'
print("\nPekin: {}".format(datetime.now(timezone("Asia/Shanghai")).strftime(time_global)))
print("Sydney: {}".format(datetime.now(timezone("Australia/Sydney")).strftime(time_global)))
print("London: {}".format(datetime.now(timezone("Europe/London")).strftime(time_global)))
 
response = request("GET", "https://imienniczek.pl/widget/js")
soup = BeautifulSoup(response.text, "html.parser")
print("")
for name_day in soup.find_all("span"):
    print(name_day.text)
    
cytat = get('https://type.fit/api/quotes')
if cytat.status_code == 200:
    random_quote = choice(json.loads(cytat.content))
    print(f'\n\"Cytat na dzis: {random_quote["text"]}\"\nAutor: {random_quote["author"]}')
else:
    print('bład pobierania cytatu')
    
