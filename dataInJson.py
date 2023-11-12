import json
import pandas as pd

# Open the JSON file

def groupByZip(input_zip):
    with open('data.json', 'r') as file:
        data = json.load(file)  
    df= pd.DataFrame(data)
    result = df[df["zipcode"] == input_zip]
    return result.to_json('data.json')
    


    

