import lat_long
import json
import collections
import pandas as pd


import http.client

conn = http.client.HTTPSConnection("api.iq.inrix.com")
payload = ''
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6IjVuY3J5aDA1NjUiLCJ0b2tlbiI6eyJpdiI6IjVmNjhiNzhlNGRhNWZhY2JiYmE2NjUxYWZkNzFhZjgzIiwiY29udGVudCI6IjFmM2UwZWFlNTQ3M2QyMWZhYTM5OGEwMWRlZmQ1MmU2YzBjNTBiODI2NzE3NmE2ZDg5NzU5M2Q5ZmQ2MDVkYTFjNWQzMTViZGE3YzcyOTRkZmZiZDdlMWFiZTY1NjkxMTJmNWE1YzNjZTdlYjQ4NDRiMTk4YWU0MTQ1NjkwMWRiY2MwMjk3NzBjZmJlMjcxMGJhYTNhOWI1MzY4MjRjY2RkYWZiOTc4ZTViYTJjOGU3ZGEwODRkMDUyOGJmYmVmYjcxOWJlNTUxODNkZTg4YmVjYmJmNTVkNmM2OWFmOGI1NmZkZDBlMmRjNWVmNWEwMzFkNTViOTYxMzdhODE3ODVkODRmMWU0MDdiNDY0Y2Y3MzhiYmYxNDcyOTgxMTU0ZTkzNTlmN2FlYTNkZmQxZThlM2VkOTIzNjlmM2FiZTIwZDdmODEwMWRjZThmNzFhNGUyY2E1NjQwYzZjMGU1NDczMDk2YWFkZmNkODBjMDg5ZTgwZDdkYjYwYzUwZjdkZTZjYjc5YmQwYzUzNDM1NTkwMTk1YzljNzRiN2VjNmU5MmY5NjY3ZjVjM2FmZDgxNjRlODcwNTI2NTFjMjM3ZDQ3YTBiZDlmYmM4NmU3ZmMzYTJiZGY0YTBhZDYxNTAzZTQ5YWQ0MTUyZWIyNjJhYmU3ZmM0NWI4YTQwZjVkMjFhM2QyNGFmYTc5NDU5OGQ5MGMyYTlhYjMzNzEzZWZiMzYzNmVmNzNlOTYwODM4YzgzY2IxMGNjYmM1Y2NlY2M1OWIwMDAyNjIwZmUxY2IwY2QzMzhkZDNiYzQyZTE2NGUwMWYxZWY5OWZmNjM1Yjc3MmJiNjFhZTEwOWI2MTEwYWQzM2YyODhlZDk3YThlNmUyNDdjZmY0In0sInNlY3VyaXR5VG9rZW4iOnsiaXYiOiI1ZjY4Yjc4ZTRkYTVmYWNiYmJhNjY1MWFmZDcxYWY4MyIsImNvbnRlbnQiOiI0ZTE2MzdiYzRlNjc4MzI0YTAwNTgxMGFlZmQ0NWQ5YmMwZDgxMGMwNmMzNTczM2Y5MzVmYmQ4MWMxMjY2NmIzYzZkNzcyY2VjZmQ1MTk2NWY0ZWEwZTI0In0sImp0aSI6ImJkNGI0MzRjLTEzZGItNDY1ZS05ZTA4LTA3ZjJkZTE2MzZjOSIsImlhdCI6MTY5OTc0NzEyMCwiZXhwIjoxNjk5NzUwNzIwfQ.lE3zNU1-wRr4cev-MAwKPUyYgzPbzL9aZFszSbSdQws\''
}
conn.request("GET", "/blocks/v3?point=37.7878202%7C-122.4109003&radius=500", payload, headers)
res = conn.getresponse()
data = res.read()
decoded = json.loads(data.decode('utf-8'))
# decoded_rest = json.loads(decoded["result"].decode('utf-8'))
# count = decoded["count"]
# hrs_available = decoded["result"][0]["hrs"][0]
# print("Number of On-Street Parkings available- ", count)
# print(hrs_available)
df = pd.DataFrame(decoded)
length = len(df["result"])
count = 0
while count<length: 
    if(df["result"][count]["probability"] == None): 
        count = count+1
    else:
        print(df["result"][count]["name"] + " Probability to Find Parking: ", df["result"][count]["probability"], "%")
    
    count = count +1

