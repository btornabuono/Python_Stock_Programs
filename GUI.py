#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 04:54:44 2018

@author: BrianTornabuono
"""

# Import libraries
from tkinter import *
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import pandas_datareader.data as web
import pandas as pd
import datetime as dt
import csv
import urllib.request as url
from bs4 import BeautifulSoup


class Window:
    def __init__(self, window):
        #*************************  Main Setup  *************************
        self.stock = pd.DataFrame()
        # Main Window size
        self.Main = window.geometry('1000x700')

        #Main Menu Title
        self.title = Label(self.Main, text = 'Main Menu',height = 2, width = 20,
                           font = ('Arial',40))
        self.title.place(x = 275, y = 20)

        #*************************  Main Buttons  *************************

        #Historical menu button
        self.historical_btn = Button(self.Main, text="Historical Plots",
                                     command=self.historical_menu, height = 2, width = 20)
        self.historical_btn.place(x = 100, y = 100)

        #Monte Carlo menu button
        self.Monte_btn = Button(self.Main, text="Monte Carlo Sim",
                                     command=self.monte_menu, height = 2, width = 20)
        self.Monte_btn.place(x = 100, y = 150)

        #Monitor menu button
        self.Monte_btn = Button(self.Main, text="Monitor Stocks",
                                     command=self.monitor, height = 2, width = 20)
        self.Monte_btn.place(x = 100, y = 200)


    def historical_menu(self):
        #********************  Historical Frame Setup  ********************

        # Make Frame for historical plots menu
        self.historical_frame = Frame(self.Main,width = 1000,height = 700)
        self.historical_frame.place(x=0,y=0)
        # Title for Historical Plots Menu
        self.historical_title = Label(self.historical_frame,
                                      text = 'Historical Plots',height = 2,
                                      width = 20,font = ('Arial',40))
        self.historical_title.place(x=275,y=20)


        # ****************** Historical Entry Boxes  *******************

        # Make an entry box too look up stock symbol
        self.sym_label = Label(self.historical_frame, text = 'Stock Symbol:')
        self.sym_label.place(x=100,y=200)
        self.sym_lookup = Entry(self.historical_frame)
        self.sym_lookup.place(x=100,y=220)

        # Make an entry box for number of months to lookup
        self.n_months_label = Label(self.historical_frame, text = 'Number of Months to Look Up:')
        self.n_months_label.place(x=100,y=250)
        self.n_months = Entry(self.historical_frame)
        self.n_months.place(x=100,y=270)


        #*********************  Historical Buttons  *********************

        # Make a button that destroys the frame and returns to main menu
        self.main_btn = Button(self.historical_frame, text = 'Main Menu',
                               command = self.close_historical_frame)
        self.main_btn.place(x = 900, y = 600)

        # Make a submit button
        self.submit_btn = Button(self.historical_frame,text='SUBMIT',height = 1,
                              width = 10, command = self.get_sym_data)
        self.submit_btn.place(x=150,y=300)

        # Add in Plot Price Button
        self.plot_price_btn = Button(self.historical_frame, text = 'Moving Average',
                                     command = self.plot_price,height = 2, width = 20)
        self.plot_price_btn.place(x = 100, y = 100)

        # Add in Plot Candlestick Button
        self.plot_candle_btn = Button(self.historical_frame, text = 'Candlestick',
                                     command = self.plot_candlestick,height = 2, width = 20)
        self.plot_candle_btn.place(x = 100, y = 150)


     # ********************* Monte Carlo Sim Menu **********************8

    def monte_menu(self):

        #******************** Monte Carlo Frame Setup  ********************

        # Make Frame for historical plots menu
        self.monte_frame = Frame(self.Main,width = 1000,height = 700)
        self.monte_frame.place(x=0,y=0)
        # Title for Historical Plots Menu
        self.monte_title = Label(self.monte_frame, text = 'Monte Carlo Sim',
                                 height = 2, width = 20, font = ('Arial',40))
        self.monte_title.place(x=275,y=20)


        # ******************* Monte Carlo Entry Boxes  ******************

        # Make an entry box too look up stock symbol
        self.sym_label = Label(self.monte_frame, text = 'Stock Symbol:')
        self.sym_label.place(x=100,y=180)
        self.sym_lookup = Entry(self.monte_frame)
        self.sym_lookup.place(x=100,y=200)

        # Make an entry box for number of months to forecast
        self.n_months_label = Label(self.monte_frame, text = 'Number of Months for Reference:')
        self.n_months_label.place(x=100,y=230)
        self.n_months_box = Entry(self.monte_frame)
        self.n_months_box.place(x=100,y=250)

        # Make an entry box for number of months to forecast
        self.n_days_label = Label(self.monte_frame, text = 'Number of days to Sim:')
        self.n_days_label.place(x=100,y=280)
        self.n_days_box = Entry(self.monte_frame)
        self.n_days_box.place(x=100,y=300)

        # Make an entry box for number of simulations to run
        self.n_sim_label = Label(self.monte_frame, text = 'Number of Sims to Run:')
        self.n_sim_label.place(x=100,y=330)
        self.n_sim_box = Entry(self.monte_frame)
        self.n_sim_box.place(x=100,y=350)


        #********************  Monte Carlo Buttons  ********************

        # Make a button that destroys the frame and returns to main menu
        self.main_btn = Button(self.monte_frame, text = 'Main Menu',
                               command = self.close_monte_frame)
        self.main_btn.place(x = 900, y = 600)

        # Make a submit button
        self.submit_btn = Button(self.monte_frame,text='SUBMIT',height = 1,
                              width = 10, command = self.get_monte_data)
        self.submit_btn.place(x=150,y=403)

    def monitor(self):
        #******************** Monitor Frame Setup  ********************

        # Make Frame for monitor menu
        self.monitor_frame = Frame(self.Main,width = 1000,height = 700)
        self.monitor_frame.place(x=0,y=0)
        # Title for Historical Plots Menu
        self.monitor_title = Label(self.monitor_frame, text = 'Monitor Stocks',
                                   height = 2, width = 20, font = ('Arial',40))
        self.monitor_title.place(x=275,y=20)

        # ******************* Monitor Entry Boxes  ******************

        # Make an entry box too look up stock symbol
        self.sym_label = Label(self.monitor_frame, text = 'Stock Symbols to Monitor (separate with space):')
        self.sym_label.place(x=100,y=180)
        self.sym_lookup = Entry(self.monitor_frame)
        self.sym_lookup.place(x=100,y=200)


        #********************  Monitor Buttons  ********************

        # Make a submit button
        self.submit_btn = Button(self.monitor_frame,text='SUBMIT',height = 1,
                              width = 10, command = self.scrape_data)
        self.submit_btn.place(x=150,y=250)

        # Make a save button
        self.save_btn = Button(self.monitor_frame,text='Save to CSV',height = 1,
                              width = 10, command = self.save_to_csv)
        self.save_btn.place(x=150,y=300)


    def scrape_data(self):
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
        # Initialize empty arrays
        syms = []
        quotes = []
        count = 0

        symbol = self.sym_lookup.get()
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

                # Add the new row to the dataframe
                stock_df.loc[count] = quotes

                # Clear the list
                quotes.clear()

                count+=1

        except KeyboardInterrupt:
            pass

    def save_to_csv(stock_df):
        with open('stockdata.csv', 'a') as outfile:

            # Write to csv
            write = csv.writer(outfile)
            write.writerow(stock_df)

    def get_monte_data(self):
        sym = self.sym_lookup.get()
        months = int(self.n_months_box.get())
        #start date for stock data
        start = dt.datetime.today() - dt.timedelta(days = months*30)
        #end date for stock data
        end = dt.datetime.today()
        #get apple stock data from google
        self.stock = web.DataReader(sym,'google',start,end)
        #get months to forecast
        n_days = int(self.n_days_box.get())
        n_sim = int(self.n_sim_box.get())
        #only take close data
        prices = self.stock['Close']
        #calculate returns
        returns = prices.pct_change()
        #take last price
        last_price = prices[-1]
        #simulation dataframe
        sim_df = pd.DataFrame()
        date_series=[]
        print('Calculating...')
        for x in range(n_sim):
            count = 0
            daily_vol = returns.std()
            price_series = [last_price]
            price = last_price * (1 + np.random.normal(0,daily_vol))
            price_series.append(price)
            for y in range(n_days):
                if count == n_days-1:
                    break
                price = price_series[count] * (1 + np.random.normal(0,daily_vol))
                price_series.append(price)
                count+=1
            sim_df[x] = price_series

        for i in range(n_days+1):
            date_series.append(dt.datetime.now()+dt.timedelta(days=i-1))
        sim_df.index = date_series

        #Create figure
        fig = Figure(figsize=(6,5))
        price_plot = fig.add_subplot(111)
        price_plot.plot(prices)
        price_plot.plot(sim_df,lw=0.5)
        plt.show()

        #Plot Labels
        price_plot.set_title ("Stock", fontsize=16)
        price_plot.set_ylabel("Price", fontsize=14)
        price_plot.set_xlabel("Date", fontsize=14)

        #Draw Plots
        self.plot_frame = Frame(self.monte_frame,width = 500,height = 500)
        self.plot_frame.place(x=400,y=100)
        canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
        canvas.get_tk_widget().pack()
        canvas.draw()


    # ************************ Get Stock Data ***************************8
    def get_sym_data(self):
        sym = self.sym_lookup.get()
        months = int(self.n_months.get())
        #start date for stock data
        start = dt.datetime.today() - dt.timedelta(days = months*30)
        #end date for stock data
        end = dt.datetime.today()
        #get apple stock data from google
        self.stock = web.DataReader(sym,'google',start,end)

    # ********************** Return To Main ************************
    def close_historical_frame(self):
        self.historical_frame.destroy()
    def close_monte_frame(self):
        self.monte_frame.destroy()

     # ************************ PLot Historical Data ***************************8
    def plot_price(self):
        stock = self.stock
        stock['MA_50'] = stock['Close'].rolling(50).mean().shift()
        #200 day moving average
        stock['MA_200'] = stock['Close'].rolling(200).mean()

        # Sell stock if 200 day MA is greater than 50 day MA
        stock['Sell'] = stock['MA_200']>stock['MA_50']

        # convert to int for plotting
        stock['Sell'] = stock.Sell.astype(int)

        #****************************plots****************************

        #generate figures for plots
        fig = Figure(figsize=(10,10))
        price_plot = fig.add_subplot(111)
        price_plot.plot(stock['Close'], color = 'black')
        price_plot.plot(stock['MA_50'],label = '50 Day Moving Average', color = 'blue')
        price_plot.plot(stock['MA_200'],label = '200 Day Moving Average',color = 'green')

        #plot share volume
        price_plot.plot(stock['Volume']/1000000, color = 'orange',alpha=0.5,
                 label='Volume (in Millions)')
        price_plot.fill_between(stock.index.values,0,stock['Volume']/1000000,color='orange',
                 alpha = 0.25)

        # Mark any time MA_200 > MA_50
        for index, row in stock.iterrows():
            #if close > open
            if row['Sell'] == 1:
                #plot a red line indicating sell
                price_plot.vlines(x = index, ymin = 0,ymax=row['MA_200'],
                           color='red', lw=1)
        #Plot Labels
        price_plot.set_title ("Stock", fontsize=16)
        price_plot.set_ylabel("Price", fontsize=14)
        price_plot.set_xlabel("Date", fontsize=14)
        price_plot.legend(loc=2)

        #Draw Plots
        self.plot_window = Tk()
        canvas = FigureCanvasTkAgg(fig, master=self.plot_window)
        canvas.get_tk_widget().pack()
        canvas.draw()


    def plot_candlestick(self):

        #daily metrics
        ohlc = self.stock
        #if close is larger than open, Gains = true
        ohlc['Gains'] = ohlc['Close']>=ohlc['Open']
        #convert T/F to 1/0
        ohlc['Gains'] = ohlc.Gains.astype(int)

        #generate figure
        fig = Figure(figsize=(10,10))
        candle = fig.add_subplot(111)

        #iterate through the rows of ohlc, plot gains for that day
        for index, row in ohlc.iterrows():
            #if close > open
            if row['Gains'] == 1:
                #plot a thin green line from low to high
                candle.vlines(x = index, ymin = row['Low'], ymax=row['High'],
                           color='green', lw=0.5)
                #plot a thick green line from open to close
                candle.vlines(x = index, ymin = row['Open'], ymax=row['Close'],
                           color='green', lw=2, alpha = 0.5)
            elif row['Gains'] == 0:
                #plot a thin red line from low to high
                candle.vlines(x = index, ymin = row['Low'], ymax=row['High'],
                           color='red', lw=0.5)
                #plot a thick red line from open to close
                candle.vlines(x = index, ymin = row['Open'], ymax=row['Close'],
                       color='red', lw=2,alpha = 0.5)

        #Plot Titles
        candle.set_title ("Stock", fontsize=16)
        candle.set_ylabel("Price", fontsize=14)
        candle.set_xlabel("Date", fontsize=14)

        #show plot
        self.plot_window = Tk()
        canvas = FigureCanvasTkAgg(fig, master=self.plot_window)
        canvas.get_tk_widget().pack()
        canvas.draw()
        plt.show()


# MAIN
root = Tk()
start = Window(root)
root.mainloop()
