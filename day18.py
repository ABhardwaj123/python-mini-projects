#json to csv converter

import os
import csv
import json

csv_file = "csv_to_json.csv"
json_file = "converted.json"

def load_csv(filename):
    if not os.path.exists(filename):
        print("your csv file not found!")
        return []
    
    with open(filename , 'r' ,encoding ="utf-8") as f:
        reader = csv.DictReader(f)
        data = list(reader)
        return data
    
def convert_to_json(data , filename):
    if not data:
        print("no data in your json file!")

    with open(filename , 'w' , encoding = "utf-8") as f:
        json.dump(data , f , indent = 5)

    print(f"converted {len(data)} records to json format")

    return filename

def display_data(data ):
    for row in data:
        json.dumps(row , indent = 2) #json.dumps(row) converts row to json format with 2 spaces(indent = 2)
        
    print()
    
def main():

    data = load_csv(csv_file)

    if not data:
        return
    
    convert_to_json(data , json_file)

    display_data(json_file)

if __name__ == "__main__":
    main()

