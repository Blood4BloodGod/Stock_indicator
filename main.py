#Aim to use kaggle's given data to prject the future price of  using a model
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from Data_Loader import fetch_stock_data, add_basic_features

def main():
    print("Starting program...")

    ticker = "AAPL"
    df = fetch_stock_data(ticker)
    df = add_basic_features(df)

    print(df.head())


main()