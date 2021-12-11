import yfinance as yf
import streamlit as st

st.write("""
# **Stock price Data App**
The app tracks 10 year data on the stock price of **Meta**
""")
tickerSymbol = 'FB'
tickerData = yf.Ticker(tickerSymbol)
tickerDataframe = tickerData.history(period='1d', start='2011-11-10', end='2021-11-10')
# Open	High	Low	Close	Volume	Dividends	Stock Splits
st.write(""" ## Closing Price """)
st.line_chart(tickerDataframe.Close)
st.write(""" ## Volume """)
st.line_chart(tickerDataframe.Volume)
st.write(""" ## Highs """)
st.line_chart(tickerDataframe.High)
st.write(""" ## Lows """)
st.line_chart(tickerDataframe.Low)