from app.utils.functions import read_prices, create_daily_stocks,calculate_ema
from collections import namedtuple
import pandas as pd

def test_read_prices():
    """Verify output of test_read_prices() funtion"""
    output = read_prices()

    assert len(output.columns) == 3

    assert output.columns[0] == "TS"
    assert output.columns[1] == "PRICE"
    assert output.columns[2] == "DATE"

    assert output["TS"].dtype == "<M8[ns]"
    assert output["PRICE"].dtype == "float64"
    assert output["DATE"].dtype == "object"


def test_create_daily_stocks():
    """Verify output of create_daily_stocks() funtion"""
    df = read_prices()
    output = create_daily_stocks(df)

    assert len(output.columns) == 6
    assert (output.columns == ["Date", "High", "Low", "Open", "Close", "Volume"]).all()

    assert output["Date"].dtype == "object"
    assert output["High"].dtype == "float64"
    assert output["Low"].dtype == "float64"
    assert output["Open"].dtype == "float64"
    assert output["Close"].dtype == "float64"
    assert output["Volume"].dtype == "int64"


def test_calculate_ema():
    """Verify output of EMA funtion"""

    StockData = namedtuple("StocksData", "date price")

    price = [1000.0, 2000.0, 1500.0, 1200.0]
    days = ['2023-05-04 18:00:00.000000000', '2023-05-05 19:00:00.000000000', '2023-05-06 20:00:00.000000000', '2023-05-07 21:00:00.000000000']
    days = [pd.to_datetime(day) for day in days]

    stock_data = list(map(StockData, days, price))

    test_result = calculate_ema(stocks_data=stock_data, alpha=0.5)

    assert test_result[0][0] == '2023-05-04 18:00:00'
    assert test_result[0][1] == 125.0

    assert test_result[1][0] == '2023-05-05 19:00:00'
    assert test_result[1][1] == 500.0

    assert test_result[2][0] == '2023-05-06 20:00:00'
    assert test_result[2][1] == 750.0

    assert test_result[3][0] == '2023-05-07 21:00:00'
    assert test_result[3][1] == 1200.0