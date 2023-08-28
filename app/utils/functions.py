import pandas as pd
import mplfinance as mpf
from matplotlib.pyplot import show
import os
from dotenv import load_dotenv
from operator import itemgetter

load_dotenv()

def read_prices() -> pd.DataFrame:
    """ Read provided data and prodive data preprocessing """
    df = pd.read_csv(os.getenv('DATA_STR'))

    df["TS"] = pd.to_datetime(df["TS"])
    df["PRICE"] = pd.to_numeric(df["PRICE"])

    df["DATE"] = pd.to_datetime(df["TS"]).dt.date
    df["DATE"] = df["DATE"].astype("str")

    return df


def create_daily_stocks(df: pd.DataFrame) -> pd.DataFrame:
    """ Split source dataset to different parts and calculate max, min, open price, close price and volume """
    df_max = df.groupby(by=["DATE"])["PRICE"].max().reset_index(name="max")
    df_min = df.groupby(by=["DATE"])["PRICE"].min().reset_index(name="min")
    df_open = df.groupby(by=["DATE"])["PRICE"].first().reset_index(name="first")
    df_close = df.groupby(by=["DATE"])["PRICE"].last().reset_index(name="last")
    df_volume = df.value_counts(subset=["DATE"]).reset_index()

    daily_stocks = (
        df_max.merge(df_min, on="DATE", how="inner")
        .merge(df_open, on="DATE", how="inner")
        .merge(df_close, on="DATE", how="inner")
        .merge(df_volume, on="DATE", how="inner")
    )

    daily_stocks.index = pd.DatetimeIndex(daily_stocks["DATE"])

    daily_stocks.columns = ["Date", "High", "Low", "Open", "Close", "Volume"]

    return daily_stocks


def create_plot(df: pd.DataFrame):
    """ Creating plot using matplotlib """
    mpf.plot(
        df,
        type="candlestick",
        xrotation=0,
        style="yahoo",
        tight_layout=True,
        figratio=(48, 24),
        volume=True,
    )

    # Here you can check links in order to understand why do we need line 55: show(block=False)
    # https://stackoverflow.com/questions/56656777/userwarning-matplotlib-is-currently-using-agg-which-is-a-non-gui-backend-so
    # https://stackoverflow.com/questions/458209/is-there-a-way-to-detach-matplotlib-plots-so-that-the-computation-can-continue/13361748#13361748
    show(block=False)


def calculate_ema(stocks_data, alpha=1, today=None):
    """Perform exponential smoothing with factor `alpha`.

    Time period is a day.
    Each time period the value of `price` drops `alpha` times.
    The most recent data is the most valuable one.
    """
    assert 0 < alpha <= 1

    if alpha == 1:  # no smoothing
        return sum(map(itemgetter(1), stocks_data))

    if today is None:
        today = max(map(itemgetter(0), stocks_data))

    x = [
        (str(date), alpha ** ((today - date).days) * price)
        for date, price in stocks_data
    ]

    return x
