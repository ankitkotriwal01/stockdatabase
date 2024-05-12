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
stocks = import streamlit as st
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
stocks = ["BMH.AX","BRK.AX","MTU.AX","MPX.AX","GPH.AX","PRA.AX","ICG.AX","DLS.AX","CLA.AX","OXXCB.AX","CBS.AX","VELCP.AX","ORG.AX","ANZ.AX","XRF.AX","WOW.AX","WAT.AX","QBE.AX","MDG.AX","VTX.AX","BXB.AX","BHP.AX","WVL.AX","WRR.AX","STO.AX","NHH.AX","NEN.AX","NDO.AX","MQG.AX","MCX.AX","KTE.AX","KIK.AX","IPT.AX","BMP.AX","ZYL.AX","WPL.AX","WNS.AX","WHC.AX","WES.AX","WDS.AX","WCC.AX","VMS.AX","VKA.AX","UCW.AX","TZL.AX","TLS.AX","SXL.AX","REA.AX","PBD.AX","NMS.AX","NME.AX","NFE.AX","NAB.AX","LER.AX","LCT.AX","LAU.AX","KOV.AX","KME.AX","KBC.AX","IRI.AX","HIL.AX","CPU.AX","CMW.AX","CBA.AX","BBG.AX","ANN.AX","PNA.AX","ZRL.AX","ZGL.AX","WSA.AX","WOR.AX","WEC.AX","WBC.AX","WBA.AX","SDL.AX","VIP.AX","VII.AX","VIE.AX","UGL.AX","TPM.AX","TGZ.AX","TGR.AX","TCN.AX","TCL.AX","SUD.AX","RRS.AX","RHC.AX","PLS.AX","OZL.AX","OKU.AX","NSX.AX","NOE.AX","NML.AX","MYR.AX","MOC.AX","MMR.AX","MKO.AX","LNR.AX","KRS.AX","KNH.AX","KKT.AX","KAS.AX","JRV.AX","ORS.AX","IMU.AX","ILU.AX","HVN.AX","GNC.AX","GML.AX","GID.AX","COH.AX","SPX.AX","BLD.AX","BEN.AX","ASX.AX","AMP.AX","3DM.AX","IIN.AX","YAL.AX","XTD.AX","WTR.AX","WFD.AX","WCP.AX","WBAPA.AX","VELIN.AX","UUL.AX","USG.AX","UOS.AX","UCM.AX","UBI.AX","TZN.AX","TWE.AX","TPI.AX","TGS.AX","TEN.AX","SOO.AX","KRA.AX","SIQ.AX","SIP.AX","SHV.AX","SEN.AX","SDF.AX","SBM.AX","SAI.AX","RBX.AX","RIS.AX","RIO.AX","PYC.AX","PSA.AX","PPT.AX","PMV.AX","PEK.AX","PDN.AX","PBP.AX","PAY.AX","PAN.AX","ORI.AX","OFX.AX","NTM.AX","NSP.AX","NOD.AX","NIO.AX","NHF.AX","MYX.AX","MYN.AX","MQA.AX","MOL.AX","MNY.AX","MIG.AX","MDD.AX","LTR.AX","LIC.AX","LCE.AX","LBT.AX","KPC.AX","KGM.AX","KGL.AX","JYC.AX","IPP.AX","IPL.AX","IPD.AX","IGO.AX","HFA.AX","HAW.AX","GXY.AX","GUD.AX","GMG.AX","GEM.AX","GCS.AX","GBA.AX","GAP.AX","FMG.AX","EME.AX","ELD.AX","ECO.AX","DVI.AX","DUO.AX","DUE.AX","DMP.AX","CVO.AX","CTP.AX","CSL.AX","CDD.AX","BTT.AX","BSE.AX","BPT.AX","BOL.AX","BLY.AX","BKW.AX","BKN.AX","BKL.AX","BFG.AX","ASZ.AX","KKL.AX","AMC.AX","ALU.AX","AJL.AX","AGI.AX","ABC.AX","ZEU.AX","ZAM.AX","YPB.AX","YOW.AX","YHL.AX","VIA.AX","MHI.AX","FBU.AX","MVP.AX","HDX.AX","DXS.AX","DWS.AX","DVN.AX","DVL.AX","DTM.AX","DRA.AX","DNA.AX","DLX.AX","DGX.AX","DGR.AX","DCN.AX","DCG.AX","WDE.AX","TDL.AX","IDX.AX","ENE.AX","TWR.AX","TME.AX","SKT.AX","SKC.AX","KMD.AX","VEI.AX","SXE.AX","SXA.AX","SER.AX","SEH.AX","RLE.AX","RCU.AX","QTM.AX","POW.AX","PEN.AX","PEA.AX","NZO.AX","MTN.AX","MCE.AX","IEM.AX","ICN.AX","GEG.AX","FPH.AX","FET.AX","EVN.AX","ERX.AX","EPD.AX","ELM.AX","EGP.AX","EFE.AX","ECX.AX","CUE.AX","CNX.AX","CNU.AX","BKY.AX","AJQ.AX","AIA.AX","AEF.AX","AEE.AX","88E.AX","XRO.AX","VGI.AX","SFH.AX","RFG.AX","RFF.AX","PGI.AX","PGF.AX","PFL.AX","JBH.AX","GFL.AX","FWD.AX","FSA.AX","FNP.AX","FLT.AX","FLN.AX","FFG.AX","FDC.AX","FAN.AX","AFJ.AX","TOX.AX","SVW.AX","SUN.AX","SKI.AX","SGH.AX","RGX.AX","PRT.AX","PGR.AX","NGY.AX","MNF.AX","MGX.AX","MGR.AX","LNG.AX","VRT.AX","TWH.AX","TTA.AX","TAH.AX","SHL.AX","REC.AX","RAP.AX","QUB.AX","PRY.AX","PHA.AX","OLV.AX","OLH.AX","KAM.AX","JHC.AX","HTA.AX","HSN.AX","HOM.AX","HNG.AX","HHL.AX","HAO.AX","GLH.AX","GBT.AX","CHC.AX","8IH.AX","ZYB.AX","VIG.AX","VAH.AX","TBH.AX","SPO.AX","SPL.AX","SOL.AX","SMA.AX","SHM.AX","SAR.AX","RWH.AX","RHI.AX","REX.AX","REG.AX","JAL.AX","RUM.AX","JRL.AX","JKL.AX","JIN.AX","JHX.AX","JAT.AX","GJT.AX","SHR.AX","AJA.AX","KSN.AX","KSC.AX","KPL.AX","KOR.AX","KIS.AX","KBU.AX","KSL.AX","KRM.AX","KRL.AX","KNM.AX","KNL.AX","KKO.AX","KFG.AX","KFE.AX","KDR.AX","KCN.AX","KBL.AX","KAT.AX","KAR.AX","KEY.AX","OSH.AX","WWI.AX","WOF.AX","WGO.AX","CRX.AX","WCN.AX","WAA.AX","VTM.AX","VSC.AX","VML.AX","VAN.AX","UML.AX","TWD.AX","TTE.AX","TMX.AX","TMP.AX","TIG.AX","TAP.AX","SYP.AX","SYD.AX","SST.AX","SRX.AX","BZL.AX","SNL.AX","SMX.AX","SMM.AX","SLX.AX","SKS.AX","RND.AX","PDM.AX","OSL.AX","MOU.AX","MSI.AX","MSB.AX","MOZ.AX","MOY.AX","MMJ.AX","MLX.AX","MLT.AX","MLB.AX","MDI.AX","MBO.AX","LEG.AX","SFR.AX","PNW.AX","NXT.AX","NWS.AX","NST.AX","NRT.AX","NNW.AX","NMT.AX","NKP.AX","NCL.AX","LKE.AX","ARE.AX","APN.AX","ADY.AX","RNY.AX","RNI.AX","RIM.AX","PWN.AX","NWZ.AX","NWSLV.AX","NWF.AX","NVL.AX","NVI.AX","NUF.AX","NTU.AX","NSR.AX","NSE.AX","NRR.AX","NMI.AX","NHC.AX","NGE.AX","NEU.AX","TOF.AX","ORE.AX","ONT.AX","OKJ.AX","OCC.AX","LGO.AX","BOQ.AX","URF.AX","TIX.AX","SSN.AX","PSF.AX","OVL.AX","OVH.AX","OTW.AX","OTI.AX","OTH.AX","ORL.AX","OPG.AX","OOO.AX","ONC.AX","OML.AX","OIL.AX","OGH.AX","OGC.AX","OEX.AX","OEG.AX","OEC.AX","ODN.AX","OAR.AX","NCC.AX","NAC.AX","MTA.AX","MRM.AX","PCL.AX","LCY.AX","IOF.AX","HZN.AX","ERA.AX","EGO.AX","CMT.AX","AOW.AX","AOK.AX","AOC.AX","ABL.AX","1AL.AX","ORX.AX","AYD.AX","IOG.AX","ORGN.AX","OVR.AX","OTC.AX","OZB.AX","UNV.AX","QVE.AX","QUR.AX","QST.AX","QSS.AX","QMS.AX","QAN.AX","IND.AX","AQX.AX","QRX.AX","BOQKOC-A","QUAL.AX","QBL.AX","QTG.AX","QRE.AX","QHL.AX","QMN.AX","QUE.AX","RXL.AX","RMD.AX","RHP.AX","RFN.AX","RED.AX","RCR.AX","RAF.AX","VXR.AX","GRB.AX","CXX.AX","CWN.AX","CII.AX","CAZ.AX","CAY.AX","CAS.AX","BDR.AX","AXZ.AX","ADN.AX","XST.AX","WPG.AX","WIN.AX","WAF.AX","VRL.AX","UXA.AX","ARV.AX","URI.AX","TYX.AX","TRL.AX","TPR.AX","TNR.AX","TLG.AX","TAS.AX","SYR.AX","SRQ.AX","SRK.AX","SPI.AX","SGZ.AX","SBU.AX","S2R.AX","RXP.AX","RXM.AX","RVR.AX","RVA.AX","UXC.AX","USF.AX","USA.AX","UBN.AX","GDF.AX","ENU.AX","EMF.AX","BIG.AX","BCS.AX","APW.AX","VTG.AX","VPC.AX","VOC.AX","VMT.AX","VMC.AX","PVE.AX","AVL.AX","VED.AX","VGE.AX","MVR.AX","PVD.AX","VBS.AX","VRX.AX","VEC.AX","VELPA.AX","YRR.AX","CWY.AX","WLC.AX","WTP.AX","WPI.AX","WMC.AX","WLL.AX","WLF.AX","WLD.AX","WHFPA.AX","WHF.AX","TPW.AX","SWM.AX","LMW.AX","EWC.AX","CWC.AX","AWI.AX","WDCSZB-A","WAC.AX","WCB.AX","WPLCD.AX","MWR.AX","NTC.AX","WESSRU-A","WPLKOT-A","PWNCA.AX","WEB.AX","WSG.AX","WGL.AX","WMK.AX","WKT.AX","WEL.AX","WHE.AX","XTE.AX","XAM.AX","DCC.AX","KSO.AX","XJOMOQ-A","XJOMOU-A","XTV.AX","XF1.AX","XJOKZT-A","XJOLOL-A","XJOKOP-A","XPD.AX","XXL.AX","DXF.AX","XIP.AX","XJOLON-A","XJOLOK-A","DYL.AX","YTMF06.AX","YTMF03.AX","YTMWE1.AX","YTMLL1.AX","YTMQF2.AX","YTMQF1.AX","CYU.AX","YTMSG1.AX","YNB.AX","YTMF05.AX","YTMF02.AX","HHY.AX","YTMF01.AX","YTMQF3.AX","YBR.AX","YTMF04.AX","DIV.AX","ZTA.AX","ZNC.AX","ZMG.AX","ZGM.AX","AIZ.AX","ZGCKOP-A","CZL.AX","IBG.AX","ZIP.AX","ZNZ.AX","AZC.AX","ZER.AX","ZML.AX","ZHGKOS-A","ZIM.AX","AAX.AX","AAI.AX","AAA.AX","BAF.AX","AAK.AX","AAD.AX","AADKOD-A","AAT.AX","AAC.AX","AAP.AX","AAU.AX","AAR.AX","AAJ.AX","ABX.AX","ABY.AX","ABV.AX","AB1.AX","ABW.AX","ALR.AX","ABP.AX","AEG.AX","ABA.AX","ABU.AX","ACX.AX","ACR.AX","MGP.AX","EAX.AX","AIV.AX","ACW.AX","ACL.AX","ACK.AX","ACG.AX","ACU.AX","IPE.AX","ACS.AX","ACB.AX","ACQ.AX","AKG.AX","ACY01.AX","ACP.AX","ACO.AX","ACE.AX","ADH.AX","LNK.AX","AHZ.AX","ADR.AX","ADO.AX","ADX.AX","ADA.AX","ADJ.AX","ADV.AX","ADD.AX","ADQ.AX","AES.AX","ASW.AX","AQR.AX","AER.AX","AEB.AX","AEK.AX","AIS.AX","AML.AX","AEV.AX","AED.AX","AEI.AX","AEJ.AX","AFA.AX","AFR.AX","DAF.AX","AFINA.AX","AFG.AX","CZA.AX","AFP.AX","AFI.AX","AGJ.AX","ANB.AX","AGX.AX","AGO.AX","AGL.AX","AGE.AX","AMN.AX","AHA.AX","AGLCD.AX","AGD.AX","AGS.AX","DFM.AX","AGR.AX","AGF.AX","AGY.AX","AGG.AX","AHL.AX","AHD.AX","AHG.AX","AHY.AX","AHX.AX","AHQ.AX","AHK.AX","AHF.AX","AHN.AX","AHR.AX","MJP.AX","AIQ.AX","AIO.AX","TO2.AX","AIB.AX","AIY.AX","AXP.AX","AIK.AX","AIR.AX","AJY.AX","AJX.AX","AJJ.AX","AJD.AX","AJM.AX","AKY.AX","AKP.AX","AKF.AX","AKM.AX","AKK.AX","AWC.AX","CAF.AX","AYR.AX","AQG.AX","AOH.AX","ALL.AX","ALK.AX","ALI.AX","ALC.AX","AUQ.AX","AQZ.AX","AWD.AX","APT.AX","GPS.AX","BLA.AX","ARS.AX","LEP.AX","ALY.AX","ALF.AX","ALQKOA-A","ALQ.AX","ATC.AX","ALT.AX","AQI.AX","AMT.AX","ALA.AX","AYS.AX","AMI.AX","AMB.AX","CCL.AX","AYH.AX","PAK.AX","AMH.AX","AMO.AX","SAY.AX","AMA.AX","AYK.AX","AYJ.AX","AZY.AX","MGU.AX","AWV.AX","ATM.AX","ANP.AX","ANW.AX","ANZKOR-A","AZZ.AX","TYO.AX","LHM.AX","AVD.AX","EOR.AX","TA8.AX","ANZCD.AX","ANI.AX","ASN.AX","MAD.AX","ANO.AX","ATP.AX","ANR.AX","GGG.AX","ANG.AX","AOP.AX","AOG.AX","AOD.AX","AOU.AX","AOA.AX","AON.AX","APZ.AX","APX.AX","API.AX","APD.AX","APE.AX","APA.AX","APO.AX","APG.AX","WNR.AX","AQQ.AX","APY.AX","AQU.AX","AQS.AX","AQF.AX","AQD.AX","HUO.AX","AQC.AX","AQP.AX","ARI.AX","ARG.AX","AXT.AX","AXE.AX","ARA.AX","ARO.AX","AR1.AX","ARM.AX","ARD.AX","AWN.AX","ARJ.AX","ARU.AX","ARC.AX","ARF.AX","AWO.AX","AWQ.AX","ARW.AX","ARB.AX","SAM.AX","ICQ.AX","AST.AX","ASL.AX","DIG.AX","PAI.AX","PTM.AX","EAI.AX","AUF.AX","ASH.AX","ATR.AX","ASXKOT-A","ASY.AX","ASB.AX","ASXKOR-A","AZQ.AX","ASP.AX","ASXCD.AX","PZC.AX","AYA.AX","ATA.AX","ATE.AX","ATU.AX","ATI.AX","SHJ.AX","SGP.AX","SFC.AX","SEK.AX","S32.AX","PRR.AX","PPG.AX","POH.AX","PMP.AX","PHI.AX","INL.AX","LYL.AX","LBL.AX","IVC.AX","ITD.AX","IMD.AX","IDZ.AX","GZL.AX","GWR.AX","GUF.AX","GPT.AX","GDY.AX","CYP.AX","CYG.AX","CVC.AX","CUV.AX","CSE.AX","COO.AX","COM.AX","CND.AX","CLX.AX","CGO.AX","CGL.AX","CCP.AX","CUX.AX","CCF.AX","CAB.AX","CAA.AX","BYR.AX","BYI.AX","BTI.AX","BTC.AX","BPS.AX","BNO.AX","BCI.AX","AWE.AX","AVX.AX","AVJ.AX","AVH.AX","TTS.AX","TTN.AX","TTC.AX","TSV.AX","TSN.AX","TSM.AX","TPD.AX","TON.AX","TOE.AX","THX.AX","TGG.AX","TFL.AX","TFG.AX","TFC.AX","SXY.AX","STX.AX","SRV.AX","SRF.AX","PPN.AX","SOR.AX","SND.AX","SNC.AX","SMI.AX","SKE.AX","SIO.AX","SHP.AX","SHE.AX","SGU.AX","SGO.AX","SGM.AX","SFL.AX","SEA.AX","SDM.AX","SDG.AX","SCI.AX","SCG.AX","SCD.AX","SBB.AX","SAV.AX","RUB.AX","RTR.AX","SMD.AX","RSG.AX","RRL.AX","ROY.AX","RNU.AX","RMG.AX","RKN.AX","RGP.AX","RFT.AX","RFL.AX","REZ.AX","RER.AX","RDS.AX","RCM.AX","RCG.AX","RTA.AX","RBR.AX","RAW.AX","RAD.AX","R3D.AX","PYM.AX","PXS.AX","PXG.AX","PWW.AX","PSC.AX","PSY.AX","PRU.AX","PRL.AX","PRH.AX","PRG.AX","PPS.AX","POZ.AX","PNL.AX","PNE.AX","PME.AX","PLV.AX","PLH.AX","PIO.AX","PGL.AX","PGC.AX","PFM.AX","PEZ.AX","PEX.AX","PEC.AX","PBT.AX","PAF.AX","PAC.AX","PAA.AX","PMY.AX","NCM.AX","NCK.AX","NAM.AX","MYS.AX","MXI.AX","MXC.AX","NWR.AX","MVT.AX","MVF.AX","MUB.AX","MUA.AX","MTS.AX","MTH.AX","MRP.AX","MRN.AX","MPL.AX","MNW.AX","MNM.AX","MND.AX","MML.AX","MMG.AX","NGX.AX","MLM.AX","MLI.AX","MLD.AX","MHM.AX","MFG.AX","MEO.AX","MEI.AX","MEA.AX","MDC.AX","MCR.AX","MCP.AX","MAS.AX","MAQ.AX","MAK.AX","MAH.AX","MBK.AX","LYC.AX","LVT.AX","MPJ.AX","LMG.AX","LMC.AX","LMB.AX","LLO.AX","LLC.AX","LIO.AX","LHC.AX","LGR.AX","LFC.AX","LCM.AX","MBD.AX","IZZ.AX","ISN.AX","ISD.AX","IRE.AX","IQ3.AX","IPA.AX","IMF.AX","ILH.AX","IGL.AX","IFN.AX","IDR.AX","ICZ.AX","IAG.AX","GRF.AX","HSO.AX","HRR.AX","HMX.AX","HLS.AX","HIT.AX","HGO.AX","HGL.AX","HCH.AX","HAV.AX","GXL.AX","GUL.AX","GTY.AX","GSC.AX","GRY.AX","GOZ.AX","GOLD.AX","GNG.AX","GMR.AX","GMN.AX","GMM.AX","GLL.AX","GHC.AX","GCR.AX","GCN.AX","GBP.AX","GBM.AX","GAL.AX","FZR.AX","FXL.AX","GGE.AX","FUN.AX","FTZ.AX","FRM.AX","FRI.AX","FRC.AX","FOY.AX","FOD.AX","FMS.AX","FML.AX","FLK.AX","FIE.AX","FGX.AX","GPP.AX","FGG.AX","FGF.AX","FFT.AX","GLA.AX","FCN.AX","FCG.AX","EZL.AX","EXU.AX","EVT.AX","ERR.AX","ERL.AX","ERJ.AX","ERD.AX","EMX.AX","EML.AX","EMH.AX","EMC.AX","EMB.AX","ELX.AX","ELK.AX","EGY.AX","EGS.AX","EGH.AX","FCR.AX","EEG.AX","EDE.AX","ECG.AX","EBG.AX","DYE.AX","DVA.AX","DTX.AX","DTL.AX","DSH.AX","DRM.AX","DOW.AX","DM1.AX","DLE.AX","DKO.AX","DKM.AX","DGO.AX","DDT.AX","DDR.AX","CVS.AX","CZZ.AX","CYY.AX","CYB.AX","CVN.AX","CUP.AX","CTX.AX","CTT.AX","CTR.AX","CTM.AX","CTD.AX","CSV.AX","CSS.AX","CRL.AX","CR8.AX","COI.AX","COE.AX","CNW.AX","CMM.AX","CMI.AX","CM8.AX","CLV.AX","CLQ.AX","CLH.AX","CINPA.AX","CIM.AX","CIE.AX","CHN.AX","CGS.AX","CGN.AX","CGH.AX","CGF.AX","CFE.AX","CDV.AX","CDU.AX","CDP.AX","CDG.AX","CCV.AX","CAR.AX","CAP.AX","CAJ.AX","BYE.AX","BWX.AX","BWP.AX","BWF.AX","BUL.AX","BUG.AX","BTN.AX","BSR.AX","BSM.AX","BSL.AX","COY.AX","CCJ.AX","BRG.AX","BRBCA.AX","BPF.AX","BOE.AX","BOA.AX","BCG.AX","BMG.AX","BLX.AX","BLT.AX","BLK.AX","BLG.AX","BGG.AX","BFC.AX","BCT.AX","BUR.AX","BAU.AX","BAR.AX","BAL.AX","AZS.AX","AZK.AX","AZJ.AX","AYF.AX","AYC.AX","AYB.AX","AXI.AX","AVZ.AX","AVI.AX","AUZ.AX","AUC.AX","AUB.AX","8CO.AX","1ST.AX","1PG.AX","DMPKOE-A","TPP.AX","HZR.AX","ETE.AX","EER.AX","RWD.AX","PIQ.AX","EXC.AX","ESI.AX","SIR.AX","SGT.AX","EUM.AX","TML.AX","RMS.AX","NDQ.AX","SFI.AX","CKF.AX","SAU.AX","BIQ.AX","BRU.AX","TTI.AX","PDY.AX","GPR.AX","CNQ.AX","RSH.AX","G8C.AX","SAO.AX","TOM.AX","NXR.AX","PML.AX","LIT.AX","CDA.AX","RIC.AX","NSTKOQ-A","CDT.AX","ENZ.AX","PPP.AX","DJW.AX","BML.AX","RXH.AX","SBI.AX","LML.AX","SRI.AX","STON.AX","IMC.AX","SRR.AX","KIN.AX","CWH.AX","TOU.AX","RTG.AX","SLK.AX","HML.AX","MTR.AX","AYZ.AX","CCZ.AX","CGR.AX","RMI.AX","NUH.AX","POS.AX","DOWKOP-A","AUK.AX","TTW.AX","BRS.AX","PBG.AX","MDL.AX","GBZ.AX","SVY.AX","BUY.AX","CNL.AX","MAX.AX","ICX.AX","GMC.AX","CLY.AX","POP.AX","PPX.AX","REH.AX","BEZ.AX","TAM.AX","MNS.AX","CYC.AX","GC1.AX","TRG.AX","MSM.AX","TGN.AX","WDR.AX","OCL.AX","PNX.AX","LCD.AX","SIT.AX","LSX.AX","SES.AX","EAL.AX","ERM.AX","TPS.AX","HHM.AX","BRN.AX","ORR.AX","GLB.AX","TNP.AX","GRV.AX","SUM.AX","HNR.AX","MIRN.AX","SSI.AX","EHE.AX","ENR.AX","CVG.AX","FAR.AX","SKB.AX","MRC.AX","MEB.AX","GBG.AX","SIV.AX","CVV.AX","ECV.AX","SLE.AX","MOV.AX","CKA.AX","RIE.AX","DTI.AX","EUG.AX","GMY.AX","KLO.AX","MIN.AX","SIH.AX","LHB.AX","MP1.AX","CAQ.AX","IEQ.AX","MPO.AX","GIP.AX","HFR.AX","AVQ.AX","AVN.AX","AVB.AX","AVG.AX","AZM.AX","AZV.AX","BBN.AX","BRL.AX","BBR.AX","BBX.AX","BBGDA.AX","BBL.AX","BCD.AX","BCK.AX","BCC.AX","BEL.AX","BGH.AX","BGD.AX","BGA.AX","BGC.AX","BGS.AX","BGL.AX","BIT.AX","PAR.AX","GBI.AX","BIS.AX","BXN.AX","BKI.AX","BKT.AX","CDB.AX","BMZ.AX","BOK.AX","BLDCD.AX","BLZ.AX","SAN.AX","TCH.AX","BMN.AX","SOP.AX","KLR.AX","BNE.AX","BNT.AX","BNR.AX","BND.AX","BNV.AX","BOC.AX","RGB.AX","BOP.AX","BOND.AX","BPH.AX","BPL.AX","BPA.AX","BSA.AX","BST.AX","BUX.AX","BUD.AX","BAP.AX","AUP.AX","MTB.AX","SFZ.AX","BWR.AX","BYL.AX","IBC.AX","RCT.AX","CZI.AX","OCP.AX","CBAKOS-A","CBC.AX","CBL.AX","CBAKOO-A","CBACD.AX","CCLCD.AX","CDM.AX","ENC.AX","CDH.AX","UPD.AX","CDY.AX","CEL.AX","CYA.AX","SCP.AX","CWP.AX","CEN.AX","CLT.AX","CXM.AX","CNI.AX","CMA.AX","CER.AX","VCX.AX","CNLCA.AX","CGW.AX","CGC.AX","CIA.AX","CTO.AX","CIZ.AX","CIW.AX","CIR.AX","CIN.AX","CIK.AX","CJC.AX","CKL.AX","CL1.AX","CVW.AX","CAM.AX","CLZ.AX","CL8.AX","CMP.AX","CMC.AX","CMY.AX","CPD.AX","CPS.AX","CQC.AX","CQR.AX","PNC.AX","LCK.AX","CTE.AX","SWR.AX","CRM.AX","CRQ.AX","CRB.AX","CSR.AX","CSLCD.AX","CSD.AX","GXNCA.AX","CTN.AX","CTDKOB-A","CUU.AX","CVE.AX","CVT.AX","CV1.AX","CXO.AX","CXZ.AX","CXU.AX","CYL.AX","CYS.AX","CZN.AX","CZR.AX","DNK.AX","DAU.AX","DTR.AX","DSX.AX","FNTDA.AX","DGH.AX","DXB.AX","DML.AX","DMC.AX","SBN.AX","DIS.AX","LOM.AX","DUI.AX","DRX.AX","KDL.AX","MED.AX","DJXKOE-A","DMI.AX","DMG.AX","DMY.AX","DME.AX","DMA.AX","DRG.AX","DSB.AX","DUB.AX","EAR.AX","EAS.AX","EBO.AX","EBT.AX","EPM.AX","IQE.AX","EVO.AX","RDH.AX","IEL.AX","EGL.AX","EGN.AX","EGG.AX","EGI.AX","EGODA.AX","EHL.AX","ENN.AX","EOS.AX","ELT.AX","8EC.AX","EMG.AX","MBE.AX","MVE.AX","EMU.AX","EMUCA.AX","RMP.AX","EMR.AX","MAE.AX","SGR.AX","EOL.AX","EPW.AX","EPA.AX","EPX.AX","UEQ.AX","EQU.AX","EQT.AX","RQL.AX","MVW.AX","EQE.AX","PIC.AX","OEQ.AX","EQX.AX","ERI.AX","ESV.AX","ESR.AX","ESM.AX","ESK.AX","REV.AX","RARI.AX","MUE.AX","EVR.AX","EVM.AX","EVZ.AX","EVRDA.AX","EVE.AX","STOKOU-A","EXE.AX","MQGKOD-A","EXM.AX","EXG.AX","MEP.AX","GTE.AX","ILUKOQ-A","EZA.AX","FXJ.AX","FBR.AX","FFC.AX","FEL.AX","FWL.AX","FFI.AX","FGI.AX","FGR.AX","FND.AX","FID.AX","FSI.AX","SGF.AX","FRX.AX","MFF.AX","FNT.AX","USR.AX","FSF.AX","ORGR.AX","GFI.AX","RCF.AX","WBCCD.AX","WAX.AX","GRG.AX","SPK.AX","NTL.AX","VGL.AX","TAHCD.AX","MIL.AX","RYD.AX","IFT.AX","MKE.AX","UND.AX","SXI.AX","FRN.AX","GVF.AX","SFN.AX","FYI.AX","ENB.AX","GCY.AX","GDI.AX","GDA.AX","GTK.AX","GER.AX","GMD.AX","GES.AX","GTG.AX","RES.AX","GSS.AX","GNX.AX","GNE.AX","SGQ.AX","GED.AX","GMA.AX","GFY.AX","MPP.AX","GLN.AX","GLE.AX","GLF.AX","HHV.AX","GBE.AX","GME.AX","GMF.AX","GNV.AX","GSE.AX","LSN.AX","TPO.AX","GOR.AX","KGD.AX","SAUDA.AX","OGX.AX","GOW.AX","ORN.AX","GOE.AX","TAR.AX","PGO.AX","GTR.AX","GWA.AX","HAS.AX","HMI.AX","HAZ.AX","HCT.AX","HDG.AX","SUHDC.AX","HLX.AX","SUH.AX","PHG.AX","ONE.AX","HXG.AX","HSOKOB-A","RHT.AX","HLODA.AX","HGG.AX","HLO.AX","OHE.AX","HSK.AX","JHL.AX","RHS.AX","HIG.AX","HPR.AX","HJB.AX","TENDA.AX","SMP.AX","HPI.AX","HRL.AX","HSXKOR-A","HUB.AX","IAU.AX","IAT.AX","IAB.AX","IB8.AX","ICT.AX","ICI.AX","ICS.AX","ICU.AX","IDO.AX","IDC.AX","IDM.AX","IDT.AX","IEC.AX","IFM.AX","IFS.AX","IFZ.AX","IFL.AX","IIL.AX","IXR.AX","IPC.AX","IMA.AX","IPH.AX","IPB.AX","IRM.AX","IRC.AX","IRD.AX","KPT.AX","ITW.AX","ISU.AX","ISH.AX","ISX.AX","ITQ.AX","IVO.AX","IVX.AX","IVQ.AX","IVR.AX","IWG.AX","JKA.AX","JCI.AX","JCS.AX","JPR.AX","KPO.AX","KRC.AX","KNO.AX","KPR.AX","KRB.AX","KTA.AX","D13.AX","LRS.AX","RLC.AX","LAA.AX","LAM.AX","SLR.AX","SO4.AX","LSA.AX","LTN.AX","LLCCD.AX","LRR.AX","3PL.AX","LMR.AX","LRL.AX","LGD.AX","LOV.AX","LPE.AX","LSR.AX","LWP.AX","MZN.AX","MQGCD.AX","MGY.AX","MGT.AX","MYE.AX","MBN.AX","MBT.AX","MBC.AX","MCS.AX","MCH.AX","MCT.AX","MMS.AX","MSG.AX","MDR.AX","MPLKOQ-A","MUI.AX","MNE.AX","MLA.AX","MRQ.AX","SXT.AX","ENT.AX","MTD.AX","MKB.AX","OSP.AX","MGB.AX","MGL.AX","MGZ.AX","MGV.AX","MGS.AX","MGC.AX","MHC.AX","A2M.AX","MYT.AX","VAR.AX","MRD.AX","PDZ.AX","SWK.AX","MIR.AX","PLP.AX","SYA.AX","NMG.AX","TND.AX","POK.AX","PNN.AX","MOO.AX","PCP.AX","MMI.AX","MIH.AX","MNQ.AX","RCY.AX","MOD.AX","MZM.AX","MOQ.AX","MOX.AX","SMN.AX","MUM.AX","MQGKOY-A","MRR.AX","MRF.AX","MSV.AX","MSC.AX","MSP.AX","MTL.AX","MTM.AX","MUS.AX","MX1.AX","MZI.AX","NAG.AX","NVT.AX","NCO.AX","NABCD.AX","NAN.AX","NBL.AX","NEC.AX","NEA.AX","NWT.AX","NHO.AX","WMN.AX","WNH.AX","AUIN.AX","NXM.AX","BRB.AX","LITCC.AX","SMC.AX","ENX.AX","LITCB.AX","OXX.AX","MAU.AX","NOV.AX","NOR.AX","NPX.AX","NWH.AX","NSL.AX","MEZ.AX","SNZ.AX","OBJ.AX","ODY.AX","OEL.AX","OFW.AX","OGY.AX","TDO.AX","OMT.AX","OMH.AX","TNE.AX","OTR.AX","OOK.AX","TOP.AX","OPT.AX","ORA.AX","ORM.AX","OZG.AX","PSQ.AX","PGH.AX","SPZ.AX","PAB.AX","SPB.AX","PPY.AX","UPG.AX","CHF.AX","PXR.AX","PNR.AX","PEH.AX","PCH.AX","PPC.AX","PEP.AX","PEL.AX","PTL.AX","PSM.AX","PUN.AX","PEG.AX","PTR.AX","PFG.AX","PGM.AX","PHK.AX","PIL.AX","PKA.AX","COT.AX","SNR.AX","PMC.AX","PNV.AX","PPL.AX","PPK.AX","PSI.AX","PVA.AX","PSZ.AX","PTX.AX","PTB.AX","PWH.AX","PZR.AX","CAG.AX","RPG.AX","RYG.AX","RCE.AX","RCO.AX","RDG.AX","RDF.AX","RDM.AX","RFX.AX","RGS.AX","RGU.AX","RNO.AX","RHL.AX","RIOKOC-A","RVY.AX","RNL.AX","RRR.AX","RMT.AX","RNT.AX","RNS.AX","WRM.AX","RRE.AX","RSL.AX","RUL.AX","SLM.AX","SBR.AX","SIE.AX","SCU.AX","SDA.AX","SDI.AX","SSM.AX","SFG.AX","SFX.AX","SGN.AX","SGC.AX","SRO.AX","SHU.AX","TRS.AX","SHH.AX","SSL.AX","SIX.AX","SVA.AX","SSLPA.AX","SKF.AX","SKIKOQ-A","SLC.AX","SLA.AX","SMG.AX","SMR.AX","SNY.AX","SOM.AX","SVM.AX","SRT.AX","SRZ.AX","SRS.AX","SRQDA.AX","STS.AX","SRH.AX","SRY.AX","STOKRN-A","SWJ.AX","SPQ.AX","SUNCD.AX","SUL.AX","SVS.AX","SOI.AX","SOIDA.AX","SWMKOB-A","SWL.AX","SWE.AX","TLM.AX","TAU.AX","TMM.AX","TAN.AX","TAG.AX","TBR.AX","TCO.AX","TCLN.AX","TGP.AX","TGA.AX","TIS.AX","THO.AX","TNK.AX","TIK.AX","TKL.AX","TLSKOG-A","TLSKOQ-A","TLSKZE-A","TLSLOP-A","TMZ.AX","TNT.AX","TNG.AX","TOL.AX","TOT.AX","TPE.AX","TPC.AX","TSE.AX","TUP.AX","TV2.AX","TYK.AX","UGLKZC-A","UIL.AX","UNS.AX","AUI.AX","URIDA.AX","VXL.AX","VMX.AX","VMG.AX","VET.AX","USH.AX","VGP.AX","VMY.AX","VLA.AX","VLW.AX","VIT.AX","VIC.AX","WAL.AX","WAM.AX","WBCLOP-A","WDCKRD-A","WDCSRV-A","WDC.AX","WESLOW-A","WIC.AX","WIG.AX","WPLLOS-A","PLA.AX","BRC.AX","CAE.AX","CAV.AX","CAT.AX","CHP.AX","CHR.AX","CHZ.AX","CHK.AX","CNJ.AX","COF.AX","COJ.AX","ENA.AX","GBX.AX","MEU.AX","E88.AX","FRY.AX","GRA.AX","GRR.AX","HOR.AX","INA.AX","LTX.AX","MAI.AX","MEY.AX","MAT.AX","MEL.AX","4DS.AX","SPH.AX","TRM.AX","SPFKOP-A","MYQ.AX","MYO.AX","STI.AX","PRO.AX","REF.AX","REY.AX","STA.AX","SAP.AX","STL.AX","TER.AX","TRY.AX","TWT.AX","N1H.AX"]

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

