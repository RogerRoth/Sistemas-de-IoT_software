#http://rogerroth.pythonanywhere.com/
#http://rogerroth.pythonanywhere.com/ws
#https://rogerroth.pythonanywhere.com/find?condition=temperature>20

from flask import Flask, request, make_response, jsonify
import json
import sqlite3

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Weather report API'

@app.route('/ws', methods=["GET", "POST"])
def ws():
    if request.method == "POST":
        requestData = request.get_json()

        temperature = None
        humidity = None
        dewpoint = None
        pressure = None
        speed = None
        direction = None
        datetime = None

        if requestData:
            if 'temperature' in requestData:
                temperature = requestData['temperature']
            if 'humidity' in requestData:
                humidity = requestData['humidity']
            if 'dewpoint' in requestData:
                dewpoint = requestData['dewpoint']
            if 'pressure' in requestData:
                pressure = requestData['pressure']
            if 'speed' in requestData:
                speed = requestData['speed']
            if 'direction' in requestData:
                direction = requestData['direction']
            if 'datetime' in requestData:
                datetime = requestData['datetime']

            insertData(temperature,humidity,dewpoint,pressure,speed,direction,datetime)

            return make_response(jsonify({"message": "Dados inseridos com sucesso"}), 200)

        else:
            return make_response(jsonify({"error": "Request body must be JSON"}), 400)

    elif request.method == "GET":
        if request.args.get('all') == "true":
            return selectAll()

@app.route('/find', methods=["GET"])
def find():
    condition = request.args.get('condition')

    data = selectByFilter(condition)

    return make_response(data, 200)

def connectDB():
    dbFile = '/home/RogerRoth/mysite/weatherData.db'
    dataBaseConnection = sqlite3.connect(dbFile)
    cursor = dataBaseConnection.cursor()

    return dataBaseConnection, cursor

def selectAll():
    [dataBaseConnection, cursor] = connectDB()

    cursor.execute("SELECT * FROM weather")
    response = cursor.fetchall()

    cursor.close()
    dataBaseConnection.close()
    return processData(response)

def selectByFilter(condition):
    [dataBaseConnection, cursor] = connectDB()

    sql = "SELECT * FROM weather WHERE " + condition

    cursor.execute(sql)
    response = cursor.fetchall()

    data = processData(response)

    cursor.close()
    dataBaseConnection.close()
    return data


def insertData(temperature,humidity,dewpoint,pressure,speed,direction,datetime):
    [dataBaseConnection, cursor] = connectDB()

    cursor.execute("INSERT INTO weather VALUES (?, ?, ?, ?, ?, ?, ?)", (float(temperature), float(humidity), float(dewpoint), float(pressure), float(speed), direction, datetime))
    dataBaseConnection.commit()

    cursor.close()
    dataBaseConnection.close()

def processData(data):
    items = []

    for row in data:
        items.append({'temperature': row[0],'humidity': row[1],'dewpoint': row[2],'pressure': row[3],'speed': row[4],'direction': row[5],'datetime': row[6]})

    return json.dumps({'weather': items})