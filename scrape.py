import csv
import time
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

style.use('ggplot')
# Variables used for scrape
apple_price = []
amazon_price = []
google_price = []
time_stamp = []

# Used to write csv, will hold all values from scrape
stock_data = []

# Variables used for analysis
dates = []
apple_data = []
amazon_data = []
google_data = []

# Index place holder
i = 0

# The next three functions take care of the scrape for the stock prices taken from nasdaq
def apple_scrape():
    page = requests.get('https://www.nasdaq.com/symbol/aapl/real-time')
    soup = BeautifulSoup(page.content,'html.parser')
    stock_price = soup.find_all('td')[9].get_text()
    stock_price = stock_price[1:7]
    time.sleep(3)
    return stock_price
def amazon_scrape():
    page = requests.get('https://www.nasdaq.com/symbol/amzn/after-hours')
    soup = BeautifulSoup(page.content,'html.parser')
    stock_price = soup.find_all('td')[13].get_text()
    stock_price = float(stock_price[2:10].replace(',',''))
    time.sleep(3)
    return stock_price
def google_scrape():
    page = requests.get('https://www.nasdaq.com/symbol/goog/after-hours')
    soup = BeautifulSoup(page.content,'html.parser')
    stock_price = soup.find_all('td')[13].get_text()
    stock_price = float(stock_price[1:10].replace(',',''))
    time.sleep(3)
    return stock_price
# Function for Writing data to the csv for further analysis
def write_csv(data):
    with open('stockdata.csv', 'a') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(data)

# Body of program:
# Scrapes data from nasdaq site for apple, amazon and google
# Prints data in terminal and saves in a csv for future data analysis
# Kill program by hitting CTRL^C

try:
    while True:
        # Determine share price of stocks
        apple_price.append(apple_scrape())
        amazon_price.append(amazon_scrape())
        google_price.append(google_scrape())

        # Configure the timestamp as a string in standard form
        time_stamp.append(dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        # If timestamp is at 9:30, save this as the opening price for each stock
        if dt.datetime.now().strftime("%H:%M") == "9:30":
            time_stamp[i] = "Opening Price"
        #If timestamp is at 4:30, save this as the closing price for each stock
        elif dt.datetime.now().strftime("%H:%M") == "4:30":
            time_stamp[i] = "Closing Price"

        print('  Time: ', time_stamp[i],'Apple Price: $',apple_price[i],'   Amazon Price: $',amazon_price[i],'   Google Price: $',google_price[i],'\n')
        write_csv([time_stamp[i], apple_price[i], amazon_price[i], google_price[i]])
        i+=1

except KeyboardInterrupt:
    pass
