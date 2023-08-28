from collections import namedtuple
import pandas as pd

from app.utils.functions import (
    read_prices,
    create_daily_stocks,
    create_plot,
    calculate_ema,
)


class CreateStocksPlotUseCase:
    def __init__(self) -> None:
        pass

    def create_stocks_plot(self):
        df = read_prices()
        daily_stocks = create_daily_stocks(df)
        create_plot(daily_stocks)

    def calculate_stock_ema(self):
        StockData = namedtuple("StocksData", "date price")

        df = pd.read_csv("app/data/prices.csv")
        df["TS"] = pd.to_datetime(df["TS"])

        price = list(df["PRICE"])
        days = list(df["TS"])

        stock_data = list(map(StockData, days, price))

        data = calculate_ema(stock_data, alpha=0.5)

        print(data)
