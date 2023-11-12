import lat_long
import json
import collections
import http.client


conn = http.client.HTTPSConnection("api.iq.inrix.com")
payload = ''
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6IjVuY3J5aDA1NjUiLCJ0b2tlbiI6eyJpdiI6ImE5YTkwZWI5Nzc0YTFkNjVhYWFmMTE1MzkzOGE3NzA2IiwiY29udGVudCI6IjZlNjAxOTZhMmU4NjQxODYyMjRiMjU3NWU0OGQ2MDVkZTY5MWMxZjc0NWExMjU3YjJmNTdiYzU5OWFjODM3Njg5YWUxMjcxYzYwYWEzZDAwNjg1YzZmNTA1ZTU1Y2YzNDc1ODhkNGYwYzkzNmE0YzYxYzkxY2E2ZGMwNjVkMGFkZDgyMDc1OGY1MzJiZTdjY2EzYWNiYjg5Njk3NWQxY2ViYjQ5MmZiZjE2ODY2MDI0NWExMjJlMTg4MTcxYWRlYTJlODcxODA1MmU5NGE2MjAzYWZmMmI5Njc0YTczYjQzMWJmOTZjNzU4YWQyYTBiMGRiNmZhMzZiOTBiZDhiY2E3MjM5M2Q1MzFmYmE0ZGE3NWQ3OTY1OTA0ZGQxYTMzNzQxNjQ5ZThlZjg0MjhlMGEzNWFjZmE1YTEwZWRiMWEyZDg5NjE3ODNiMDk3NmU1OGZiYWM2ZDZmMjc2YTA1ODI3OGQzZDI5ODNiZDJmNThiZjdhNDRiMTkzZGJmODk4YjcwMGRlMGYxOTE0NWEyOTQyZjljMGEyN2ZlN2Y2MmE5ZGYyOGQ2NDIxYWRjYWMwNTIyNjJjYjk3ZTMzMzE4NmU1MGQ1MDZmMzVlOWYxODJhNDUzN2Q5NmQ2ZWE3ZDEzYzI2OGJiNTFiYjdjZGRhNGEwNGYxOGIzYzQwYTQzZjRiZGJkYTIwZmY4MTllNjE5ZGI1M2FkNDc1OTQxNGVmZDllMzQzNjUxN2RjYWU2YmQ1OGQ1Zjg5NDhmZmUzZTQyZmExZTg3Njk5ZmQwN2M5OTI5Yjg0NmIyY2Q2NDkxY2RmZjU1YzE3MmU0NGY5N2ZkY2E3MWMyZTliMzgzYTVkMTk3MTg2N2Q5YzE4MGY4MDgwZWU1MWZiIn0sInNlY3VyaXR5VG9rZW4iOnsiaXYiOiJhOWE5MGViOTc3NGExZDY1YWFhZjExNTM5MzhhNzcwNiIsImNvbnRlbnQiOiI3YjdiNjc1NTA5OTY2YmExMDA0NjE3NmRmNWEzNjEwMmZkYTFlNGZlNmRhNjFlMDMyYTc3YzcxNzlhYzgyYzU0ODZlZTE0NzYxOGJkMTYzMDM3MDY0MDZlIn0sImp0aSI6IjBhZWJhYmM3LWJmNWUtNDdjZC05YzFiLTM0ODgwODJjNTUwOCIsImlhdCI6MTY5OTc1ODE2NSwiZXhwIjoxNjk5NzYxNzY1fQ.OAkXwPGL1KsSDhtmUuJRYQNLUgjoE-isUjd0nrapvPg'
}
conn.request("GET", lat_long.OffGetCoordinates("555 Post Street"), payload, headers)
res = conn.getresponse()
data = res.read()
decoded = json.loads(data.decode('utf-8'))
# decoded_rest = json.loads(decoded["result"].decode('utf-8'))
count = decoded["count"]
hrs_available = decoded["result"][0]["hrs"][0]
print("Number of Off-Street Parkings available- ", count)
print(hrs_available)


    
