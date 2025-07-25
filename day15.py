#api calling using open weather
import csv
import os
import json
from datetime import datetime
import requests

file_name = "weather.csv"
API_key ="82a1984ba5032a21f38e1e3f872d5138"
city = ""

if not os.path.exists(file_name):
    with open(file_name , "a", newline= '' , encoding = "utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Date" , "City" , "Temperature" ,"Condition"])



def logging_weather():
    city = input("enter city name: ")
    date = datetime.now().strftime("%d/%m/%Y")

    with open(file_name , "r" , encoding = "utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            if row['City'].lower() == city.lower() and row['Date'] == date:
                print("Data for this city/time exists!")
                return

    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"

        response = requests.get(url) #we try to get response from the server
        data = response.json() #the response is in string format. We convert it into json

        if response.status_code != 200: #generally when there is no issues in response , it gives code as 200
            print(f"API error") # in error cases , it gives codes like 404 etc
            return
        
        temperature = data['main']['temp']
        weather = data['weather'][0]['main']

        with open(file_name , "a", newline= '' , encoding = "utf-8") as f:
            writer = csv.writer(f)

            writer.writerow([date , city , temperature , weather])
            print(f"{temperature} updated for {city} at {date}")

    except Exception as e:
        print("API call failed!")


def view_logs():
    with open(file_name , "r" , encoding = "utf-8") as f:
        reader = list(csv.reader(f))

    if len(reader)<=1: # 1 because of the heading city , temp , condition etc
        print("no entries!")

    for row in reader[1:]:
        print(f"{row[0]} -> {row[1]} -> {row[2]} -> {row[3]}")

       
def main():
    print("welcome to our weather app!")

    while True:
        print("1. add weather")
        print("2. view logs")
        print("3. exit")

        choice = int(input("enter your choice: "))


        if choice == 1:
            logging_weather()
        elif choice == 2:
            view_logs()
        elif choice == 3:
            break
        else:
            print("invalid choice!")


if __name__ == "__main__":
    main()

# add lowest , highest , average temperature

        


        



