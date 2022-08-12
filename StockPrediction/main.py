import streamlit as st
import yfinance as yf


st.write("""
# Simple Stock Price App

Shown are the stock **closing prices** and **volume** of Apple!

""")
# define Ticker Symbol
tickerSymbol = 'AAPL'
# get the Data
tickerData = yf.Ticker(tickerSymbol)
# get historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume
""")
st.line_chart(tickerDf.Volume)
