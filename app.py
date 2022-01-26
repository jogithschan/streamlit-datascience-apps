import yfinance as yf
import streamlit as st
from datetime import date
from dateutil.relativedelta import relativedelta

st.write("""
# **Stock price Data App**
The app tracks 5 year data on the stock price of **Meta**
""")
tickerSymbol = 'FB'
tickerData = yf.Ticker(tickerSymbol)
oneMonthAgo = date.today() - relativedelta(months=1)
# tenYearsAgo = oneMonthAgo - relativedelta(years=10)
tenYearsAgo = date.today() - relativedelta(years=5)
st.write("""### Start Date - """, tenYearsAgo, """ End Date - """, date.today())
tickerDataframe = tickerData.history(period='1d', start=tenYearsAgo, end=date.today())
# Open	High	Low	Close	Volume	Dividends	Stock Splits
st.write(""" ## Closing Price """)
st.line_chart(tickerDataframe.Close)
st.write(""" ## Volume """)
st.line_chart(tickerDataframe.Volume)
st.write(""" ## Highs """)
st.line_chart(tickerDataframe.High)
st.write(""" ## Lows """)
st.line_chart(tickerDataframe.Low)