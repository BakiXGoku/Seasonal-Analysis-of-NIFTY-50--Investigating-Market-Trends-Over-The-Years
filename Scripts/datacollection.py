import yfinance as yf

# Fetching NIFTY50 data from yahoo finance 
nifty50 = yf.download("^NSEI", start="2000-01-01", end="2025-01-01")
nifty50.to_csv("nifty50_data.csv")
