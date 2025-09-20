
import os
import csv
import requests
from datetime import datetime
import matplotlib.pyplot as plt
import schedule
import time

api_url = "https://api.coingecko.com/api/v3/coins/markets"

parameters = {
    'vs_currency' : 'usd' ,
    'order' : 'market_cap_desc',
    'per_page' : 10 , 
    'page' : 1,
    'sparkline' : False
}

csv_file = 'crypto_info.csv'

def fetch_data():
    response = requests.get(api_url, params = parameters)
    return response.json()



def save_to_csv(data):
    file_exsits = os.path.isfile(csv_file)

    with open(csv_file , 'a' , newline='') as file:
        writer = csv.writer(file)
        if not file_exsits: #write headers
            writer.writerow(["timestamp" , "coin" , "price"])

        timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")

        for coin in data:
            writer.writerow([timestamp , coin['id'] , coin['current_price']])

        
    print("data saved to csv")

def job(): #job is the function to do something repeatedly, say every hour , every min etc
    print("fetching data hourly!")
    crypto_data = fetch_data()
    save_to_csv(crypto_data)

schedule.every().hour.at(":00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

# def plot_graph(coin_id):
#     times = []
#     prices = []

#     with open(csv_file , 'r' , newline='') as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             if row['coin'] == coin_id:
#                 times.append(row['timestamp'])
#                 prices.append(float(row['price']))

#         if not times and not prices:
#             print(f"no data to plot for {coin_id}")
#             return
        
#     plt.figure(figsize=(10,5))
#     plt.plot(times , prices , marker = 'o')
#     plt.tight_layout()
#     plt.grid()
#     plt.show()

    
# def main():
#     print("getting crypto data!")
#     crypto_data = fetch_data()
#     save_to_csv(crypto_data)

#     for coin in crypto_data:
#         print(f"{coin['id']}\n")

#     coin_name = input("enter the coin name for graph: ").strip().lower()

#     if coin_name:
#         plot_graph(coin_name)

# if __name__ == "__main__":
#     main()

