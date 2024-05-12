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
stocks = ["TRAN.BA","APBR.BA","CSCO.BA","COME.BA","BHIP.BA","RIGO.BA","LEDE.BA","GCLA.BA","APBRA.BA","ABX.BA","MOLI.BA","TGNO4.BA","PSUR.BA","KOFM.BA","HD.BA","FERR.BA","FNMA.BA","FRAN.BA","SAMI.BA","SEMI.BA","JMIN.BA","PATY.BA","KO.BA","KMB.BA","TS.BA","YPCZO.BA","NEM.BA","OYP19.BA","NKE.BA","BRIO6.BA","BRIO.BA","DIY0.BA","AY24.BA","AS17.BA","AGRO.BA","DICE.BA","OVO3P.BA","AO20.BA","AO17.BA","AF17.BA","OAEY1.BA","OVOP.BA","CTIO.BA","OIRY7.BA","TVPP.BA","CO17.BA","PMD18.BA","SNP.BA","QCOM.BA","QCC8O.BA","VALE.BA","TGLT.BA","T.BA","YPCNO.BA","UTX.BA","ERAR.BA","WMT.BA","DISN.BA","WFC.BA","XOM.BA","YPCPO.BA","BDED.BA","GJ17.BA","BPLD.BA","XNC4O.BA","XNC6O.BA","XNC5O.BA","XNC3O.BA","XNC2O.BA","PBJ21.BA","TSC10.BA","AUY.BA","YPFD.BA","YHOO.BA","IRSA.BA","DOME.BA","CRES.BA","YZC.BA","YCA5O.BA","YCA2O.BA","PATA.BA","YCA7O.BA","YCABO.BA","YCA4O.BA","YCA8O.BA","ESTR.BA","YPCUC.BA","YPCUO.BA","OIRX6.BA","YPCRO.BA","OIRX7.BA","YCA6O.BA","OYPF0.BA","YCAAO.BA","GARO.BA","AAPL.BA","AA17D.BA","AA17C.BA","AA.BA","AA17Z.BA","AA17.BA","AA17X.BA","ABT.BA","MBT.BA","BP.BA","AD16X.BA","AD16D.BA","AEN.BA","AF17D.BA","CS.BA","NVS.BA","SIEGY.BA","INAG.BA","VALO.BA","INTR.BA","BD2C9.BA","AIG.BA","BBO16.BA","AJ17X.BA","AJ17.BA","GOOGL.BA","MO.BA","AL16X.BA","ALUA.BA","AL16.BA","AXP.BA","AM20.BA","AMGN.BA","AM18X.BA","AM17.BA","AMX9.BA","BA-C.BA","AM20D.BA","AM17X.BA","AMX8.BA","AM18.BA","AMX9X.BA","DYCA.BA","AN18X.BA","AN18.BA","AN18D.BA","AO16D.BA","AO20D.BA","AO20C.BA","AO20X.BA","AO17X.BA","AO16X.BA","APSA.BA","PETR.BA","INTC.BA","IBM.BA","CARC.BA","CAPU.BA","C.BA","BPAT.BA","TRVV.BA","PEP.BA","POLL.BA","PG.BA","PESA.BA","PAMP.BA","MORI.BA","MMM.BA","MIRG.BA","HSBC.BA","GG.BA","GFI.BA","FIPL.BA","DGCU2.BA","CVX.BA","COLO.BA","BNG.BA","BMA.BA","BBRY.BA","CEPU.BA","CAT.BA","FMX.BA","TSM.BA","CX.BA","TSCH9.BA","BDC18.BA","AY16.BA","MRK.BA","FCX.BA","TI.BA","GRIM.BA","MVIA.BA","NDG21.BA","DD.BA","BUN16.BA","AVP.BA","EBAY.BA","PHG.BA","DICY.BA","MCD.BA","PUM21.BA","JPM.BA","NOKA.BA","INVJ.BA","OCR14.BA","OGZD.BA","CELU.BA","ORCL.BA","SNE.BA","GNCEO.BA","PAA0.BA","EDN.BA","TXN.BA","BMA-5.BA","EMC.BA","CECO2.BA","MOLI5.BA","FORM3.BA","CHL.BA","RNG21.BA","MPC7O.BA","BA.BA","FMCC.BA","MDC4O.BA","PARP.BA","MELI.BA","PTR.BA","TUCS1.BA","ERG16.BA","DEO.BA","BHP.BA","BBD.BA","PR15.BA","NGG.BA","VZ.BA","LONG.BA","PARY.BA","TECO2.BA","NF18.BA","BCS.BA","BNN16.BA","H04Y6.BA","PUO19.BA","MON.BA","TVPA.BA","ERD16.BA","TVPY.BA","BADER.BA","LMT.BA","PR13.BA","CL.BA","OEST.BA","BDC19.BA","GBAN.BA","BOLT.BA","INDU.BA","HMY.BA","OCK2P.BA","NORT6.BA","PFE.BA","BBV.BA","HPQ.BA","AUSO.BA","PARA.BA","BSBR.BA","SLB.BA","VOD.BA","PMO18.BA","REGE.BA","ERJ17.BA","DIA0.BA","AD16.BA","RDS.BA","TXR.BA","DICP.BA","IBN.BA","HMC.BA","BD6C6.BA","BC2N6.BA","BMY.BA","CUAP.BA","E.BA","METR.BA","JNJ.BA","BNN17.BA","UN.BA","GGAL.BA","TM.BA","BAO17.BA","MSFT.BA","TOT.BA","SBUX.BA","ROSE.BA","MTU.BA","GE.BA","CGPA2.BA","BDC20.BA","PAP0.BA","GSK.BA","DIP0.BA","TGSU2.BA","ESME.BA","GN10Q.BA","DICA.BA","ORAN.BA","AZN.BA","SAP.BA","CADO.BA","CAPX.BA","AS17X.BA","AS16X.BA","AY24X.BA","AY24C.BA","AY24D.BA","STD.BA","BARY1.BA","BCG16.BA","BCN16.BA","BD2C0.BA","BD4C6.BA","BDEDD.BA","BD7C6.BA","BARX1.BA","BDC16.BA","BD2C6.BA","BFCGO.BA","BFCHO.BA","BFCBO.BA","BHCDO.BA","BHCXO.BA","TSC1O.BA","BNL17.BA","BNM17.BA","BNJ16.BA","BPLE.BA","BPMD.BA","BP21D.BA","BPLDD.BA","BP18.BA","BP28.BA","BP21.BA","BR00P.BA","IRCP.BA","BWS6V.BA","BY08C.BA","CEDI.BA","CG27C.BA","CG26B.BA","CG27B.BA","CG26C.BA","CLCEO.BA","CL4OD.BA","CLC4O.BA","CN15Q.BA","CN16Q.BA","CPC6O.BA","CPC2O.BA","CPC4O.BA","CSBNO.BA","CS9JO.BA","CSBMO.BA","CS8HO.BA","CUAPX.BA","CZ12B.BA","DICYC.BA","DICAX.BA","DICAC.BA","DIA0D.BA","DICAD.BA","DIE0.BA","DICPX.BA","DICYD.BA","ER2D6.BA","REP.BA","TEF.BA","GJ17C.BA","GJ17D.BA","GL08Q.BA","GLW.BA","GL08C.BA","LB2A6.BA","LCY16.BA","LDC3O.BA","LEY16.BA","LG72O.BA","MBCOO.BA","MDC6O.BA","ML09B.BA","ML10B.BA","MTALO.BA","MTAUO.BA","NF18X.BA","NF18C.BA","NJC3O.BA","NLC2V.BA","NO20.BA","NRH2.BA","NS00A.BA","NVC3O.BA","OAOY2.BA","OCEY1.BA","ODNY9.BA","OGBY1.BA","ONY13.BA","OPNY1.BA","OROY5.BA","OROY4.BA","PAC.BA","PARAC.BA","PARAX.BA","PAA0D.BA","PARE.BA","PAY0.BA","PARAD.BA","PBM24.BA","PNC7O.BA","PNC8O.BA","PNC4O.BA","PR15X.BA","RAC2O.BA","RCC8O.BA","RICLO.BA","RICGO.BA","RIK4O.BA","RICMO.BA","RIK2O.BA","RIK2P.BA","RIH2P.BA","RIH1O.BA","RICFO.BA","RIK1O.BA","RIJ2P.BA","RIK3O.BA","RIH2O.BA","RICOO.BA","RIJ1O.BA","RICNO.BA","RNG22.BA","SCCO.BA","SD13B.BA","SNS1O.BA","SSC5V.BA","SV3GO.BA","TSC11.BA","TSC12.BA","TSCH7.BA","TSCH8.BA","TUBB1.BA","TVPYD.BA","TVY0.BA","TVPPX.BA","TVPYX.BA","TVPE.BA","VC05A.BA","VC03B.BA","BAE17.BA","COLOX.BA","PARPX.BA","PRO9.BA","SARH.BA","TRCNO.BA"]

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

