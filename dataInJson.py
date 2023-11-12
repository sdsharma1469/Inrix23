from flask import Flask, jsonify, request
import requests
import lat_long
import json
import http.client
import pandas as pd
import time
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app)

CORS(app, resources={r"/getOffStreetParking": {"origins": "http://localhost:8000"}})
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route('/gettoken')
@cross_origin()
def get_token():
    app_id = "5ncryh0565"
    hash_token = "NW5jcnloMDU2NXxFUG10d1NEVGJwNHhCSzJWQjdqMlk1NGhoRFhjYjRaUDVwTkcxUXJY"
    url = f"https://api.iq.inrix.com/auth/v1/appToken?appId={app_id}&hashToken={hash_token}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        json_data = response.json()
        token = json_data['result']['token']
        print("token", token)
        return token

    except requests.exceptions.RequestException as e:
        return jsonify(error=str(e)), 500

# Open the JSON file

import http.client
from datetime import datetime, timedelta


def TradeAreaTrips(address):
    location = lat_long.OffGetCoordinates(address)
    print(location)
    conn = http.client.HTTPSConnection("api.iq.inrix.com")
    payload = ''
    headers = {
            'accept': 'application/json',
            'Authorization': "Bearer "+str(get_token()),
            'Access-Control-Allow-Origin': 'http://127.0.0.1:9000',
            'Access-Control-Allow-Credentials': 'true'
        }
    input_string = location

    start_index = input_string.find('=') + 1
    end_index = input_string.find('&')

    coordinates = input_string[start_index:end_index]
    
    conn.request("GET", "/v1/trips-count?od=destination&geoFilterType=circle&radius=0.2km&points="+coordinates+"&limit=100&startDateTime=%3E%3D2023-06-01T02%3A31&endDateTime=%3C%3D2023-06-15T02%3A31", payload, headers)
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    return data

def getOffStreetParking(address):
    token_x = get_token()
    try:
        conn = http.client.HTTPSConnection("api.iq.inrix.com")
        payload = ''
        headers = {
            'accept': 'application/json',
            'Authorization': "Bearer "+token_x,
            'Access-Control-Allow-Origin': 'http://127.0.0.1:9000',
            'Access-Control-Allow-Credentials': 'true'
        }

        url = lat_long.OffGetCoordinates(address)
        
        conn.request("GET", url, payload, headers)
        res = conn.getresponse()
        data = res.read()
        decoded = json.loads(data.decode('utf-8'))
        count = decoded.get("count")
        hrs_available = decoded.get("result", [])[0].get("hrs", [])[0]

        # print("Number of Off-Street Parkings available:", count)

        return str(count)
    except Exception as e:
        return jsonify(error=str(e)), 500
    
@app.route('/GroupByZip', methods=['GET'])
@cross_origin()
def groupByZip():
    list1=[]
    list2=[]
    with open('data.json', 'r') as file:
        data = json.load(file)  
    df = pd.DataFrame(data)
    for value in df['address']:
        list1.append(TradeAreaTrips(value))
        list2.append(getOffStreetParking(value))
        print (TradeAreaTrips(value))

    df['OffStreet']=list1
    df['TradeTrips']=list2

  
    df.to_json('test_data.json', orient='records', default_handler=str)

    json_file_path = 'test_data.json'

    with open(json_file_path, 'r') as file:
        json_content = json.load(file)

    formatted_json = json.dumps(json_content, indent=2)
    with open(json_file_path, 'w') as output_file:
        output_file.write(formatted_json)
    return json_file_path
    

if __name__ == '__main__':
    app.run(port=8000, debug=True)
    

