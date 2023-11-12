from flask import Flask, jsonify
import requests
import lat_long
import json
import http.client
import pandas as pd


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route('/gettoken')
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
    

@app.route('/getOffStreetParking')
def getOffStreetParking():
    token_x = get_token()
    try:
        conn = http.client.HTTPSConnection("api.iq.inrix.com")
        payload = ''
        headers = {
            'accept': 'application/json',
            'Authorization': "Bearer "+token_x
        }
        address = "555 Post Street"
        url = lat_long.OffGetCoordinates(address)
        
        conn.request("GET", url, payload, headers)
        res = conn.getresponse()
        data = res.read()
        decoded = json.loads(data.decode('utf-8'))
        count = decoded.get("count")
        hrs_available = decoded.get("result", [])[0].get("hrs", [])[0]

        print("Number of Off-Street Parkings available:", count)
        print("Hours available:", hrs_available)

        return jsonify(count=count, hrs_available=hrs_available)

    except Exception as e:
        return jsonify(error=str(e)), 500

@app.route('/TradeAreaTrips')
def TradeAreaTrips():  
    conn = http.client.HTTPSConnection("api.iq.inrix.com")
    payload = ''
    headers = {
    'Authorization': "Bearer "+get_token()
    }
    conn.request("GET", "/v1/trips-count?od=origin&geoFilterType=polygon&points=37.734622%7C-122.471603%2C37.743627%7C-122.463850%2C37.743066%7C-122.475429&limit=100&startDateTime=%3E%3D2023-06-01T02%3A31&endDateTime=%3C%3D2023-06-15T02%3A31", payload, headers)
    res = conn.getresponse()
    data = res.read()
    return(data.decode("utf-8"))

@app.route('/getSeg')
def getSeg():
    conn = http.client.HTTPSConnection("api.iq.inrix.com")
    payload = ''
    headers = {
    'Authorization': "Bearer "+get_token()
    }
    conn.request("GET", "/v1/segments/speed?point=37.7878202%7C-122.4109003&radius=10&SpeedOutputFields=average, speedbucket&Duration=10&StartTime=2023-11-12T04:43:20.084Z", payload, headers)
    res = conn.getresponse()
    data = res.read()

    decoded = json.loads(data.decode('utf-8'))

    df = pd.DataFrame(decoded)

    df= df["result"]["segmentspeeds"][0]["segments"]
    df = pd.DataFrame(df)
    df.set_index('average', inplace=True)
    del df['code']
    del df['type']
    del df['segmentClosed']

    print(df.head())
    return df.head()

@app.route('/getOnStreet')
def getOnStreet():
    token_x = get_token()
    try:
        conn = http.client.HTTPSConnection("api.iq.inrix.com")
        payload = ''
        headers = {
            'accept': 'application/json',
            'Authorization': "Bearer "+token_x
        }
        address = "555 Post Street"
        url = lat_long.OnGetCoordinates(address)
        
        conn.request("GET", url, payload, headers)
        res = conn.getresponse()
        data = res.read()
        decoded = json.loads(data.decode('utf-8'))
        count = decoded.get("count")
        hrs_available = decoded.get("result", [])[0].get("hrs", [])[0]

        df = pd.DataFrame(decoded)
        print(df.keys())
        length = len(df["result"])
        count = 0
        print(df.keys())
        print(df["MeterCount"])
        while count<length: 
            if(df["result"][count]["probability"] == None): 
                count = count+1
            else:
                print(df["result"][count]["name"] + " Probability to Find Parking: ", df["result"][count]["probability"], "%", "Meter Count:", df["MeterCount"][count])
            
            count = count +1

        return jsonify(count=count, hrs_available=hrs_available)

    except Exception as e:
        return jsonify(error=str(e)), 500
    

# Starting server using the run function
if __name__ == '__main__':
    port = 8000
    app.run(port=port, debug=True)


