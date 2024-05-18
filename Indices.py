import streamlit as st
import yfinance as yf
import pandas as pd
import time
from datetime import datetime
import base64
import io
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st


stocks = [
    "^GSPTSE",   # S&P/TSX Composite Index
    "^GSPC",     # S&P 500
    "^DJI",      # Dow Jones Industrial Average
    "^IXIC",     # NASDAQ Composite
    "^NYA",      # NYSE Composite
    "^XAX",      # NYSE AMEX Composite Index
    "^RUT",      # Russell 2000
    "^VIX",      # CBOE Volatility Index
    "^FTSE",     # FTSE 100
    "^GDAXI",    # DAX Performance-Index
    "^FCHI",     # CAC 40
    "^STOXX50E", # ESTX 50 PR.EUR
    "^N100",     # Euronext 100 Index
    "^BFX",      # BEL 20
    "IMOEX.ME",  # MOEX Russia Index
    "^N225",     # Nikkei 225
    "^HSI",      # Hang Seng Index
    "000001.SS", # SSE Composite Index
    "399001.SZ", # Shenzhen Index
    "^STI",      # STI Index
    "^AXJO",     # S&P/ASX 200
    "^AORD",     # All Ordinaries
    "^BSESN",    # S&P BSE SENSEX
    "^JKSE",     # IDX Composite
    "^KLSE",     # FTSE Bursa Malaysia KLCI
    "^NZ50",     # S&P/NZX 50 Index Gross
    "^KS11",     # KOSPI Composite Index
    "^TWII",     # TSEC Weighted Index
    "^BVSP",     # IBOVESPA
    "^MXX",      # IPC Mexico
    "^IPSA",     # S&P/CLX IPSA
    "^MERV",     # MERVAL
    "^TA125.TA", # TA-125
    "^CASE30",   # EGX 30 Price Return Index
    "^JN0U.JO",  # Top 40 USD Net TRI Index
    "^NSEI",     # NIFTY 50
    "^OMX",      # OMX Stockholm 30 Index
    "^OSEAX",    # Oslo Børs All-Share Index
    "^IBEX",     # IBEX 35
    "^ATX",      # Austrian Traded Index
    "^OMXC25",   # OMX Copenhagen 25
    "^MERV",     # MERVAL Buenos Aires
    "^HSCE",     # Hang Seng China Enterprises Index
    "^JKSE",     # Jakarta Composite Index
    "^STI",      # Straits Times Index
    "^NGE",      # NSE All-Share Index
    "^ISEQ",     # ISEQ Overall Index
    "^OMXH25",   # OMX Helsinki 25
]

