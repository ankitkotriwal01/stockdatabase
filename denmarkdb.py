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


# List of 6300 predefined stocks
stocks = ["VWS.CO","CARL-B.CO","DANSKE.CO","GEN.CO","WDH.CO","TRYG.CO","PNDORA.CO","NOVO-B.CO","MOLS.CO","MAERSK-B.CO","JYSK.CO","IC.CO","FASTPC.CO","DFDS.CO","CHEMM.CO","VIINT.CO","TPSL.CO","TOP.CO","TDC.CO","SYDB.CO","SPNO.CO","SALB.CO","RIAS-B.CO","RBREW.CO","PRIMOF.CO","OJBA.CO","NZYM-B.CO","NRDC.CO","NNIT.CO","NKT.CO","MPI.CO","LUN.CO","LL-B.CO","LASP.CO","JDAN.CO","ISS.CO","GN.CO","GJ.CO","GES.CO","FLS.CO","EXQ.CO","ENALYZ.CO","JOBNDX.CO","ONXEO.CO","BO.CO","WIRTEK.CO","ZEAL.CO","AAB.CO","ELITE-B.CO","PAAL-B.CO","NDA-DKK.CO","SAS-DKK.CO","ADMCAP-B.CO","VIBHK.CO","RILBA.CO","SCHO.CO","ALK-B.CO","ALMB.CO","AM-B.CO","AMBU-B.CO","DAB.CO","AOJ-P.CO","ARKIL-B.CO","ASGGRO.CO","ATHENA.CO","ATLA-DKK.CO","SKJE.CO","BIOPOR.CO","BIF.CO","BLVIS.CO","BNORDIK-CSE.CO","BOCON-B.CO","BORD-B.CO","HARB-B.CO","SBS.CO","HART.CO","UIE.CO","CBRAIN.CO","CHR.CO","CPHNW.CO","CPHCAP.CO","DNORD.CO","DLH.CO","DANTH.CO","DANT.CO","SCD.CO","FED.CO","DJUR.CO","COLUM.CO","COLO-B.CO","LUXOR-B.CO","DSV.CO","TMCOM.CO","SFG.CO","IMAIL-B.CO","EI.CO","ROCK-A.CO","PARKEN.CO","BAVA.CO","NUNA.CO","SPKSJL.CO","SIF.CO","SPG.CO","ESOFT.CO","ROV.CO","KRE.CO","ROCK-B.CO","KLEE-B.CO","CARL-A.CO","JUTBK.CO","SKAKO.CO","NORDJB.CO","DKC.CO","GERHSP-B.CO","MIGA-B.CO","VIPRO.CO","SIM.CO","SIF-B.CO","HOEJ-A.CO","MAERSK-A.CO","EGE-B.CO","FLUG-B.CO","TORM-A.CO","NTR-B.CO","HH.CO","HOEJ-B.CO","MERM.CO","TIV.CO","MATAS.CO","GRLA.CO","ERRIA.CO","GYLD-B.CO","AURI-B.CO","SOLAR-B.CO","STYLE.CO","NEWCAP.CO","LL-A.CO","GYLD-A.CO","FFARMS.CO","HVID.CO","KBHL.CO","TKDV.CO","VELO.CO","STRINV.CO","RTX.CO","GABR.CO","FYNBK.CO","NORTHM.CO","DELTAQ.CO","MNBA.CO","MT-B.CO","SANI.CO","RELLA.CO","RBLN-B.CO","NRDF.CO","VJBA.CO","EGNETY.CO","TOTA.CO","SPEAS.CO","NEUR.CO","STG.CO","EXP-B.CO","LOLB.CO","NORDIC.CO","G4S.CO","OSSR.CO"]


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
        total_debt = format_currency(info.get('totalDebt', 'N/A'))
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
            "Market Cap": market_cap,
            "Open Price": open_price,
            "Average Price": average_price,
            "Beta (1 year)": beta,
            "Bid Price": bid_price,
            "Ask Price": ask_price,
            "PE Ratio (TTM)": pe_ratio_ttm,
            "EPS (TTM)": eps_ttm,
            "Day's Range": day_range,
            "52 Week Range": fifty_two_week_range,
            "1 Year Target": one_year_target,
            "52 Week Change (%)": fifty_two_week_change,
            "Earnings Date": earnings_date,
            "Forward Dividend": forward_dividend,
            "Dividend Yield": dividend_yield,
            "Volume": volume,
            "Ex-Dividend Date": ex_dividend_date,
            "Enterprise Value": enterprise_value,
            "Price/Earnings Ratio (Trailing)": pe_ratio_trailing,
            "Price/Earnings Ratio (Forward)": pe_ratio_forward,
            "PEG Ratio": peg_ratio,
            "Price/Sales Ratio": price_sales_ratio,
            "Price/Book Ratio": price_book_ratio,
            "50-Day Moving Average": fifty_day_moving_average,
            "200-Day Moving Average": two_hundred_day_moving_average,
            "Enterprise Value/EBITDA": enterprise_value_ebitda,
            "Profit Margin": profit_margin,
            "Operating Margin": operating_margin,
            "Return on Assets": return_on_assets,
            "Return on Equity": return_on_equity,
            "Revenue": revenue,
            "Revenue per Share": revenue_per_share,
            "Quarterly Revenue Growth": quarterly_revenue_growth,
            "Gross Profit": gross_profit,
            "EBITDA": ebitda,
            "Diluted EPS": diluted_eps,
            "Quarterly Earnings Growth": quarterly_earnings_growth,
            "Total Cash (MRQ)": total_cash,
            "Total Cash Per Share (MRQ)": total_cash_per_share,
            "Total Debt (MRQ)": total_debt,
            "Current Ratio (MRQ)": current_ratio,
            "Book Value Per Share (MRQ)": book_value_per_share,
            "Operating Cash Flow (TTM)": operating_cash_flow,
            "Levered Free Cash Flow (TTM)": levered_free_cash_flow,
            "Share Statistics": share_statistics,
            "Dividends & Splits": dividends_splits,
            "About Company": about_company
        }
    except Exception as e:
        print(f"Error fetching data for {stock}: {e}")
        return None

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

# Main function to run the Streamlit app
def main():
    st.title("Stock Data Dashboard")

    # Sidebar for selecting stocks
    all_stocks_option = st.sidebar.checkbox("Select All Stocks")
    if all_stocks_option:
        selected_stocks = stocks
    else:
        selected_stocks = st.sidebar.multiselect("Select Stocks", stocks)

    # Placeholder to show data
    placeholder = st.empty()

    # Progress bar
    progress_bar = st.progress(0)

    # Main loop for real-time updates
    while True:
        if selected_stocks:
            stocks_data = update_selected_stocks_data(selected_stocks, progress_bar)
        else:
            stocks_data = update_selected_stocks_data(stocks, progress_bar)

        if not stocks_data:
            placeholder.write("No data to display.")
        else:
            df = pd.DataFrame(stocks_data)
            placeholder.dataframe(df)

        time.sleep(60)  # Wait for 60 seconds before next update

        # Download the metrics table as xlsx
# Download the metrics table as xlsx


if __name__ == "__main__":
    main()

