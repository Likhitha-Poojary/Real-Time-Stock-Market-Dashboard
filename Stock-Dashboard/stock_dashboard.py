import streamlit as st
import yfinance as yf
import plotly.express as px

st.set_page_config(page_title="Stock Market Dashboard", layout="wide")
st.title("📈 Real-Time Stock Market Dashboard")

# User input
stock_symbol = st.text_input("Enter Stock Symbol (e.g. AAPL, TSLA, INFY):", "AAPL")

if stock_symbol:
    stock = yf.Ticker(stock_symbol)
    df = stock.history(period="1mo", interval="1d")

    if not df.empty:
        st.subheader(f"Stock Price for {stock_symbol}")
        fig = px.line(df, x=df.index, y="Close", title=f"{stock_symbol} Closing Prices")
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Recent Data")
        st.dataframe(df.tail())
    else:
        st.error("No data found. Try another symbol.")
