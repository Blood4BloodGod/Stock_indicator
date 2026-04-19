from Data_Loader import fetch_stock_data, add_basic_features, plot_stock
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def main():
    print("Starting program...")

    tickers = ["AAPL", "TSLA", "GOOG"]

    all_data = {}
    returns_df = pd.DataFrame()

    # Load and process data
    for ticker in tickers:
        print(f"\nFetching {ticker}...")

        df = fetch_stock_data(ticker)
        df = add_basic_features(df)

        all_data[ticker] = df
        returns_df[ticker] = df["daily_return"]

        print(df[["date", "close"]].head())

        # Plot individual stock
        plot_stock(df, ticker)

    # Clean returns
    returns_df.dropna(inplace=True)

    # Correlation analysis
    correlation = returns_df.corr()

    print("\nCorrelation Matrix:")
    print(correlation)

    # Heatmap
    plt.figure()
    sns.heatmap(correlation, annot=True)
    plt.title("Stock Return Correlation")
    plt.show()


if __name__ == "__main__":
    main()