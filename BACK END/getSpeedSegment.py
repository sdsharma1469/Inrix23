import http.client
import lat_long
import json
import collections
import pandas as pd
import TokenProxyAPI

conn = http.client.HTTPSConnection("api.iq.inrix.com")
payload = ''
headers = {
'Authorization': 'Bearer ' +TokenProxyAPI.get_token()
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


