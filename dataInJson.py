import json
import pandas as pd
# Open the JSON file
with open('addys.json', 'r') as file:
    data = json.load(file)  # Read the JSON data

# Now 'data' contains the contents of the JSON file
# You can access the JSON elements like a Python dictionary
df= pd.DataFrame(data)
df['zipcode'] = "94102"
del df['id']

print(df)

df.to_json('data.json')

