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
stocks = ["ASURB.MX","WALMEX.MX","MTN.MX","GOOG.MX","AMXL.MX","AAPL.MX","LALAB.MX","AZTECACPO.MX","ALFAA.MX","ADSK.MX","BIMBOA.MX","GRUMAB.MX","FEMSAUBD.MX","DIS.MX","KOFL.MX","ELEKTRA.MX","RDSB.MX","GMEXICOB.MX","CEMEXCPO.MX","RDSA.MX","PINFRA.MX","MEXCHEM.MX","MASECAB.MX","LABB.MX","ICHB.MX","ICA.MX","HOMEX.MX","HERDEZ.MX","HD.MX","GPH1.MX","GIGANTE.MX","GBMO.MX","FIBRAMQ12.MX","CMOCTEZ.MX","CHDRAUIB.MX","BAFARB.MX","AMD.MX","VALUEGFO.MX","SIMECB.MX","SIEN.MX","RCENTROA.MX","OMAB.MX","ODP.MX","LIVEPOL1.MX","INVEXA.MX","IDEALB-1.MX","HOGARB.MX","GMD.MX","GFNORTEO.MX","GEOB.MX","GCARSOA1.MX","FINN13.MX","FINAMEXO.MX","NEMAKA.MX","XOM.MX","PRU.MX","FSLR.MX","KHC.MX","CVS.MX","BHI.MX","JPM.MX","JNJ.MX","JCP.MX","GLENN.MX","STJN.MX","JCI.MX","JAH.MX","DECN.MX","JDN.MX","SINAN.MX","KO.MX","KUOA.MX","SLBN.MX","MMM.MX","SITESL.MX","NFLX.MX","TELN.MX","SIDN.MX","RIGN.MX","NVSN.MX","NVDA.MX","NOKN.MX","NKE.MX","POTN.MX","ORCL.MX","CULTIBAB.MX","BAC.MX","HOTEL.MX","TEMGBIAA.MX","ORN.MX","PINFRAL.MX","OHLMEX.MX","QSRN.MX","QIHUN.MX","QCOM.MX","Q.MX","CREAL.MX","SNEN.MX","TWX.MX","TOTN.MX","COST.MX","YHOO.MX","X.MX","VALEN.MX","UAL.MX","UA.MX","SCCO.MX","INTC.MX","GPS.MX","GILD.MX","CSCO.MX","CMG.MX","C.MX","BIDUN.MX","BCSN.MX","BBY.MX","BBBY.MX","BA.MX","ATVI.MX","AMZN.MX","ALUN.MX","AIG.MX","ABBN.MX","AA.MX","WU.MX","WHR.MX","V.MX","UTX.MX","ULN.MX","TWTR.MX","TSO.MX","TSLA.MX","TRV.MX","TMN.MX","TIN.MX","TGT.MX","TEVAN.MX","SYTN.MX","STT.MX","SNDK.MX","RGC.MX","PUKN.MX","PLD.MX","PHM.MX","PFE.MX","PBRN.MX","MU.MX","MS.MX","MON.MX","MO.MX","MGM.MX","MELIN.MX","MCD.MX","MA.MX","LYGN.MX","IP.MX","ILMN.MX","HYUDN.MX","GS.MX","GOOGL.MX","GM.MX","GGBN.MX","FCFS.MX","EN.MX","EMR.MX","EBAY.MX","DLTR.MX","DISH.MX","CVX.MX","CPLN.MX","COP.MX","CL.MX","CHK.MX","CBPX.MX","CAR.MX","BSBRN.MX","BRFSN.MX","BMY.MX","BBDN.MX","AZNN.MX","AXP.MX","AMGN.MX","VRXN.MX","VASCONI.MX","BOLSAA.MX","BBDBN.MX","VPKN.MX","SAVBMX1B.MX","BBVA.MX","SLN.MX","VESTA.MX","DGN.MX","BOKAN.MX","WMT.MX","WFTN.MX","WINN.MX","WEIRN.MX","WRLD.MX","AXTELCPO.MX","XLNX.MX","AGNN.MX","MCMN.MX","YOKUN.MX","BMEN.MX","YPFN.MX","GRAMN.MX","YGEN.MX","RYAN.MX","ZINCQ.MX","JMATN.MX","AAL.MX","AAUN.MX","ABT.MX","ABEVN.MX","ABXN.MX","0R87N.MX","ABBV.MX","ABI.MX","ACI.MX","ACCN.MX","ACOFN.MX","ACTIPATB.MX","ACTIPATA.MX","ACHN.MX","ACTINVRB.MX","AC.MX","FIBRAHD15.MX","ACXN.MX","HISN.MX","ACCELSAB.MX","ACNN.MX","ACTIPATFF.MX","ADM.MX","ADBE.MX","FPAFYN.MX","EDUN.MX","SHPGN.MX","CRHN.MX","CEON.MX","STON.MX","ADSN.MX","SIMON.MX","MRN.MX","CHTN.MX","CTRPN.MX","LFCN.MX","PNGAYN.MX","DRDN.MX","LKODN.MX","AEGN.MX","NBGGYN.MX","CNCON.MX","VIPSN.MX","JKSN.MX","TCEHYN.MX","CCUN.MX","CHUN.MX","ECN.MX","BAKN.MX","ORANN.MX","ARMHN.MX","ASXN.MX","VIVN.MX","JASON.MX","PBRAN.MX","OIBRN.MX","ENIN.MX","HQCLN.MX","NTTN.MX","NTESN.MX","SPILN.MX","SNPN.MX","SOLN.MX","TSLN.MX","KBN.MX","SSLN.MX","SBSN.MX","MTXN.MX","GAPB.MX","AEROMEX.MX","DBN.MX","AGUA.MX","AGKN.MX","AGLN.MX","AGNC.MX","CSN.MX","DAIN.MX","UBSN.MX","AHN.MX","DAL.MX","LUV.MX","AIN.MX","JBLU.MX","ATSG.MX","GOLN.MX","AKS.MX","AKEN.MX","ALSEA.MX","ALLEN.MX","ALSN.MX","ALPEKA.MX","BABAN.MX","ALVN.MX","AMXA.MX","PASAB.MX","AMFWN.MX","APH.MX","VRSK.MX","DWA.MX","ANTM.MX","APC.MX","LLY.MX","APOL.MX","APOLO10E.MX","APPSN.MX","APA.MX","ARTCK13-2.MX","ARTCK13.MX","ARYNN.MX","ARISTOSA.MX","ARA.MX","ARCON.MX","ASMLN.MX","ASCN.MX","T.MX","EBON.MX","AVN.MX","AVP.MX","AXBN.MX","AXAN.MX","AXIAN.MX","SAN.MX","GFREGIOO.MX","BNS.MX","DANHOS13.MX","USB.MX","BACHOCOB.MX","BBRYN.MX","BCHN.MX","BEVIDESB.MX","BEVIDESA.MX","BRKB.MX","INVEXCOBE.MX","BKGN.MX","INVEXCOBF.MX","BG.MX","BHPN.MX","BIIB.MX","CBPO.MX","PAPPEL.MX","FUNO11.MX","FIHO12.MX","FIBRAPL14.MX","BKIAN.MX","BLK.MX","BLD.MX","BMWM5N.MX","NCLHN.MX","INVEXCOBM.MX","BAPN.MX","BNPN.MX","BNRN.MX","BNN.MX","DB1N.MX","WBA.MX","BOSSN.MX","BPN.MX","CST.MX","BTN.MX","BURL.MX","BVNN.MX","IBM.MX","BXLT.MX","PROCORPA.MX","TCPTFN.MX","PROCORPB.MX","CBDN.MX","CBKN.MX","CC.MX","CCRN.MX","CDIN.MX","CERAMICB.MX","CLNXN.MX","CELG.MX","FBRN.MX","CERAMICD.MX","GCC.MX","FOX.MX","CFHSN.MX","CFRIN.MX","CGGN.MX","DOW.MX","LISPN.MX","CHS.MX","SCHW.MX","ROGN.MX","CIDMEGA.MX","CIEB.MX","KSU.MX","CTXS.MX","CIEAN.MX","HCITY.MX","CIGN.MX","FSHOP13.MX","TERRA13.MX","KIMBERB.MX","KIMBERA.MX","CLF.MX","CMRB.MX","CMCSA.MX","CMCN.MX","PROF-CPA1.MX","TEAKCPO.MX","LACOMERUBC.MX","LACOMERUB.MX","CPIN.MX","CPAN.MX","PROF-CPA2.MX","PROF-CPB2.MX","RCL.MX","NTE-IB1C.MX","CRM.MX","CTSH.MX","CONVERA.MX","FEMSAUB.MX","GFAMSAA.MX","VITROCPO.MX","SORIANAB.MX","SAREB.MX","EDOARDOB.MX","FINDEP.MX","COMERCIUB.MX","DINEB.MX","COMERCIUBC.MX","CABLECPO.MX","GFINBURO.MX","VITROA.MX","MAXCOMCPO.MX","MEDICAB.MX","URBI.MX","GISSAA.MX","AUTLANB.MX","SANMEXB.MX","COLLADO.MX","GPROFUT.MX","DINEA.MX","LAMOSA.MX","MINSAB.MX","MEGACPO.MX","HILASALA.MX","POCHTECB.MX","FRAGUAB.MX","CYDSASAA.MX","GFINTERO.MX","POSADASA.MX","SAB.MX","KUOB.MX","DATA.MX","DSYN.MX","DHR.MX","DD.MX","DDD.MX","FMEN.MX","DIDAN.MX","DO.MX","DEON.MX","WDC.MX","0QBON.MX","0JN9N.MX","DNOW.MX","DPWN.MX","RDYN.MX","DTEN.MX","DUFNN.MX","DVN.MX","STLD.MX","GD.MX","EBRON.MX","ECL.MX","EIN.MX","LIVEPOLC-1.MX","REEN.MX","EL.MX","ELEMENT.MX","GE.MX","SUN.MX","ELPN.MX","ERJN.MX","EMC.MX","ENELN.MX","SN.MX","ENGI.MX","EOANN.MX","ERICN.MX","CAFEN.MX","ITXN.MX","ESNTN.MX","COLN.MX","FAEN.MX","MRLN.MX","GRFPN.MX","ESRX.MX","IBEN.MX","TREN.MX","VISCN.MX","FERN.MX","MAPN.MX","TUBN.MX","POPN.MX","GCON.MX","REPSN.MX","IDRN.MX","OHLN.MX","GASN.MX","ENGN.MX","NHHN.MX","ETLN.MX","EVR.MX","HEEN.MX","PREN.MX","EXON.MX","EXC.MX","FB.MX","FFHN.MX","WFC.MX","FCAN.MX","FCX.MX","FDX.MX","RACEN.MX","FFIV.MX","FGEN.MX","FHIPO14.MX","GFMULTIO.MX","UNIFINA.MX","PNC.MX","COF.MX","FLEXN.MX","FLR.MX","FMTY14.MX","FIG.MX","WFM.MX","F.MX","FVIN.MX","MFRISCOA-1.MX","KERN.MX","TECN.MX","GLEN.MX","UGN.MX","MLN.MX","PUBN.MX","VALOFN.MX","COG.MX","GFAN.MX","GALPN.MX","PG.MX","GASIN.MX","IT.MX","KGFN.MX","FRES.MX","TSCON.MX","GBX.MX","MGGTN.MX","SMSNN.MX","GENTERA.MX","GENSEG.MX","GNW.MX","GGAN.MX","GGN.MX","GICSAB.MX","GIVNN.MX","GSKN.MX","HTZ.MX","GLW.MX","GNP.MX","GT.MX","TMMA.MX","TLEVISACPO.MX","GSANBORB-1.MX","HAL.MX","HBCN.MX","HEIN.MX","HPQ.MX","RMSN.MX","HGGN.MX","OPK.MX","HILASALB.MX","RH.MX","SCHPN.MX","HMCN.MX","HON.MX","HPE.MX","HSBCAHOA.MX","IENOVA.MX","MDTN.MX","SSYSN.MX","CALLN.MX","CHKPN.MX","IMTN.MX","IM.MX","IPON.MX","ISPN.MX","UCGN.MX","ITUBN.MX","SFLN.MX","PIAN.MX","SRGN.MX","JAVER.MX","KBR.MX","KBH.MX","KGXN.MX","KMX.MX","KPNN.MX","KSS.MX","UTSI.MX","MANUN.MX","LVS.MX","LB.MX","LEN.MX","LRN.MX","LEA.MX","LUK.MX","LMT.MX","LNKD.MX","TS.MX","LUPEN.MX","STAN.MX","MCN.MX","LYBN.MX","MPC.MX","MLM.MX","TSMN.MX","MRO.MX","MBTN.MX","MCK.MX","MUX.MX","MD.MX","MDLZ.MX","MRK.MX","MTG.MX","MGAN.MX","MSFT.MX","MKSN.MX","MKL.MX","MOS.MX","CHLN.MX","MONEXB.MX","MSI.MX","NSANYN.MX","MRWN.MX","MTUN.MX","MUV2N.MX","SITESA.MX","SBRAICP1.MX","INVEXCOA.MX","MIFIPCB.MX","INTERS2A.MX","VOLARA.MX","PE&OLES.MX","SBRAICPA2.MX","RLHA.MX","VECTMDA.MX","INTERS2M.MX","VALOR1FA.MX","INBUREXA.MX","CADUA.MX","INTERS2B.MX","SBRAICPB2.MX","INBUREXB.MX","SAVBMX1A.MX","VALUEV6B.MX","RASSINIA.MX","SPORTS.MX","VALOR3MB.MX","PV.MX","VALUEV6A.MX","RASSINICPO.MX","MIFIPCA.MX","NTE+USAA.MX","VALOR3MA.MX","VALOR1FB.MX","NOV.MX","NESNN.MX","NGN.MX","RANDN.MX","NOEJN.MX","NVON.MX","NUE.MX","INGN.MX","RYN.MX","ORLY.MX","TSUN.MX","UNP.MX","UGPN.MX","UPS.MX","PCLN.MX","PFCN.MX","PTRN.MX","PEP.MX","REGN.MX","VRTX.MX","PII.MX","PKXN.MX","PPG.MX","PSMT.MX","SEMN.MX","PYPL.MX","RDN.MX","RBN.MX","RCFN.MX","RION.MX","ROST.MX","SAPN.MX","SNYN.MX","SBUX.MX","SBRYN.MX","TMO.MX","SCTY.MX","SHW.MX","SKYN.MX","S.MX","SXSN.MX","SRE.MX","SRENN.MX","SSE.MX","SWC.MX","STZ.MX","SVU.MX","SVLCN.MX","UHRN.MX","SY1N.MX","TCKN.MX","TIF.MX","TIME.MX","TJX.MX","TXN.MX","TX.MX","TXT.MX","UNH.MX","VLO.MX","VRTV.MX","VZ.MX","VODN.MX","VOW3N.MX","WRK.MX","WTBN.MX","WITN.MX","WYNN.MX","ADPN.MX","BASN.MX","BAX.MX","BAYNN.MX","CAJN.MX","CNEN.MX","CAN.MX","CAT.MX","COO.MX","FRC.MX","FISV.MX","TRN.MX","INTU.MX","LINN.MX","M.MX","MAS.MX","MET.MX","PLL.MX","TEFN.MX","INCHN.MX"]


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

