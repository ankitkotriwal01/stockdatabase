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
stocks = ["ATLN.VX","ROG.VX","FHZN.SW","AAPL.SW","RO.SW","AMS.SW","ABBN.VX","CSGN.VX","VW-V.SW","DUFN.SW","BCGE.SW","VWS.SW","OXDEX.SW","OXDB1.SW","OSR.SW","KU2.SW","HEN.SW","EVE.SW","ZURN.VX","LONN.VX","GEBN.VX","UBSG.VX","GIVN.VX","USIN.SW","TEMN.SW","ROL.SW","MIKN.SW","BALN.VX","ALLN.SW","YPSN.SW","VATN.SW","VAHN.SW","UBXN.SW","SLOG.SW","STMN.SW","SOON.VX","SMET.SW","SLHN.VX","SFZN.SW","SCHPE.SW","SCHP.VX","SANN.SW","BAER.VX","NIN.SW","JEN.SW","JFN.SW","JKS.SW","BCJ.SW","TOSH.SW","JPM.SW","GRKP.SW","SGKN.SW","BLKB.SW","OXKBC.SW","SDF.SW","GMCR.SW","SYNN.VX","NESN.VX","NOVN.VX","SREN.VX","GALN.VX","CFR.VX","STL.SW","OTI.SW","RY.SW","O2D.SW","OXCON.SW","POST.SW","OXSY1.SW","OXDUE.SW","OXLXS.SW","OXCOP.SW","ORCL.SW","QCOM.SW","QIHU.SW","QIA.SW","QSC.SW","SGSN.VX","SCMN.VX","UHR.VX","SCTY.SW","PFE.SW","MDLZ.SW","GOOGL.SW","CL.SW","BHI.SW","VPB.SW","EPH.SW","VALE.SW","GSV.SW","VFC.SW","VOE.SW","VIB3.SW","NEWN.SW","VW.SW","VZ.SW","DRW3.SW","NEV.SW","KORS.SW","VILN.SW","HEN3.SW","RWE3.SW","PAH3.SW","BCVN.SW","PWTN.SW","SLW.SW","WMN.SW","WBA.SW","DWNI.SW","WDI.SW","OXGWI1.SW","GWI1.SW","WKBN.SW","OXO1BC.SW","O1BC.SW","XRX.SW","XOM.SW","XONE.SW","YRI.SW","YHOO.SW","YAR.SW","YELP.SW","YY.SW","MY.SW","YUM.SW","YGE.SW","ZWM.SW","ZIL2.SW","ZAG.SW","ZAL.SW","ZEHN.SW","ZBH.SW","GOLI.SW","ZG.SW","AFX.SW","OXAFX.SW","ZC.SW","ZMS.SW","TIM.SW","ZNGA.SW","ZUGN.SW","ZUBN.SW","METN.SW","OXZO1.SW","ZO1.SW","ARL.SW","AAM.SW","AAD.SW","AA.SW","ABX.SW","ABBV.SW","ABBNE.SW","ABF.SW","ABT.SW","ANF.SW","ACUN.SW","ATLNE.SW","AC.SW","ACA.SW","AMD.SW","ADBE.SW","BABA.SW","VJET.SW","TTM.SW","DANG.SW","HQCL.SW","BIDU.SW","ADXN.SW","RESOL.SW","ADEN.VX","ADS.SW","TEVA.SW","JASO.SW","ADENE.SW","NTES.SW","ADVN.SW","TSL.SW","AEVS.SW","AEM.SW","MTX.SW","AGN.SW","AFGN.SW","AF.SW","STLN.SW","IMPN.SW","BION.SW","TECN.SW","SWTQ.SW","SPSN.SW","PM.SW","LISN.SW","LIFE.SW","IPS.SW","INRN.SW","GBMN.SW","GAV.SW","GAM.SW","CYTN.SW","BSLN.SW","BARN.SW","ALSN.SW","DCN.SW","CPGN.SW","SAHN.SW","DESN.SW","ALPH.SW","MOBN.SW","SCHN.SW","CLTN.SW","BIOEE.SW","ALPNE.SW","PSPN.SW","LUKN.SW","EMSN.SW","IFCN.SW","STGN.SW","ELMN.SW","CALN.SW","SUN.SW","MCHN.SW","ORON.SW","MBTN.SW","EMMN.SW","CASNE.SW","AGFB.SW","TIBN.SW","CLXN.SW","HUBN.SW","VBSN.SW","AGS.SW","ESUN.SW","UHRN.SW","BC.SW","GUR.SW","BANB.SW","CPHN.SW","RIEN.SW","PEL.SW","BRKN.SW","TOHN.SW","BBN.SW","PAXN.SW","UHRNE.SW","MASN.SW","CPEN.SW","ALPN.SW","EDHN.SW","VET.SW","BEAN.SW","REPI.SW","LLB.SW","VONN.SW","TAMN.SW","BAYN.SW","PEHN.SW","ALTN.SW","LOHN.SW","MYRN.SW","BLIN.SW","IHSN.SW","BCHN.SW","LISP.SW","BUCN.SW","HELN.SW","ASCN.SW","EEII.SW","DAE.SW","VLRT.SW","LINN.SW","OFN.SW","FORN.SW","REPP.SW","WIE.SW","COM.SW","BVZN.SW","CASN.SW","SHPNE.SW","SIN.SW","FORNE.SW","STRN.SW","COTN.SW","KUNN.SW","KARN.SW","GATE.SW","VZN.SW","HUE.SW","WARN.SW","KOMN.SW","VALN.SW","AIXA.SW","AI.SW","AIRN.SW","DAL.SW","AIG.SW","AIRE.SW","AIR.SW","AKZ.SW","ALU.SW","ALO.SW","MO.SW","ALV.SW","AOX.SW","ALXN.SW","AMGN.SW","PAA.SW","BATS.SW","AXP.SW","BAC.SW","AMZN.SW","ANDR.SW","LLY.SW","SLB.SW","AU.SW","APGN.SW","MT.SW","SAZ.SW","ARYN.VX","ARIA.SW","ADM.SW","CADN.SW","ARM.SW","UA.SW","DIC.SW","ASM.SW","ASML.SW","AZN.SW","ASG.SW","SBO.SW","EBS.SW","VER.SW","OMV.SW","BWO.SW","IIA.SW","RBI.SW","RHI.SW","ROS.SW","ATS.SW","MMK.SW","CWI.SW","O2C.SW","T.SW","TKA.SW","LNZ.SW","CS.SW","SPR.SW","BPDG.SW","BA.SW","BALNE.SW","BAX.SW","BB.SW","BBDB.SW","BBY.SW","BC8.SW","BDX.SW","BDT.SW","DBAN.SW","PROX.SW","BEKN.SW","BPOST.SW","BEI.SW","OXBEI.SW","BELL.SW","BLT.SW","BHP.SW","HEB.SW","OXGBF.SW","GBF.SW","BIIB.SW","BIO3.SW","SGMO.SW","SBS.SW","BKW.SW","CBA.SW","RBS.SW","BLK.SW","BLD.SW","BX.SW","BMY.SW","BMPS.SW","OXBMW.SW","BMW3.SW","BMW.SW","BNR.SW","BNP.SW","OXBNP.SW","BOBNN.SW","BVB.SW","BOSS.SW","EN.SW","DB1.SW","BOSN.SW","BP.SW","BSKP.SW","BTO.SW","BVN.SW","BYW6.SW","CPENE.SW","CAI.SW","CARLB.SW","CAP.SW","PTK.SW","CCO.SW","CDI.SW","CDE.SW","CMBN.SW","SCAB.SW","CWC.SW","UN.SW","CELG.SW","CEV.SW","CERN.SW","CFT.SW","CGG.SW","LEON.SW","HREN.SW","EFGN.SW","DOKA.SW","CHD.SW","SFPF1.SW","WIHN.SW","LOGN.SW","PLAN.SW","KNIN.VX","PEDU.SW","SIK.VX","PRFN.SW","GMI.SW","30318277.SW","SYNNE.SW","PUBN.SW","UBSNE.SW","HBMN.SW","SRCG.SW","OERL.SW","PGHN.SW","CICN.SW","DOW.SW","SIAT1.SW","CVX.SW","NBEN.SW","SCHNE.SW","SREA1.SW","RSPF1.SW","SQN.SW","SGSNE.SW","HBLN.SW","C.SW","CIE.SW","CSCO.SW","CLN.VX","CMCSA.SW","CNC.SW","SEV.SW","CRM.SW","CSIQ.SW","EVD.SW","CTSH.SW","OXEVD.SW","DAN.SW","DAI.SW","DHR.SW","DSY.SW","DBK.SW","DDD.SW","DD.SW","CONT.SW","HD.SW","OXSAP.SW","COMPG.SW","OXNOEJ.SW","PUM.SW","TLX.SW","TEG.SW","NEMA.SW","MEO.SW","DGC.SW","DG.SW","DIS.SW","COLOB.SW","NZYMB.SW","DKSH.SW","PNDORA.SW","NOVOB.SW","GIL.SW","PMOX.SW","DPW.SW","DRI.SW","HDD.SW","DSM.SW","OXLHA.SW","DTE.SW","LHA.SW","DUFN.VX","RDSA.SW","DUE.SW","EBAY.SW","EDP.SW","RLD.SW","EDR.SW","EW.SW","EDF.SW","EI.SW","SNE.SW","LPK.SW","GE.SW","ELD.SW","EMR.SW","EMC.SW","FCEL.SW","NUS.SW","EOAN.SW","EO.SW","ERF.SW","ERICB.SW","ESRX.SW","GET.SW","DEQ.SW","EVT.SW","EVK.SW","HLEE.SW","EXPE.SW","FB.SW","WFC.SW","FCX.SW","FDX.SW","FEYE.SW","RACE.SW","FTON.SW","FFI.SW","FMS.SW","NOKIA.SW","FME.SW","FNV.SW","FNTN.SW","FVI.SW","WFM.SW","F.SW","FPE3.SW","FP.SW","MC.SW","ML.SW","MMB.SW","OXFME.SW","KER.SW","FR.SW","GOE.SW","LOCAL.SW","RI.SW","FRA.SW","KN.SW","UBI.SW","ENGI.SW","POM.SW","VIE.SW","ING.SW","SAF.SW","FRE.SW","FSLR.SW","GFMN.SW","GAMEE.SW","GFJ.SW","MRW.SW","TCG.SW","SRP.SW","RGSE.SW","OXG1A.SW","G1A.SW","GIS.SW","GEBNE.SW","GMT.SW","OXGXI.SW","GLE.SW","HTM.SW","GM.SW","GXI.SW","FI-N.SW","GFK.SW","GILD.SW","GLJ.SW","SBB.SW","GLUU.SW","GSK.SW","GLW.SW","GLKBN.SW","GMM.SW","GPRO.SW","GT.SW","KG.SW","G.SW","GOB.SW","GS.SW","PGM.SW","GPR.SW","HAL.SW","HAB.SW","HOG.SW","HNR1.SW","HBMNE.SW","HBH3.SW","KHC.SW","OXHEN3.SW","OXHEI.SW","HL.SW","HEID.SW","HEI.SW","HMB.SW","HHFA.SW","HIAG.SW","LEN.SW","CHT.SW","SOONE.SW","ISN.SW","OXKD8.SW","HOCN.SW","TTI.SW","MOZN.SW","ONVO.SW","SLT.SW","INH.SW","HPQ.SW","HYG.SW","NHY.SW","IMG.SW","IBM.SW","MDT.SW","IFX.SW","SHLTN.SW","LEG.SW","P1Z.SW","IMB.SW","IONS.SW","IPH.SW","IRBT.SW","ISP.SW","ISRG.SW","TIT.SW","NWRN.SW","SPM.SW","UCG.SW","SKIN.SW","PRP.SW","ENI.SW","IT.SW","ENEL.SW","JCP.SW","OXJEN.SW","JNJ.SW","SOFB.SW","SONC.SW","MAELI.SW","SHA.SW","TOYMO.SW","JUNGH.SW","KNDI.SW","KBC.SW","TKBP.SW","KCO.SW","KGX.SW","KPO.SW","KO.SW","KRN.SW","OXSDFG.SW","KUD.SW","KWS.SW","LXS.SW","LVS.SW","LMN.SW","LHN.VX","LEO.SW","LECN.SW","LEHN.SW","OXLING.SW","LLOY.SW","LMT.SW","LNKD.SW","COPN.SW","SFQ.SW","RTL.SW","MAN.SW","MCD.SW","MCP.SW","NCM.SW","NEM.SW","MLP.SW","MMM.SW","TSLA.SW","MOLN.SW","MOR.SW","PMI.SW","MS.SW","MRK.SW","MSFT.SW","MUV2.SW","MU.SW","MYL1.SW","SNBN.SW","NDA.SW","NDX1.SW","NDASEK.SW","NESNE.SW","WAC.SW","NFLX.SW","NKE.SW","NIHN.SW","WIN.SW","PHI.SW","INO.SW","TMO.SW","RDN.SW","PN6.SW","SBM.SW","NOEJ.SW","TEL.SW","NOVNEE.SW","NVDA.SW","ODHN.SW","OR.SW","ORA.SW","ORMP.SW","OXDTE.SW","OXADS.SW","OXDPW.SW","OXMRK.SW","OXRWE.SW","OXDBK.SW","OXFNTN.SW","OXEOAN.SW","OXFIE.SW","UNP.SW","UPS.SW","PCLN.SW","PEP.SW","WPL.SW","UG.SW","PEAN.SW","PFV.SW","PG.SW","VRTX.SW","REGN.SW","VRX.SW","PLUG.SW","PSEC.SW","PSM.SW","PSAN.SW","PUB.SW","PYPL.SW","RAA.SW","RB.SW","RCO.SW","RHK.SW","RHM.SW","RIO.SW","RIOP.SW","RIGN.SW","RNO.SW","RSTI.SW","RUS.SW","RWE.SW","SAX.SW","SNDK.SW","SBUX.SW","SCZ.SW","SCR.SW","TFS.SW","SFPN.SW","SFSN.SW","SGL.SW","SW1.SW","SSO.SW","SIX2.SW","SVM.SW","SW.SW","S92.SW","SOW.SW","SWVK.SW","SPLS.SW","SRT3.SW","SYK.SW","CAS.SW","SZU.SW","SUR.SW","SU.SW","SPWR.SW","SWEDA.SW","UHRE.SW","SY1.SW","SYNNEE.SW","SZG.SW","THO.SW","TTK.SW","TXN.SW","TK.SW","TWX.SW","TLSN.SW","TMUS.SW","TRV.SW","TRIP.SW","TSCO.SW","TUI1.SW","TWTR.SW","UIS.SW","UL.SW","UNH.SW","UTDI.SW","GRPN.SW","UTX.SW","VLA.SW","VK.SW","VCH.SW","VIV.SW","V.SW","VNA.SW","VOS.SW","VOD.SW","WCH.SW","WMT.SW","WYNN.SW","AUTN.SW","BAP.SW","BARC.SW","BAS.SW","B5A.SW","COK.SW","CA.SW","CAT.SW","COP.SW","CON.SW","DE.SW","DEZ.SW","ENPH.SW","FIE.SW","HOT.SW","INVN.SW","LIN.SW","M5Z.SW","MA.SW","MER.SW","PARG.SW","SPCE.SW","SAN.SW","SAP.SW","SPEX.SW","SPLK.SW","COMD.SW","INTC.SW"]


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

