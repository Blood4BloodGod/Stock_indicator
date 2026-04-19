import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker: str, start="2020-01-01", end="2024-01-01"):
    df = yf.download(ticker, start=start, end=end)

    if df.empty:
        raise ValueError("No data found")

    if isinstance(df.columns, pd.MultiIndex):#multiindex columns can cause issues, so we flatten them
        df.columns = df.columns.get_level_values(0)

    # Clean column names
    df.columns = [col.lower().replace(" ", "_") for col in df.columns]

    df.reset_index(inplace=True)

    return df

def add_basic_features(df):
    df = df.copy()

    df["daily_return"] = df["close"].pct_change()
    df["ma_10"] = df["close"].rolling(10).mean()
    df["ma_50"] = df["close"].rolling(50).mean()

    return df