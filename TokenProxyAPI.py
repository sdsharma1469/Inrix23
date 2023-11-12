from flask import Flask, jsonify
import requests

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# to query, call: http://localhost:8000/gettoken
@app.route('/gettoken')
def get_token():
    # Set up URL to query
    app_id = "5ncryh0565"
    hash_token = "NW5jcnloMDU2NXxFUG10d1NEVGJwNHhCSzJWQjdqMlk1NGhoRFhjYjRaUDVwTkcxUXJY"
    url = f"https://api.iq.inrix.com/auth/v1/appToken?appId={app_id}&hashToken={hash_token}"

    # Set up query method
    request_options = {
        'method': 'GET',
    }

    try:
        # Query INRIX for token
        response = requests.get(url, **request_options)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the JSON response
        json_data = response.json()
        output = json_data['result']['token']

        # Return token
        print("token is ", output)
        return jsonify(token=output)

    except requests.exceptions.RequestException as e:
        # Handle request errors
        return jsonify(error=str(e)), 5000
    


# Starting server using the run function
if __name__ == '__main__':
    port = 8000
    app.run(port=port)