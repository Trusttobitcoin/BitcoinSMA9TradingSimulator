# BitcoinSMA9TradingSimulator

## Description
The BitcoinSMA9TradingSimulator is a Python tool for simulating a Bitcoin trading strategy based on the 9-week Simple Moving Average (SMA9). This project aims to provide an insight into how such a strategy would have performed historically, starting from a user-specified date.

## Getting Started

### Dependencies
- Python 3.x
- pandas
- yfinance

### Installing
- Ensure Python 3.x is installed on your machine.
- Install required Python packages:

### Executing Program
- Run the script using Python:

- When prompted, enter the start date for the simulation in the format YYYY-MM-DD.

## How It Works
- The tool fetches historical Bitcoin data from Yahoo Finance starting from the user-specified date.
- It calculates the 9-week SMA for Bitcoin's closing prices.
- The trading strategy is simulated as follows:
- Buy Bitcoin when its price is above the 9-week SMA.
- Sell Bitcoin when its price is below the 9-week SMA.
- The simulation assumes an initial investment of $100 and calculates the final capital at the end of the data series.

## Disclaimer
This tool is for educational purposes only. Past performance is not indicative of future results. It does not account for transaction fees, slippage, or other real-world trading factors.

## Acknowledgments
Inspiration, code snippets, etc.
* [yfinance](https://pypi.org/project/yfinance/)
* [pandas](https://pandas.pydata.org/)

