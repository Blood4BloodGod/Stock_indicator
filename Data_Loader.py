import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


def fetch_stock_data(ticker: str, start="2020-01-01", end="2024-01-01"):#added default date range for easier testing
    df = yf.download(ticker, start=start, end=end)

    if df.empty:
        raise ValueError(f"No data found for {ticker}")

    # Handle MultiIndex columns
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    # Normalize column names
    df.columns = [col.lower().replace(" ", "_") for col in df.columns]

    df.reset_index(inplace=True)

    # Fix Date column
    df.rename(columns={"Date": "date"}, inplace=True)

    return df


def add_basic_features(df):#added copy to avoid modifying original DataFrame
    df = df.copy()

    df["daily_return"] = df["close"].pct_change()
    df["ma_10"] = df["close"].rolling(10).mean()
    df["ma_50"] = df["close"].rolling(50).mean()
    df["volatility"] = df["daily_return"].rolling(10).std()

    return df


def plot_stock(df, ticker):#added ticker argument for better labeling
    plt.figure()

    plt.plot(df["date"], df["close"], label="Close Price")
    plt.plot(df["date"], df["ma_10"], label="MA 10")
    plt.plot(df["date"], df["ma_50"], label="MA 50")

    plt.title(f"{ticker} Price with Moving Averages")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()

    plt.show()