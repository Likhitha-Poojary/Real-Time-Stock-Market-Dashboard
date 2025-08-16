📊 Project Overview

Objective:
Create an interactive dashboard to visualize real-time stock prices.

Technologies Used:

Streamlit: For building the interactive web application.

yfinance: To fetch real-time stock data.

Plotly: For creating interactive visualizations.

Features:

Input any stock symbol (e.g., AAPL, TSLA) to view the past month's closing prices.

Interactive line chart displaying stock price trends.

Recent stock data displayed in a table format.

🛠️ Setup Instructions

To run the project locally:

Clone the repository:

git clone https://github.com/Likhitha-Poojary/Real-Time-Stock-Market-Dashboard.git
cd Real-Time-Stock-Market-Dashboard


Create and activate a conda environment:

conda create -n stockenv python=3.9 -y
conda activate stockenv


Install the required packages:

pip install streamlit yfinance plotly


Run the Streamlit application:

streamlit run stock_dashboard.py

<img width="1915" height="878" alt="image" src="https://github.com/user-attachments/assets/61da77d3-0c44-47ba-a3b6-57d33fe280fb" />



Add a screenshot of your dashboard here.

🚀 Future Enhancements

User Authentication: Implement user login to save favorite stocks.

Advanced Analytics: Integrate technical indicators like RSI, MACD.

Mobile Responsiveness: Ensure the dashboard is fully responsive on mobile devices.
