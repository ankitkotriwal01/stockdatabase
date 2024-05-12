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
stocks = ["ALU.PA","AI.PA","AIR.PA","CS.PA","ALO.PA","AC.PA","AF.PA","ALEHT.PA","SIPH.PA","OSI.PA","MT.PA","CAFO.PA","RMS.PA","MLMAB.PA","CDA.PA","ATO.PA","ATA.PA","ALT.PA","ALOCT.PA","ALMDG.PA","ALAST.PA","ADP.PA","ZC.PA","XIL.PA","BNP.PA","BN.PA","BAIN.PA","EN.PA","ML.PA","DSY.PA","DP.PA","EDF.PA","SMTPC.PA","MLFER.PA","EDL.PA","TAM.PA","MLMAI.PA","FDR.PA","DVT.PA","DPT.PA","DGM.PA","DBV.PA","CBSM.PA","BSD.PA","ODET.PA","MLTRA.PA","MLTED.PA","MLSHD.PA","MLNV.PA","MLLEM.PA","MLHK.PA","MLEAU.PA","MLDAM.PA","MLCMB.PA","MLCFM.PA","MALA.PA","HDP.PA","GUYD.PA","FDL.PA","SEV.PA","ERF.PA","EO.PA","EI.PA","CBE.PA","SU.PA","ERSC.PA","ENGI.PA","ELIOR.PA","ECP.PA","VIE.PA","UBI.PA","SESL.PA","RF.PA","GPE.PA","FGR.PA","ES.PA","ERYP.PA","EOS.PA","EKI.PA","EDEN.PA","ALSAS.PA","ALGEM.PA","ALESK.PA","MLCVG.PA","PUB.PA","OR.PA","SAN.PA","SAFT.PA","SAF.PA","GLE.PA","CRTO.PA","VIV.PA","SOI.PA","VRAP.PA","UL.PA","TKTT.PA","TCH.PA","SOP.PA","QUA.PA","MC.PA","MAU.PA","ILD.PA","HO.PA","FR.PA","FP.PA","CAF.PA","VK.PA","VIRP.PA","VAC.PA","UG.PA","THEP.PA","TES.PA","SX.PA","SW.PA","STAL.PA","SGO.PA","RXL.PA","RI.PA","RCO.PA","PARRO.PA","ORA.PA","NEO.PA","MLSML.PA","MGIC.PA","KER.PA","ITXT.PA","ICAD.PA","HIM.PA","HBW.PA","HAV.PA","GDS.PA","FLY.PA","FLE.PA","FII.PA","COX.PA","CAP.PA","CA.PA","BVI.PA","BB.PA","VRNL.PA","TRI.PA","TOUP.PA","TER.PA","TEC.PA","SY.PA","SWP.PA","STF.PA","SOA.PA","SEC.PA","SBT.PA","RNO.PA","QTE.PA","PIX.PA","PIG.PA","OPN.PA","NK.PA","NANO.PA","MON.PA","MMT.PA","MLSTR.PA","MLSIM.PA","MLRAM.PA","MLNOV.PA","MLHBB.PA","MLCNT.PA","MLCET.PA","MFG.PA","MF.PA","MERY.PA","MED.PA","MAGIS.PA","LBON.PA","LACR.PA","KN.PA","JBOG.PA","ITE.PA","IPS.PA","IPN.PA","IPH.PA","IMPL.PA","IML.PA","HONV.PA","GTT.PA","GFT.PA","GFI.PA","GFC.PA","GEA.PA","GBT.PA","FREY.PA","FPN.PA","FPG.PA","FNTS.PA","FNAC.PA","FFP.PA","FEM.PA","FBEL.PA","FAYE.PA","CIV.PA","CGM.PA","CGG.PA","CCA.PA","BOL.PA","BELI.PA","AREVA.PA","ALUMS.PA","ALTUT.PA","ALTRA.PA","ALTER.PA","ALQGC.PA","ALORO.PA","ALINN.PA","ALHVS.PA","ALGEN.PA","ALCLS.PA","ALCLA.PA","ALBUD.PA","ALALO.PA","ALADO.PA","AKA.PA","ACA.PA","ABIO.PA","ZIF.PA","VLAP.PA","VET.PA","VCT.PA","UFF.PA","UDIS.PA","TNG.PA","MLFIH.PA","HSB.PA","MSTY.PA","GJAJ.PA","DEC.PA","MLEST.PA","JCQ.PA","MLJAN.PA","MLKRI.PA","MLKIM.PA","KOF.PA","KEY.PA","ALKEY.PA","LAX.PA","PM.PA","MLSEQ.PA","MLSMP.PA","STM.PA","CSTM.PA","NXI.PA","NUM.PA","NRO.PA","NEX.PA","OXI.PA","ORP.PA","ORAP.PA","ONXEO.PA","OLG.PA","MLOPT.PA","MLONE.PA","ALONC.PA","ALODI.PA","ALOCA.PA","OSE.PA","AGTA.PA","SQI.PA","RX.PA","CATR.PA","MRK.PA","IFF.PA","HXL.PA","FORDP.PA","ALUCR.PA","RIN.PA","MLVER.PA","MLGEQ.PA","LTE.PA","GV.PA","DGNV.PA","DG.PA","CRAV.PA","ALVXM.PA","ALVMG.PA","ALVEL.PA","ALVDM.PA","ALVDI.PA","MLVAL.PA","MLVES.PA","VIAD.PA","MLANT.PA","MCNV.PA","MLPHW.PA","MBWS.PA","ALWEB.PA","IGE.PA","XPO.PA","GND.PA","MLDYH.PA","MLZAM.PA","STAGR.PA","ZCNV.PA","MLDUR.PA","CV.PA","ABCA.PA","ABBV.PA","AB.PA","MLABC.PA","ABVX.PA","MLACP.PA","CIB.PA","ACAN.PA","ALACI.PA","ALACR.PA","MLACT.PA","MLLEO.PA","ACNV.PA","ATI.PA","ALP.PA","ALADM.PA","ADVI.PA","ALPAT.PA","ADV.PA","ADOC.PA","ALADA.PA","ADI.PA","FGA.PA","MLNOT.PA","BOAF.PA","AFO.PA","MLAFT.PA","FOAF.PA","CRLO.PA","CRBP2.PA","CNF.PA","CAT31.PA","ALAGR.PA","CMO.PA","AGCR.PA","MLBRO.PA","MLMLT.PA","CRSU.PA","CRLA.PA","MLAAH.PA","MLIFE.PA","MLAGI.PA","ALFBA.PA","AKE.PA","MLAKD.PA","AKENV.PA","ALCOI.PA","ALATP.PA","LTA.PA","CRAP.PA","ATE.PA","ALUCI.PA","ALTHE.PA","ALTEV.PA","ALSPO.PA","ALSIM.PA","ALSDL.PA","ALS30.PA","ALRGR.PA","ALNEV.PA","ALNBT.PA","ALLOG.PA","ALIOX.PA","ALIMO.PA","ALICR.PA","ALHIT.PA","ALHEO.PA","ALGOW.PA","ALGLD.PA","ALGEP.PA","ALFRE.PA","ALFPC.PA","ALEUP.PA","ALENT.PA","ALDEI.PA","ALCYB.PA","ALCOR.PA","ALCJ.PA","ALCAR.PA","ALAUP.PA","ALANT.PA","AREIT.PA","ALTRO.PA","ALNXT.PA","ALHPC.PA","ALMER.PA","ALSGD.PA","ALECR.PA","ALPHX.PA","ALREW.PA","ALINT.PA","ALTTI.PA","ALMGI.PA","ALEZV.PA","ALIDS.PA","ALMTH.PA","ALMED.PA","ALHOL.PA","ALI2S.PA","ALIMR.PA","ALREA.PA","ALPHY.PA","ALRIC.PA","ALPJT.PA","ALBFR.PA","ALMNG.PA","ALODS.PA","ALINS.PA","ALDBT.PA","ALBLD.PA","ALSFT.PA","ALBRS.PA","ALKDY.PA","ALIVA.PA","ALDBL.PA","ALBRI.PA","ALBI.PA","ALMDT.PA","ALMOU.PA","ALBIO.PA","ALAQU.PA","ALFST.PA","ALOBR.PA","ALTVO.PA","ALDEL.PA","ALDAR.PA","ALDR.PA","ALTXC.PA","ALCRB.PA","ALCOG.PA","ALHER.PA","ALUT.PA","ALSOA.PA","ALLIX.PA","ALSER.PA","ALWED.PA","ALMIL.PA","ALDMO.PA","ALMAK.PA","ALHYG.PA","ALSPW.PA","ALDLS.PA","ALLEX.PA","ALBLU.PA","ALGBE.PA","ALLMG.PA","ALMAS.PA","ALMET.PA","ALENR.PA","ALVIV.PA","ALDOL.PA","ALLP.PA","ALGIL.PA","ALCRM.PA","ALOSP.PA","ALMLB.PA","ALHIO.PA","ALISC.PA","ALANV.PA","ALPCI.PA","ALSEN.PA","ALSTW.PA","ALMIC.PA","ALCES.PA","ALCOF.PA","ALA2M.PA","ALBDM.PA","ALSOL.PA","ALBPS.PA","ALGEV.PA","ALTA.PA","ALVER.PA","ALPDX.PA","ALMDW.PA","ALDRV.PA","ALPGG.PA","ALNSE.PA","ALNOV.PA","ALTRI.PA","ALESA.PA","ALFIL.PA","ALPLA.PA","ALGCM.PA","ALROC.PA","ALTUR.PA","ALDIE.PA","ALVIA.PA","ALPOU.PA","ALWEC.PA","ALM.PA","ALLHB.PA","ALDV.PA","ALEO2.PA","ALPRI.PA","ALGAU.PA","ALSIP.PA","ALFOC.PA","ALEMV.PA","ALTLX.PA","ALEUA.PA","ALGIS.PA","ALPRO.PA","AMUN.PA","AMEBA.PA","AM.PA","AMPLI.PA","MLARD.PA","AML.PA","ROSA.PA","PSAT.PA","PROL.PA","PAOR.PA","PERR.PA","MLIMP.PA","MLHOP.PA","MLGRC.PA","GUI.PA","FIPP.PA","ETL.PA","EDI.PA","CO.PA","BLUE.PA","BLEE.PA","MPI.PA","ANF.PA","MND.PA","NSGP.PA","MLCEC.PA","MLPSH.PA","MLOLM.PA","MLAMA.PA","MLSIC.PA","ORPNV.PA","MLETA.PA","MLHYD.PA","TNFN.PA","INFE.PA","AUGR.PA","RAL.PA","MLFXO.PA","FALG.PA","LLY.PA","SLB.PA","STNT.PA","MLMTD.PA","MLFRC.PA","MLCMI.PA","NRX.PA","MLFMM.PA","MLTDS.PA","MLCFD.PA","SFCA.PA","SII.PA","APR.PA","MLAAT.PA","MLGAI.PA","ARTE.PA","ARG.PA","MLART.PA","MLARO.PA","JXR.PA","MLAMY.PA","ARTO.PA","PRC.PA","MLNMA.PA","ASY.PA","ASK.PA","MLVOP.PA","MLAEM.PA","CNP.PA","ASP.PA","ML350.PA","FATL.PA","ATEME.PA","ATONV.PA","AURE.PA","AUB.PA","AURS.PA","AVT.PA","AVQ.PA","AWOX.PA","AXW.PA","CSNV.PA","MLAZL.PA","BLC.PA","BCRA.PA","BCAM.PA","MLGES.PA","BEN.PA","MLMFI.PA","MLIOC.PA","DEXB.PA","MLV4S.PA","BERR.PA","MTU.PA","DIM.PA","BIM.PA","BIG.PA","MLCLI.PA","MLTBM.PA","BND.PA","BNS.PA","GBB.PA","BOI.PA","MLBOK.PA","CARP.PA","BON.PA","ENNV.PA","BOLNV.PA","MLLB.PA","MRB.PA","BUR.PA","BVINV.PA","BUI.PA","MLHMC.PA","CBDG.PA","CAS.PA","CAPLI.PA","CBOT.PA","CBR.PA","CCN.PA","CCE.PA","CC.PA","CDI.PA","CLNV.PA","CGR.PA","CEREN.PA","CEN.PA","MLROU.PA","CGD.PA","CFAO.PA","CFI.PA","TVRB.PA","MLTRC.PA","LHN.PA","CHSR.PA","MLFIR.PA","CHAU.PA","MLCSP.PA","MLOVE.PA","CIEM.PA","MLMAT.PA","MLTHA.PA","MLCIO.PA","FORE.PA","MLPIV.PA","VIL.PA","LTAN.PA","MLCJS.PA","CNV.PA","MLFCI.PA","MLCRO.PA","CRINV.PA","CRI.PA","CRBT.PA","CROS.PA","MLCTA.PA","CTRG.PA","MLSIL.PA","DAN.PA","IMDA.PA","MLDHZ.PA","DLT.PA","DSYNV.PA","DRTY.PA","DBT.PA","DBG.PA","COM.PA","MLMGL.PA","MLSDR.PA","MLMED.PA","DLTA.PA","ULDV.PA","FDPA.PA","MLEDR.PA","DGE.PA","DIREN.PA","MLDIG.PA","MLDDP.PA","MLBRI.PA","DIG.PA","DNX.PA","DOMS.PA","DPAM.PA","DUC.PA","DUPP.PA","MLEDS.PA","PVL.PA","FCMC.PA","MLDYN.PA","MLDYX.PA","MLEAS.PA","EEM.PA","ECASA.PA","EC.PA","MLECO.PA","MLEDU.PA","EDENV.PA","EFI.PA","GID.PA","EINV.PA","EIFF.PA","ELIS.PA","ELEC.PA","ELE.PA","GNE.PA","SUNV.PA","EPS.PA","TONN.PA","ELINV.PA","EMG.PA","SCHP.PA","MLEES.PA","MCPHY.PA","ENX.PA","EOSI.PA","MLEMG.PA","EONV.PA","EXPL.PA","ERA.PA","ERFNV.PA","ESI.PA","MLEBX.PA","MLHIN.PA","PAT.PA","MLCAC.PA","MLERO.PA","MLERI.PA","EURS.PA","EUCAR.PA","GET.PA","MLMCE.PA","MLITG.PA","EUR.PA","MLEVE.PA","GLO.PA","METEX.PA","EXE.PA","EXAC.PA","MLHYE.PA","MLMEX.PA","LEY.PA","FAUV.PA","MLFAC.PA","MFC.PA","MALT.PA","FED.PA","FINM.PA","NOKIA.PA","14488435.PA","ORIA.PA","FIM.PA","FLO.PA","FMU.PA","LEBL.PA","INEA.PA","MLCFI.PA","SPEL.PA","LFVE.PA","MLVIN.PA","FPNV.PA","THER.PA","TFF.PA","SOG.PA","SOFR.PA","SO.PA","SCDU.PA","SFT.PA","SFBS.PA","SDG.PA","SCR.PA","SAMS.PA","SABE.PA","RIB.PA","RCF.PA","PSB.PA","MUN.PA","MRM.PA","MMB.PA","MLVST.PA","MLTRO.PA","MLSTM.PA","MLPPI.PA","MLPOL.PA","MLPFX.PA","MLNLF.PA","MLMON.PA","MLLEA.PA","MLIML.PA","MLIDS.PA","MLGEO.PA","MLCOR.PA","LSS.PA","LR.PA","LPE.PA","LOCAL.PA","LD.PA","LAF.PA","ITS.PA","ITP.PA","INSD.PA","INN.PA","ING.PA","IDIP.PA","HF.PA","GTCL.PA","GOE.PA","GLENV.PA","GECP.PA","GDMS.PA","GAM.PA","FTRN.PA","COUR.PA","COH.PA","MLLOI.PA","MLIFC.PA","MLCOU.PA","MLUSG.PA","COFA.PA","MLRIV.PA","GENX.PA","MLFTI.PA","MLLED.PA","INF.PA","LAN.PA","MLSAT.PA","RIA.PA","SK.PA","MLSRP.PA","MLQUD.PA","OREGE.PA","MLUNT.PA","MLARI.PA","MLAUD.PA","MLGAL.PA","UNBL.PA","NRG.PA","SPIE.PA","MLCMG.PA","MKEA.PA","TXCL.PA","LNA.PA","PHA.PA","GNFT.PA","MLPLC.PA","MLCOL.PA","GBTNV.PA","SESNV.PA","VLTSA.PA","ROTH.PA","005408.PA","RUI.PA","MEMS.PA","GRVO.PA","MLPVG.PA","MLMII.PA","MLPAC.PA","MLCHP.PA","KORI.PA","TVLY.PA","RBT.PA","MLMUL.PA","MLGRD.PA","MLSBT.PA","MLNEO.PA","MRNNV.PA","POXEL.PA","PCA.PA","FREDS.PA","MLGLO.PA","RXLNV.PA","PREC.PA","MLTEK.PA","POM.PA","DEVR.PA","TFINV.PA","IDL.PA","CATG.PA","MLJSA.PA","LAT.PA","VDLO.PA","PAR.PA","PGP.PA","MLIDP.PA","MLGEL.PA","GTO.PA","GIRO.PA","MLGCR.PA","MLUMH.PA","HCO.PA","HERIG.PA","HIPAY.PA","MLHTT.PA","MLION.PA","MLTMT.PA","MLMHO.PA","IAM.PA","MLIPP.PA","SSI.PA","MLIPY.PA","MLSNT.PA","VIT.PA","ITL.PA","DECNV.PA","KAZI.PA","KERNV.PA","LI.PA","LCO.PA","LDL.PA","LNC.PA","MLLCS.PA","LOUP.PA","MLLSK.PA","SESG.PA","ORC.PA","MCLC.PA","MLSKN.PA","MLNEI.PA","MLWEY.PA","MLUMG.PA","MLHOT.PA","MLORC.PA","MLSEC.PA","MLMOV.PA","MLCHE.PA","MLNES.PA","MLTEA.PA","MLHCF.PA","MLBAT.PA","MLMAD.PA","MLCSV.PA","MLVIS.PA","MLSOL.PA","MLPHO.PA","MLMUT.PA","MLWTT.PA","MLONL.PA","MLDEX.PA","MLOSA.PA","MLTRS.PA","MLFDV.PA","MLPPF.PA","MLMNR.PA","MLPRI.PA","MLSUM.PA","MLPRO.PA","MLCLP.PA","MLDTB.PA","MLAAE.PA","MLATV.PA","MLSOC.PA","MLPGO.PA","MLUNI.PA","MONC.PA","MONT.PA","MRN.PA","GREV.PA","NXTV.PA","NERG.PA","NTG.PA","SACI.PA","SAFOR.PA","PARP.PA","RUSAL.PA","RUIDS.PA","RLL.PA","ROD.PA","RUINV.PA","VALE3.PA","SDT.PA","SFPI.PA","SGONV.PA","SRP.PA","TAYN.PA","TFI.PA","TIPI.PA","TOU.PA","VLA.PA","VETO.PA","VIA.PA","WLN.PA","RE.PA","SPI.PA","HOP.PA","INFY.PA","4848650.PA","LIN.PA","MAN.PA","SANNV.PA","SAVE.PA","SEFER.PA","SELER.PA","SEQ.PA"]


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

