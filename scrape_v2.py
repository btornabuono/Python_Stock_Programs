# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Librarys
import pandas as pd
import datetime as dt
import time
import csv
import urllib.request as url
from bs4 import BeautifulSoup


def get_quote(symbol):
    # Quote page using symbol
    adress = 'https://www.bloomberg.com/quote/'+symbol+':US'

    # Query Bloomberg quote page
    page = url.urlopen(adress)

    # Parse HTML
    soup = BeautifulSoup(page,'html.parser')

    # Grab the stock quote text
    quote_txt = soup.find('span',attrs={'class':'priceText__1853e8a5'})

    # Convert quote to float and remove comma
    quote = float(quote_txt.text.strip().replace(',',''))

    # Store new quote in the price list
    return quote

def write_csv(data):
    # Create or open csv file for data
    with open('stockdata.csv', 'a') as outfile:

        # Write to csv
        write = csv.writer(outfile)
        write.writerow(data)

# Take user stock symbol input
symbol = input('Enter stock symbols you would like to monitor separated by a space: ')

# Initialize empty arrays
syms = []
quotes = []
count = 0

# Split user input in case of multiple inputs
syms = symbol.split(' ')

# Create DataFrame initialized with date column and at the current time
stock_df = pd.DataFrame(columns = ['Date'])
stock_df['Date'] = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Create columns with the stock symbol as a name and get first quote
for sym in syms:
            stock_df[sym] = get_quote(sym)

try:
    while True:
        # Save the time the quote was taken
        quotes.append(dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        # Get quotes for each symbol using get_quote function defined above
        for sym in syms:
            quotes.append(get_quote(sym))

        stock_df.loc[count] = quotes
        # Write the quotes to a csv
        write_csv(quotes)
        quotes.clear()

        count+=1

except KeyboardInterrupt:
    pass
