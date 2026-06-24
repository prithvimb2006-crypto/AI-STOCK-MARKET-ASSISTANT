import streamlit as st
import yfinance as yf
from main import run_assistant
def calculate_rsi(df,period=14):
    delta =df["Close"].diff()
    gain=delta.where(delta>0,0)
    loss=-delta.where(delta<0,0)
    avg_gain=gain.rolling(period).mean()
    avg_loss=loss.rolling(period).mean()
    rs=avg_gain/avg_loss
    rsi=100-(100/(1+rs))
    return rsi
st.set_page_config(page_title="AI Stock Market Assistant", layout="wide")
st.title("AI Stock Market Assistant")
st.write("Analyze stocks")
st.sidebar.title("Navigation")
st.sidebar.title("Interval-Timeframe Selection")
st.sidebar.write("1m:~7 days\n\n5m:~60 days\n\n15m:~60 days\n\n30m:~60 days\n\n1h:~730 days (varies)\n\n1d:Many years")
st.sidebar.write("Enter a stock ticker and click Analyze.")
col1,col2,col3=st.columns(3)
with col1:
    symbol=st.text_input("Enter stock ticker")
with col2:
    timeframe=st.selectbox("Select Time Frame",["1d","7d","1mo","2mo","3mo","6mo","1y","2y"])
with col3:
    interval=st.selectbox("Select interval",["1m","5m","15m","30m","60m","90m","1d","5d","1wk","1mo"])
if st.button("Analyze"):
    if symbol:
        try:
            
            df=yf.Ticker(symbol).history(period=timeframe,interval=interval)
            if df.empty:
                st.error("Invalid stock stock ticker.")
                st.stop()
            df["MA100"] = df["Close"].rolling(window=100).mean()
            df["RSI"]=calculate_rsi(df)
            rsi=round(df["RSI"].iloc[-1],2)
            current_price = round(df["Close"].iloc[-1], 2)
            ma100=round(df["MA100"].iloc[-1],-2)
            rsi=round(df["RSI"].iloc[-1],2)
            col1,col2,col3=st.columns(3)
            with col1:
                st.metric("Current Price",f"${current_price}")
            with col2:
                st.metric("RSI",rsi)
            with col3:
                st.metric("MA100",f"${ma100}")
            st.subheader("Stock price chart")
            st.line_chart(df["Close"])
            st.subheader("AI Analysis")
            prompt=f"""Analyze the stock {symbol} Current Price: {current_price} RSI: {rsi} MA100: {ma100}
            Give:
            1. Trend Analysis
            2. Momentum Analysis
            3. Risks
            4. Short-term Outlook"""
        except Exception as e:
            st.error(f"Error:{e}")
    else:
        st.warning("Please enter a stock ticker.")
