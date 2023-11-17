import yfinance as yf
import pandas as pd

# Function to prompt for date input
def get_user_input_date():
    date_input = input("Enter the start date (YYYY-MM-DD): ")
    return date_input

# Fetch Bitcoin data with user-provided start date
start_date = get_user_input_date()
btc_data = yf.download("BTC-USD", start=start_date, interval="1wk")
btc_data['SMA9'] = btc_data['Close'].rolling(window=9).mean()

# Trading strategy simulation
capital = 100
btc_held = 0
for date, row in btc_data.iterrows():
    if row['Close'] > row['SMA9'] and capital > 0:
        btc_held = capital / row['Close']
        capital = 0
    elif row['Close'] < row['SMA9'] and btc_held > 0:
        capital = btc_held * row['Close']
        btc_held = 0

# Final capital calculation
if btc_held > 0:
    capital = btc_held * btc_data.iloc[-1]['Close']

print(capital)
