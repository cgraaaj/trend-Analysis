import pandas as pd
import datetime as dt
import logging
import os
import multiprocessing
import numpy as np
import pandas as pd

from nsetools.yahooFinance import YahooFinance as yf
from nsetools.nse import Nse

class Driver:
    def __init__(self):
        self.nse = Nse()

    def get_ticker_data(self, interval, range, ticker="CUB.NS"):
        ticker_data = yf(ticker, result_range=range, interval=interval).result
        return ticker_data