# Function to fetch data for a given stock
def fetch_stock_data(stock):
    try:
        data = yf.Ticker(stock)
        info = data.info
        name = info.get('shortName', 'N/A')
        previous_close = format_currency(info.get('previousClose', 'N/A'))
        market_cap = format_currency(info.get('marketCap', 'N/A'))
        open_price = format_currency(info.get('regularMarketOpen', 'N/A'))
        average_price = format_currency(info.get('regularMarketPrice', 'N/A'))
        beta = info.get('beta', 'N/A')
        bid_price = format_currency(info.get('bid', 'N/A'))
        ask_price = format_currency(info.get('ask', 'N/A'))
        pe_ratio_ttm = info.get('trailingPE', 'N/A')
        eps_ttm = format_currency(info.get('trailingEps', 'N/A'))
        day_range = format_currency(info.get('dayLow', 'N/A')) + ' - ' + format_currency(info.get('dayHigh', 'N/A'))
        fifty_two_week_range = format_currency(info.get('fiftyTwoWeekLow', 'N/A')) + ' - ' + format_currency(info.get('fiftyTwoWeekHigh', 'N/A'))
        one_year_target = format_currency(info.get('targetMeanPrice', 'N/A'))
        fifty_two_week_change = format_percentage(info.get('52WeekChange', 'N/A'))
        earnings_date = info.get('earningsDate', 'N/A')
        forward_dividend = format_currency(info.get('forwardDividendRate', 'N/A'))
        dividend_yield = format_percentage(info.get('dividendYield', 'N/A'))
        volume = info.get('volume', 'N/A')
        ex_dividend_date = info.get('exDividendDate', 'N/A')
        enterprise_value = format_currency(info.get('enterpriseValue', 'N/A'))
        pe_ratio_trailing = info.get('trailingPE', 'N/A')
        pe_ratio_forward = info.get('forwardPE', 'N/A')
        peg_ratio = info.get('pegRatio', 'N/A')
        price_sales_ratio = info.get('priceToSalesTrailing12Months', 'N/A')
        price_book_ratio = info.get('priceToBook', 'N/A')
        fifty_day_moving_average = format_currency(info.get('fiftyDayAverage', 'N/A'))
        two_hundred_day_moving_average = format_currency(info.get('twoHundredDayAverage', 'N/A'))
        enterprise_value_ebitda = format_currency(info.get('enterpriseToEbitda', 'N/A'))
        profit_margin = format_percentage(info.get('profitMargins', 'N/A'))
        operating_margin = format_percentage(info.get('operatingMargins', 'N/A'))
        return_on_assets = format_percentage(info.get('returnOnAssets', 'N/A'))
        return_on_equity = format_percentage(info.get('returnOnEquity', 'N/A'))
        revenue = format_currency(info.get('totalRevenue', 'N/A'))
        revenue_per_share = format_currency(info.get('revenuePerShare', 'N/A'))
        quarterly_revenue_growth = format_percentage(info.get('quarterlyRevenueGrowth', 'N/A'))
        gross_profit = format_currency(info.get('grossProfit', 'N/A'))
        ebitda = format_currency(info.get('ebitda', 'N/A'))
        diluted_eps = format_currency(info.get('trailingEps', 'N/A'))
        quarterly_earnings_growth = format_percentage(info.get('earningsQuarterlyGrowth', 'N/A'))
        total_cash = format_currency(info.get('totalCash', 'N/A'))
        total_cash_per_share = format_currency(info.get('totalCashPerShare', 'N/A'))
        # debt', 'N/A'))
        current_ratio = info.get('currentRatio', 'N/A')
        book_value_per_share = format_currency(info.get('bookValue', 'N/A'))
        operating_cash_flow = format_currency(info.get('operatingCashflow', 'N/A'))
        levered_free_cash_flow = format_currency(info.get('freeCashflow', 'N/A'))
        share_statistics = format_currency(info.get('sharesOutstanding', 'N/A'))
        dividends_splits = info.get('dividendsAndSplits', 'N/A')
        about_company = info.get('longBusinessSummary', 'N/A')

        return {
            "Symbol": stock,
            "Name": name,
            "Previous Close": previous_close,
            "Open Price": open_price,
            "Bid Price": bid_price,
            "Ask Price": ask_price,
            "Day's Range": day_range,
            "52 Week Range": fifty_two_week_range,
            "Volume": volume,
            "50-Day Moving Average": fifty_day_moving_average,
            "200-Day Moving Average": two_hundred_day_moving_average,
        }
    except Exception as e:
        print(f"Error fetching data for {stock}: {e}")
        return None

# Main function to run the Streamlit app
def main():
    st.title("World Equity Indices")

    # Placeholder to show data
    placeholder = st.empty()

    # Progress bar
    progress_bar = st.progress(0)

    # Main loop for real-time updates
    while True:
        stocks_data = update_selected_stocks_data(stocks, progress_bar)

        if not stocks_data:
            placeholder.write("No data to display.")
        else:
            df = pd.DataFrame(stocks_data)
            placeholder.dataframe(df)

        time.sleep(60)  # Wait for 60 seconds before next update

# Function to update data for selected stocks
def update_selected_stocks_data(selected_stocks, progress_bar):
    data = []
    for i, stock in enumerate(selected_stocks):
        progress_bar.progress((i + 1) / len(selected_stocks))
        stock_data = fetch_stock_data(stock)
        if stock_data:
            data.append(stock_data)
    return data

# Function to format currency
def format_currency(value):
    if value != 'N/A':
        return "${:,.2f}".format(value)
    else:
        return value

# Function to format percentage
def format_percentage(value):
    if value != 'N/A':
        return "{:.2f}%".format(value)
    else:
        return value

if __name__ == "__main__":
    main()

