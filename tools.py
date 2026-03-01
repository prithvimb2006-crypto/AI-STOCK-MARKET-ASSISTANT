import yfinance as yf
from indicators import calculate_moving_average, calculate_rsi

def fetch_stock_data(symbol="ADANIPOWER.BO", period="6mo"):
    stock = yf.Ticker(symbol)
    df = stock.history(period=period)
    return df

def analyze_stock(symbol="ADANIPOWER.BO"):
    df = fetch_stock_data(symbol)

    ma50 = calculate_moving_average(df, 50)
    rsi = calculate_rsi(df)
    latest_price = df['Close'].iloc[-1]

    return {
        "symbol": symbol,
        "latest_price": round(float(latest_price), 2),
        "ma50": round(float(ma50), 2),
        "rsi": round(float(rsi), 2)
    }