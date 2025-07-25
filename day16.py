#graphs using matplotlib

import csv
import matplotlib.pyplot as plt
from collections import defaultdict

file_name = "city_weather.csv"

def plot_weather():
    dates = []
    temps = []

    with open(file_name , "r" , encoding = "utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            try:
                dates.append(row['Date'])
                temps.append(row['Temperature'])
            except:
                continue

        if not dates:
            print("no data found!")
            return
        
        plt.figure(figsize=(10,7))
        plt.plot(temps ,dates , marker = 'o')
        plt.title("Temperature vs Date graph")
        plt.xlabel("Date")
        plt.ylabel("Temperature")
        plt.grid(True)
        plt.show()

plot_weather()





