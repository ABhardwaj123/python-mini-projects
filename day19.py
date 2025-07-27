#flattening json file

import json
import os

file_name = "nested_data.json"
output_file = "flattened_json.josn"

def flatten_json(data, parent_key = '', seperator = '.'): #because its a nested dict , we can have multiple parent keys
    #seperator is used here to seperate different parent keys
    items = {}

    if isinstance(data , dict): # if data is in dict form
        for key , value in data.items():
            full_key = f"{parent_key}{seperator}{key}" if parent_key else key
            # print(full_key)
            items.update(flatten_json(value, full_key , seperator=seperator)) #passing data as value because it can be nested
            #passing parent_key as full_key because it can be nested and will get called until last point(recursion)


    elif isinstance(data , list): # if data is in list form
        for idx, item in enumerate(data):
            full_key = f"{parent_key}{seperator}{idx}" if parent_key else str(idx)
            items.update(flatten_json(item, full_key ,seperator=seperator))
    else: #if data is a normal key value pair
        items[parent_key] = data

    return items

def main():
    if not os.path.exists(file_name):
        print("input file not found!")

    try:
        with open(file_name , 'r' , encoding = "utf-8") as f:
            data = json.load(f)

        seperator = input("enter your seperator{; , -> .}: ").strip() or '.'

        flattened_data =flatten_json(data ,seperator=seperator)

        with open(output_file , 'w', encoding = "utf-8") as f:
            json.dump(flattened_data , f , indent = 2) # putting it in the file

    except Exception as e:
        print("failed to flatten the data!")

if __name__ == "__main__":
    main()