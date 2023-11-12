from flask import Flask, jsonify
import requests
import lat_long
import json
import http.client

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route('/gettoken')
def get_token():
    app_id = "5ncryh0565"
    hash_token = "NW5jcnloMDU2NXxFUG10d1NEVGJwNHhCSzJWQjdqMlk1NGhoRFhjYjRaUDVwTkcxUXJY"
    url = f"https://api.iq.inrix.com/auth/v1/appToken?appId={app_id}&hashToken={hash_token}"
    try:
        # Provide method directly as an argument, not in request_options
        response = requests.get(url)
        response.raise_for_status()
        json_data = response.json()
        output = json_data['result']['token']
        print("token", output)
        return jsonify(token=output)

    except requests.exceptions.RequestException as e:
        return jsonify(error=str(e)), 500

    except requests.exceptions.RequestException as e:
        return jsonify(error=str(e)), 500

@app.route('/getOffStreetParking')
def getOffStreetParking():
    try:
        conn = http.client.HTTPSConnection("api.iq.inrix.com")
        payload = ''
        headers = {
            'accept': 'application/json',
            'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6IjVuY3J5aDA1NjUiLCJ0b2tlbiI6eyJpdiI6ImE5YTkwZWI5Nzc0YTFkNjVhYWFmMTE1MzkzOGE3NzA2IiwiY29udGVudCI6IjZlNjAxOTZhMmU4NjQxODYyMjRiMjU3NWU0OGQ2MDVkZTY5MWMxZjc0NWExMjU3YjJmNTdiYzU5OWFjODM3Njg5YWUxMjcxYzYwYWEzZDAwNjg1YzZmNTA1ZTU1Y2YzNDc1ODhkNGYwYzkzNmE0YzYxYzkxY2E2ZGMwNjVkMGFkZDgyMDc1OGY1MzJiZTdjY2EzYWNiYjg5Njk3NWQxY2ViYjQ5MmZiZjE2ODY2MDI0NWExMjJlMTg4MTcxYWRlYTJlODcxODA1MmU5NGE2MjAzYWZmMmI5Njc0YTczYjQzMWJmOTZjNzU4YWQyYTBiMGRiNmZhMzZiOTBiZDhiY2E3MjM5M2Q1MzFmYmE0ZGE3NWQ3OTY1OTA0ZGQxYTMzNzQxNjQ5ZThlZjg0MjhlMGEzNWFjZmE1YTEwZWRiMWEyZDg5NjE3ODNiMDk3NmU1OGZiYWM2ZDZmMjc2YTA1ODI3OGQzZDI5ODNiZDJmNThiZjdhNDRiMTkzZGJmODk4YjcwMGRlMGYxOTE0NWEyOTQyZjljMGEyN2ZlN2Y2MmE5ZGYyOGQ2NDIxYWRjYWMwNTIyNjJjYjk3ZTMzMzE4NmU1MGQ1MDZmMzVlOWYxODJhNDUzN2Q5NmQ2ZWE3ZDEzYzI2OGJiNTFiYjdjZGRhNGEwNGYxOGIzYzQwYTQzZjRiZGJkYTIwZmY4MTllNjE5ZGI1M2FkNDc1OTQxNGVmZDllMzQzNjUxN2RjYWU2YmQ1OGQ1Zjg5NDhmZmUzZTQyZmExZTg3Njk5ZmQwN2M5OTI5Yjg0NmIyY2Q2NDkxY2RmZjU1YzE3MmU0NGY5N2ZkY2E3MWMyZTliMzgzYTVkMTk3MTg2N2Q5YzE4MGY4MDgwZWU1MWZiIn0sInNlY3VyaXR5VG9rZW4iOnsiaXYiOiJhOWE5MGViOTc3NGExZDY1YWFhZjExNTM5MzhhNzcwNiIsImNvbnRlbnQiOiI3YjdiNjc1NTA5OTY2YmExMDA0NjE3NmRmNWEzNjEwMmZkYTFlNGZlNmRhNjFlMDMyYTc3YzcxNzlhYzgyYzU0ODZlZTE0NzYxOGJkMTYzMDM3MDY0MDZlIn0sImp0aSI6IjBhZWJhYmM3LWJmNWUtNDdjZC05YzFiLTM0ODgwODJjNTUwOCIsImlhdCI6MTY5OTc1ODE2NSwiZXhwIjoxNjk5NzYxNzY1fQ.OAkXwPGL1KsSDhtmUuJRYQNLUgjoE-isUjd0nrapvPg'  # Replace with your actual access token
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
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6IjVuY3J5aDA1NjUiLCJ0b2tlbiI6eyJpdiI6ImE5YTkwZWI5Nzc0YTFkNjVhYWFmMTE1MzkzOGE3NzA2IiwiY29udGVudCI6IjZlNjAxOTZhMmU4NjQxODYyMjRiMjU3NWU0OGQ2MDVkZTY5MWMxZjc0NWExMjU3YjJmNTdiYzU5OWFjODM3Njg5YWUxMjcxYzYwYWEzZDAwNjg1YzZmNTA1ZTU1Y2YzNDc1ODhkNGYwYzkzNmE0YzYxYzkxY2E2ZGMwNjVkMGFkZDgyMDc1OGY1MzJiZTdjY2EzYWNiYjg5Njk3NWQxY2ViYjQ5MmZiZjE2ODY2MDI0NWExMjJlMTg4MTcxYWRlYTJlODcxODA1MmU5NGE2MjAzYWZmMmI5Njc0YTczYjQzMWJmOTZjNzU4YWQyYTBiMGRiNmZhMzZiOTBiZDhiY2E3MjM5M2Q1MzFmYmE0ZGE3NWQ3OTY1OTA0ZGQxYTMzNzQxNjQ5ZThlZjg0MjhlMGEzNWFjZmE1YTEwZWRiMWEyZDg5NjE3ODNiMDk3NmU1OGZiYWM2ZDZmMjc2YTA1ODI3OGQzZDI5ODNiZDJmNThiZjdhNDRiMTkzZGJmODk4YjcwMGRlMGYxOTE0NWEyOTQyZjljMGEyN2ZlN2Y2MmE5ZGYyOGQ2NDIxYWRjYWMwNTIyNjJjYjk3ZTMzMzE4NmU1MGQ1MDZmMzVlOWYxODJhNDUzN2Q5NmQ2ZWE3ZDEzYzI2OGJiNTFiYjdjZGRhNGEwNGYxOGIzYzQwYTQzZjRiZGJkYTIwZmY4MTllNjE5ZGI1M2FkNDc1OTQxNGVmZDllMzQzNjUxN2RjYWU2YmQ1OGQ1Zjg5NDhmZmUzZTQyZmExZTg3Njk5ZmQwN2M5OTI5Yjg0NmIyY2Q2NDkxY2RmZjU1YzE3MmU0NGY5N2ZkY2E3MWMyZTliMzgzYTVkMTk3MTg2N2Q5YzE4MGY4MDgwZWU1MWZiIn0sInNlY3VyaXR5VG9rZW4iOnsiaXYiOiJhOWE5MGViOTc3NGExZDY1YWFhZjExNTM5MzhhNzcwNiIsImNvbnRlbnQiOiI3YjdiNjc1NTA5OTY2YmExMDA0NjE3NmRmNWEzNjEwMmZkYTFlNGZlNmRhNjFlMDMyYTc3YzcxNzlhYzgyYzU0ODZlZTE0NzYxOGJkMTYzMDM3MDY0MDZlIn0sImp0aSI6IjBhZWJhYmM3LWJmNWUtNDdjZC05YzFiLTM0ODgwODJjNTUwOCIsImlhdCI6MTY5OTc1ODE2NSwiZXhwIjoxNjk5NzYxNzY1fQ.OAkXwPGL1KsSDhtmUuJRYQNLUgjoE-isUjd0nrapvPg'
    }
    conn.request("GET", "/v1/trips-count?od=origin&geoFilterType=polygon&points=37.734622%7C-122.471603%2C37.743627%7C-122.463850%2C37.743066%7C-122.475429&limit=100&startDateTime=%3E%3D2023-06-01T02%3A31&endDateTime=%3C%3D2023-06-15T02%3A31", payload, headers)
    res = conn.getresponse()
    data = res.read()
    return(data.decode("utf-8"))

# Starting server using the run function
if __name__ == '__main__':
    port = 8000
    app.run(port=port, debug=True)
