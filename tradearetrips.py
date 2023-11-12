import http.client
import lat_long
import json
import collections
import pandas as pd

conn = http.client.HTTPSConnection("api.iq.inrix.com")
payload = ''
headers = {
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6IjVuY3J5aDA1NjUiLCJ0b2tlbiI6eyJpdiI6ImE5YTkwZWI5Nzc0YTFkNjVhYWFmMTE1MzkzOGE3NzA2IiwiY29udGVudCI6IjZlNjAxOTZhMmU4NjQxODYyMjRiMjU3NWU0OGQ2MDVkZTY5MWMxZjc0NWExMjU3YjJmNTdiYzU5OWFjODM3Njg5YWUxMjcxYzYwYWEzZDAwNjg1YzZmNTA1ZTU1Y2YzNDc1ODhkNGYwYzkzNmE0YzYxYzkxY2E2ZGMwNjVkMGFkZDgyMDc1OGY1MzJiZTdjY2EzYWNiYjg5Njk3NWQxY2ViYjQ5MmZiZjE2ODY2MDI0NWExMjJlMTg4MTcxYWRlYTJlODcxODA1MmU5NGE2MjAzYWZmMmI5Njc0YTczYjQzMWJmOTZjNzU4YWQyYTBiMGRiNmZhMzZiOTBiZDhiY2E3MjM5M2Q1MzFmYmE0ZGE3NWQ3OTY1OTA0ZGQxYTMzNzQxNjQ5ZThlZjg0MmEwMjQzNWFjZWE2YzEwZWVhMWI2OTI5NTM5ODdmYjk2N2U1OGZiYWM2ZDZmMjc2YTA1ODI3OGQzZDI5ODNiZDJmNThiZjdhNDRiMTE3NGJjOTliZDcwMGRlMGYxOTE0NWEyOTQyZjljMGEyN2ZlN2Y2MmE5ZGYyOGQ2NDIxYWRjYWMwNTIyNjJjYjk3ZTMzMzE4NmU1MGQ1MDZmMzVlOWYxODJhNDUzN2Q5NmQ2ZWE3ZDEzYzI2OGJiNTFiYjdjZGRhNGEwNGYxOGIzYzQwYTQzZjRiZGJkYTIwZmY4MTllNjE5ZGI1M2FkNDc1OTQxNGVmZDllMzQzNjUxN2RjYWU2YmQ1OGQ1Zjg5NDhmZmUzZTQyZjhjZTE3MWI0ZDMyN2RiYjM4MmJlNzMyOThlNGMxNmFhZmUzOTI3MmY2ZWJlNjVlOGIzMGI1Y2FmMWExZjY5MWI0Nzk0NTg5MDJlMjVkY2ZiZTI0OWViIn0sInNlY3VyaXR5VG9rZW4iOnsiaXYiOiJhOWE5MGViOTc3NGExZDY1YWFhZjExNTM5MzhhNzcwNiIsImNvbnRlbnQiOiI1OTc0Mzg2NzA4YjA1NDg1M2Q3NDFmN2JmYzllNjcwNWUzY2RiOWJkN2ZmYTMwMDMyMTY2YmU1ZmUxZWEyYzdjOTlkMjM5NjkyMTgyMmUxZjQzMDc3NjZlIn0sImp0aSI6IjNiODIwODFhLWVjYmEtNDZkMi04NWJjLWFlY2Y2ZDk0MTU3NiIsImlhdCI6MTY5OTc1OTczNywiZXhwIjoxNjk5NzYzMzM3fQ.mD5ZIEj6xhM6F9G1oB1SXMnrBpcw0BYQHG3w9keBdRI\''
}
conn.request("GET", "/v1/trips-count?od=origin&geoFilterType=polygon&points=37.734622%7C-122.471603%2C37.743627%7C-122.463850%2C37.743066%7C-122.475429&limit=100&startDateTime=%3E%3D2023-06-01T02%3A31&endDateTime=%3C%3D2023-06-15T02%3A31", payload, headers)
res = conn.getresponse()
data = res.read()

decoded = json.loads(data.decode('utf-8'))

print(decoded)
