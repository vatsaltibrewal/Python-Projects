import requests
import csv
import os
import datetime
import matplotlib.pyplot as plt
import time
import schedule

def fetch_latest_price(url, params):
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        print("Data Fetched Successfully!")
        return response.json()
    except requests.RequestException as e:
        print("An Error Occured While Fetching:", e)

def save_data_to_CSV(data, fileName = "cryptoData.csv"):
    fileExixts = os.path.isfile(fileName)

    with open(fileName, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        if not fileExixts:
            writer.writerow(['coin', 'price', 'timestamp'])
        
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")

        for coin in data:
            writer.writerow([coin["id"], coin["current_price"], timestamp])
    print("Data Saved to : ", fileName)

def create_plot(coinId, fileName = "cryptoData.csv"):
    timestamp = []
    price = []

    with open(fileName, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['coin'] == coinId:
                timestamp.append(row['timestamp'])
                price.append(float(row['price']))
    
    if not timestamp:
        print("No Data Found")
        return None
    
    plt.figure(figsize=(10,5))
    plt.plot(timestamp, price, marker='o')
    plt.tight_layout()
    plt.grid()
    plt.show()

def job():
    API_URL = "https://api.coingecko.com/api/v3/coins/markets"
    PARAMS = {
        "vs_currency" : "usd",
        "order" : "market_cap_desc",
        "per_page" : 20
    }

    data = fetch_latest_price(API_URL, PARAMS)
    save_data_to_CSV(data)

if __name__ == "__main__":
    API_URL = "https://api.coingecko.com/api/v3/coins/markets"
    PARAMS = {
        "vs_currency" : "usd",
        "order" : "market_cap_desc",
        "per_page" : 20
    }

    data = fetch_latest_price(API_URL, PARAMS)
    save_data_to_CSV(data)

    choice = input("Enter the coinname to get graph: ").strip().lower()

    if choice:
        create_plot(choice)
    print("Done")

    '''
    Uncomment the following lines to enable scheduling
    Schedule the job every hour

    schedule.every().hour.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)
    '''
