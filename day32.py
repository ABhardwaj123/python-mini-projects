import os
import csv
import requests
from datetime import datetime
import matplotlib.pyplot as plt
import schedule
import sqlite3
import time

api_url = "https://api.coingecko.com/api/v3/coins/markets"

parameters = {
    'vs_currency' : 'usd' ,
    'order' : 'market_cap_desc',
    'per_page' : 10 , 
    'page' : 1,
    'sparkline' : False         #sparkline is small graph data
}

database = 'crypto.db'

def create_table():
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS crypto_prices (
                   id INTEGER PRIMARY KEY AUTOINCREMENT ,
                   timestamp TEXT ,
                   coin TEXT ,
                   price REAL
                   ) 
    ''')
    connection.commit()
    connection.close()


def save_info(data):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    timestamp = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    for coin in data:
        cursor.execute('''
                INSERT INTO crypto_prices (timestamp , coin , price)
                    VALUES (? , ? , ?)
            ''', (timestamp , coin['id'] , coin['current_price']))

    connection.commit()
    connection.close()
    print("data saved to database!")


def search_in_table(coin_name):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    cursor.execute('''
                SELECT timestamp , price from crypto_prices
                   WHERE coin = ?
                   ORDER BY timestamp DESC
                   LIMIT 1

        ''', (coin_name ,))
    
    result = cursor.fetchone()

    connection.commit()
    connection.close()

    if result:
        print(f"price -> {result[1]} - {result[0]}")


def fetch_data():
    response = requests.get(api_url, params = parameters)
    return response.json()


def main():
    create_table()
    print("1. Fetch and store data")
    print("2. search price of a coin")
    print("3. exit")

    while(True):
        choice = int(input("enter your choice: "))

        if choice == 1:
            data = fetch_data()
            save_info(data)
        elif choice == 2:
            coin_name = input("enter coin name: ").strip().lower()
            search_in_table(coin_name)
        elif choice == 3:
            break
        else:
            print("invalid choice")


if __name__ == "__main__":
    main()