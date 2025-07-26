#json to csv converter 

import json
import csv
import os

file_name = "data.json"
csv_file = "converted.csv"

def read_json(filename):
    if not os.path.exists(filename):
        print("your json file not found!")
        return []
    
    with open(filename , 'r' , encoding = "utf-8") as f:
        try:
            return json.load(f) #this reads all the content of f and converts it into json format
        
        except: #if the data in the json file is not in the json format
            print("invalid JSON format")


def converter_csv(data , output):
    if not data:
        print("no data to convert")
        return
    
    key_names = list(data[0].keys())

    with open(output, "w" , newline = "" , encoding = "utf-8") as f:
        writer = csv.DictWriter(f , fieldnames=key_names)
        writer.writeheader()

        for record in data:
            writer.writerow(record)

    print(f"converted {len(data)} items to {output}")

    return output


def main():
    print("this is a json to csv converter")

    data = read_json(file_name)
    converter_csv(data , csv_file)

if __name__ == "__main__":
    main()


            
