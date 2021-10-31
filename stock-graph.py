# Simple stock graph script
import datetime
from dateutil.relativedelta import relativedelta
from tiingo import TiingoClient
import matplotlib.pyplot as plt
from matplotlib import style
import tkinter as tk
from tkinter import *

all_tickers = []
dates_string = ""
tickers_string = ""
one_year_ago = datetime.datetime.now() - relativedelta(years=1)
six_months_ago = datetime.datetime.now() - relativedelta(months=6)
one_month_ago = datetime.datetime.now() - relativedelta(months=1)
ticker_start_date = any
	
def stock_graph(ticker_input):
    style.use("fivethirtyeight") # matlab style

    config = {}  # config for the TiingoClient and API
    config['session'] = True
    config['api_key'] = '' # Add your own api key for tiingo https://api.tiingo.com/
    client = TiingoClient(config) # setting client equal to the TiingoClient with the api key in config

    end = datetime.datetime.now()

    if str(var.get()) == "One Month":
        ticker_start_date = one_month_ago
        dates_string = "One Month"
    elif str(var.get()) == "Six Months":
        ticker_start_date = six_months_ago
        dates_string = "Six Months"
    elif str(var.get()) == "One Year":
        ticker_start_date = one_year_ago
        dates_string = "One Year"

    ticker = str(ticker_input)

    ticker = ticker.upper()

    all_tickers.append(ticker)

    stock_data = client.get_dataframe(ticker,frequency = 'daily', startDate = ticker_start_date, endDate = end) # setting dataframe with ticker, frequency, dates

    print("\n",ticker,"Data\n",stock_data) 

    tickers_string = ", ".join(all_tickers) 

    print(tickers_string)

    stock_data["high"].plot(label=ticker) # Matlab plotting of graph and showing
    plt.title(tickers_string+" Stock Performance Over "+dates_string)
    plt.legend()

    plt.draw()
    plt.show(block=False)
  
def button_bundle(text):
    ticker_input_data = text.get()
    stock_graph(ticker_input_data)

def radio_selection():
    selection = "You selected " + str(var.get())
    date_label.config(text = selection)

# GUI
root = tk.Tk()
root.title("Stock Performance")
date_label = Label(root)
date_label.config(text = "You selected Six Months")
var = tk.StringVar(None, "Six Months")

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
    
        root.geometry("400x200")

        ticker_label = tk.Label(root, text="Stock Ticker: ")
        text = tk.StringVar()
        ticker_input = tk.Entry(root, textvariable=text)
        ticker_input.focus()

        radio1 = Radiobutton(root, text="One Month", variable=var, value="One Month",command=radio_selection)
        radio1.pack()

        radio2 = Radiobutton(root, text="Six Months", variable=var, value="Six Months",command=radio_selection)
        radio2.pack()

        radio3 = Radiobutton(root, text="One Year", variable=var, value="One Year",command=radio_selection)
        radio3.pack()

        ticker_label.pack()
        ticker_input.pack()

        plot_button = Button(master = root, command = lambda: button_bundle(text),height = 2, width = 10,text = "Go")
        plot_button.pack()

        root.bind('<Return>', lambda x: button_bundle(text))

        date_label.pack()

app = Application(master=root)
app.mainloop()