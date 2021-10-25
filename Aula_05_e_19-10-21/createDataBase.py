import json
import sqlite3
from urllib.request import urlopen


def readDataFrom(url):
    response = urlopen(url)
    data = json.loads(response.read())
    return data


def createDB():
    dataBase = sqlite3.connect('weatherData.db')
    cursor = dataBase.cursor()

    cursor.execute('CREATE TABLE weather (temperature real, humidity real, dewpoint real, pressure real, speed real, direction text, datetime text)')
    cursor.close
    dataBase.close()


def insertData(data):

    dataBase = sqlite3.connect('weatherData.db')
    cursor = dataBase.cursor()

    for item in data:
        cursor.execute("INSERT INTO weather VALUES (?, ?, ?, ?, ?, ?, ?)", (float(item['temperature']), float(item['humidity']), float(item['dewpoint']), float(item['pressure']), float(item['speed']), item['direction'], item['datetime']))
        dataBase.commit()
        
    cursor.close()
    dataBase.close()

    print('Registros inseridos com sucesso!')

    
data = readDataFrom('http://ghelfer.net/la/weather.json')
createDB()
insertData(data['weather'])
