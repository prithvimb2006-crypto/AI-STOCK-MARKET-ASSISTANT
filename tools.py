import yfinance as yf
from indicators import calculate_moving_average, calculate_rsi

def fetch_stock_data(symbol, period="2y"):
    stock = yf.Ticker(symbol)
    df = stock.history(period=period)
    return df

def analyze_stock(symbol):
    df = fetch_stock_data(symbol)

    ma100 = calculate_moving_average(df, 100)
    rsi = calculate_rsi(df)
    latest_price = df['Close'].iloc[-1]

    return {
        "symbol": symbol,
        "latest_price": round(float(latest_price), 2),
        "ma100": round(float(ma100), 2),
        "rsi": round(float(rsi), 2)
    }