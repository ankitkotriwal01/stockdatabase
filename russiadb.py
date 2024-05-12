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
stocks = ["MOEX.ME","HYDR.ME","DIXY.ME","IDVP.ME","DZRDP.ME","VRSBP.ME","RUAL.ME","OMSH.ME","JNOS.ME","CBOM.ME","OFCB.ME","JNOSP.ME","NKHP.ME","KUBE.ME","KROTP.ME","TGKO.ME","KTSBP.ME","KTSB.ME","KRSB.ME","KRKO.ME","KMAZ.ME","KLSB.ME","KCHEP.ME","KCHE.ME","KBTK.ME","HIMC.ME","MSNG.ME","MRKZ.ME","MOTZ.ME","MGNT.ME","NVTK.ME","NSVZ.ME","NMTP.ME","NLMK.ME","ODVA.ME","PRIN.ME","OMZZP.ME","ZMZNP.ME","QIWI.ME","VLHZ.ME","URKA.ME","SKYC.ME","SBER.ME","ROSN.ME","RASP.ME","PHOR.ME","GAZP.ME","ALNU.ME","AFLT.ME","AFKS.ME","ZMZN.ME","ZHIV.ME","YRSL.ME","YRSB.ME","YASH.ME","YAKG.ME","VSYD.ME","VJGZP.ME","VJGZ.ME","VGSBP.ME","URKZ.ME","URFD.ME","TTLK.ME","TRMK.ME","SZPR.ME","STSBP.ME","SIBN.ME","SELL.ME","SARE.ME","SAGOP.ME","SAGO.ME","VRSB.ME","VRAO.ME","RU000A0JUSX7.ME","VSMO.ME","WTCMP.ME","YNDX.ME","YKEN.ME","YKENP.ME","YRSBP.ME","ZILL.ME","ZVEZ.ME","ABRD.ME","AESL.ME","AGRO.ME","AKRN.ME","RU000A0JUGA0.ME","SIBG.ME","ALRS.ME","RU000A0JUHS0.ME","ALBK.ME","AMEZ.ME","UWGN.ME","APTK.ME","AQUA.ME","ARSA.ME","ARMD.ME","ASSB.ME","AVAZP.ME","AVAN.ME","AVAZ.ME","BANEP.ME","BANE.ME","BISVP.ME","BGDE.ME","RU000A0JUP71.ME","RU000A0JUUF0.ME","BISV.ME","BLNG.ME","BSPB.ME","CHZN.ME","CHMF.ME","CHKZ.ME","GRNT.ME","CLSBP.ME","EPLN.ME","CLSB.ME","CNTL.ME","DASB.ME","DALM.ME","DGBZ.ME","DIOD.ME","DVEC.ME","DZRD.ME","RU000A0JUA37.ME","RU000A0JVT35.ME","RU000A0JUXF4.ME","ELTZ.ME","MISB.ME","ENRU.ME","EONR.ME","RU000A0JUBX3.ME","RU000A0JUW49.ME","RU000A0JUTA3.ME","FESH.ME","FEES.ME","FORTP.ME","GAZAP.ME","GAZC.ME","GAZS.ME","GAZA.ME","GAZT.ME","GCHE.ME","RU000A0JUSU3.ME","KGKCP.ME","RU000A0JVEZ0.ME","KGKC.ME","GMKN.ME","GRAZ.ME","GTPR.ME","GTLC.ME","HALS.ME","HIMCP.ME","RUSI.ME","IGST.ME","IGSTP.ME","IRKT.ME","IRAO.ME","IRGZ.ME","ISKJ.ME","RU000A0JTXM2.ME","RU000A0JVPL6.ME","POLY.ME","TRNFP.ME","UTSY.ME","PLSM.ME","TANL.ME","NFAZ.ME","RUSP.ME","KAZTP.ME","KAZT.ME","KBSB.ME","KMEZ.ME","KOGK.ME","KROT.ME","KRSG.ME","KRKN.ME","KRKNP.ME","KUZB.ME","KZOS.ME","KZOSP.ME","LKOH.ME","LNTA.ME","LNZLP.ME","LNZL.ME","LPSB.ME","LSRG.ME","LSNG.ME","LSNGP.ME","LVHK.ME","MAGE.ME","MFGS.ME","MFGSP.ME","MFON.ME","MGVM.ME","MGNZ.ME","MGTS.ME","MGTSP.ME","MMBM.ME","MOBB.ME","MORI.ME","MRKY.ME","MRKP.ME","MRKS.ME","MRKV.ME","MRKK.ME","MRKU.ME","MRKC.ME","MRSB.ME","MSST.ME","MSRS.ME","MSTT.ME","MTSS.ME","MTLR.ME","MTLRP.ME","MUGS.ME","MUGSP.ME","MVID.ME","NAUK.ME","NKNCP.ME","NKSH.ME","NKNC.ME","NNSBP.ME","NNSB.ME","TAER.ME","OGKB.ME","OPIN.ME","OSMP.ME","OTCP.ME","PHST.ME","PIKK.ME","PLZL.ME","PMSB.ME","PMSBP.ME","PRMB.ME","PRIM.ME","RODNP.ME","TASBP.ME","PSBR.ME","RU000A0JUQZ6.ME","RBCM.ME","RDRB.ME","RGSS.ME","RKKE.ME","RLMNP.ME","RLMN.ME","RNAV.ME","ROSB.ME","ROST.ME","ROLO.ME","RSTIP.ME","RSTI.ME","RTSBP.ME","RTSB.ME","RTKM.ME","RTGZ.ME","RTKMP.ME","RUALR.ME","CHMK.ME","STSB.ME","TATNP.ME","MAGN.ME","RU000A0JQ5X1.ME","TUCH.ME","VZRZP.ME","UNKL.ME","SNGSP.ME","SNGS.ME","PRFN.ME","UNAC.ME","VSYDP.ME","USBN.ME","TASB.ME","RZSB.ME","TATN.ME","SELG.ME","TORSP.ME","CHGZ.ME","TUZA.ME","PRTK.ME","VZRZ.ME","UCSS.ME","TNSE.ME","MAGEP.ME","BRZL.ME","VRAOP.ME","LIFE.ME","SAREP.ME","SYNG.ME","PAZA.ME","VTRS.ME","KRSBP.ME","VTBR.ME","WTCM.ME","KRKOP.ME","SELGP.ME","TRCN.ME","UTAR.ME","UTII.ME","SBERP.ME","TORS.ME","MISBP.ME","SVAV.ME","VTGK.ME","UKUZ.ME","CHEP.ME","CNTLP.ME","VDSB.ME","MERF.ME","VGSB.ME","RUGR.ME","GZE1R.RG","BRV1R.RG","LJM1R.RG","RJR1R.RG","GRZ1R.RG","GRD1R.RG","VEF1R.RG","SMA1R.RG","VNF1R.RG","KA11R.RG","SCM1R.RG","KCM1R.RG","BAL1R.RG","OLF1R.RG","TMA1R.RG","VSS1R.RG","DPK1R.RG","LSC1R.RG","RKB1R.RG","RER1R.RG","BTE1R.RG","RRR1R.RG","LOK1R.RG","RAR1R.RG","TKB1R.RG","LTT1R.RG","SAF1R.RG"]


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

