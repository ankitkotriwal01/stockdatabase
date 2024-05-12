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
stocks = ["PHOL-R.BK","PACE.BK","TAE.BK","WHAPF.BK","TPCH.BK","JUBILE.BK","JTS.BK","JMT-R.BK","JASIF.BK","JCT.BK","JWD.BK","JMART.BK","NPK-R.BK","KTC.BK","KTC-R.BK","KTB.BK","KGI.BK","KC.BK","KASET.BK","KPNPF.BK","KWC-R.BK","POMPUI.BK","NEP-R.BK","UPA-R.BK","QHPF.BK","QLT-R.BK","QH.BK","QTC-R.BK","Q-CON-R.BK","QHOP.BK","QLT.BK","QHHR.BK","QH-R.BK","QTC.BK","Q-CON.BK","SPRC-R.BK","SVH.BK","UWC-R.BK","UPF-R.BK","UNIQ.BK","VIBHA.BK","VARO.BK","VIH.BK","WIN-R.BK","TWPC-R.BK","WR.BK","WHA.BK","WHABT.BK","TWS.BK","WG.BK","WORLD-R.BK","WHART.BK","WIIK.BK","SPA-R.BK","XO-R.BK","XO.BK","YUASA.BK","YCI.BK","YUASA-R.BK","YNP-R.BK","YCI-R.BK","YNP.BK","ZMICO-R.BK","ZMICO.BK","AAV.BK","AAV-R.BK","ABPIF.BK","ABICO-R.BK","ABICO.BK","EA-R.BK","ABC-R.BK","EA.BK","ABC.BK","ACD-R.BK","ACAP-R.BK","ACC-R.BK","ACC.BK","ACAP.BK","AJD.BK","ADAM-R.BK","ADVANC.BK","ADVANC-R.BK","ADVA42P1602A.BK","AEONTS-R.BK","AEC-R.BK","AEONTS.BK","AEC.BK","AFC.BK","AF.BK","AF-R.BK","AFC-R.BK","TAE-R.BK","AGE.BK","AGE-R.BK","AHC.BK","AH-R.BK","AH.BK","AHC-R.BK","EFORL.BK","AIRA-R.BK","AIT-R.BK","AIRA.BK","NOK-R.BK","AIE-R.BK","BA-R.BK","EFORL-R.BK","AIE.BK","BA.BK","AI-R.BK","NOK.BK","AI.BK","AIT.BK","AJD-R.BK","AJ-R.BK","AJ.BK","AKR-R.BK","AKP.BK","AKP-R.BK","AKR.BK","ALUCON-R.BK","ALUCON.BK","AMANAH.BK","AMARIN.BK","AMATAV-R.BK","AMANAH-R.BK","AMATA.BK","AMATA-R.BK","AMATAV.BK","AMATAR.BK","AMC-R.BK","AMC.BK","AMARIN-R.BK","CTARAF.BK","CSS.BK","HPF.BK","TREIT.BK","ANAN.BK","TLGF.BK","TNPF.BK","CSS-R.BK","LHPF.BK","ANAN-R.BK","AOT.BK","AOT-R.BK","AP.BK","APCS.BK","APURE.BK","APURE-R.BK","APX.BK","AP-R.BK","APCO.BK","APX-R.BK","APCO-R.BK","APCS-R.BK","AQUA.BK","AQ.BK","AQUA-R.BK","AQ-R.BK","ARIP-R.BK","ARROW-R.BK","ARROW.BK","ARIP.BK","ASP.BK","ASIAN.BK","BLA-R.BK","ASCON.BK","ASP-R.BK","ASEFA-R.BK","PMTA-R.BK","ASK.BK","AS.BK","ASIMAR-R.BK","UPA.BK","ASEFA.BK","BLA.BK","ASK-R.BK","AS-R.BK","ASIA-R.BK","ASIA.BK","PMTA.BK","ASIMAR.BK","PCA.BK","PCA-R.BK","ASIAN-R.BK","J.BK","SCBLIF.BK","J-R.BK","ATP30-R.BK","ATP30.BK","AUCT.BK","AUCT-R.BK","AYUD.BK","AYUD-R.BK","BAY.BK","BRC.BK","BBL.BK","BBL-R.BK","BCP.BK","BCH-R.BK","BCH.BK","BCP-R.BK","BDMS.BK","BDMS-R.BK","BECL.BK","BEM.BK","BEAUTY-R.BK","BEC-R.BK","BFIT.BK","BFIT-R.BK","BGT.BK","BGT-R.BK","BH-R.BK","BH.BK","BIGC.BK","BIG-R.BK","BIG.BK","BIGC-R.BK","BJC.BK","BJC-R.BK","BJCHI.BK","BJCHI-R.BK","BKI-R.BK","BKD.BK","BKI.BK","BKD-R.BK","BKKCP.BK","BLAND-R.BK","BLISS.BK","BLAND.BK","BLISS-R.BK","BMCL.BK","BOL-R.BK","BOL.BK","BROCK-R.BK","BROOK.BK","BRR-R.BK","BROCK.BK","BSM-R.BK","BSBM.BK","BSM.BK","BSBM-R.BK","BTS.BK","BTC.BK","BTC-R.BK","BTS-R.BK","BTNC-R.BK","BTNC.BK","BTSGIF.BK","CMR.BK","SBPF.BK","CMR-R.BK","BRR.BK","BUI.BK","BUI-R.BK","BWG.BK","BWG-R.BK","GCAP.BK","IFS-R.BK","CBG-R.BK","CBG.BK","CCET-R.BK","CCN-R.BK","CCN.BK","CCP-R.BK","CCP.BK","CCET.BK","CEN-R.BK","CENTEL.BK","LHSC.BK","CEI.BK","CEI-R.BK","CPICO.BK","TUCC-R.BK","TUCC.BK","CEN.BK","CENTEL-R.BK","CFRESH-R.BK","CFRESH.BK","CGD.BK","CGD-R.BK","CGH.BK","CGH-R.BK","CHG.BK","CHG-R.BK","CHUO.BK","CHUO-R.BK","CHOW.BK","CIMBT.BK","U-R.BK","MJLF.BK","CIG.BK","CIG-R.BK","CIMBT-R.BK","CITY-R.BK","CI-R.BK","CI.BK","CITY.BK","CKP.BK","CK.BK","CK-R.BK","CKP-R.BK","CMO.BK","CM-R.BK","CM.BK","CMO-R.BK","CNT.BK","CNT-R.BK","CNS.BK","CPALL-R.BK","CPL-R.BK","CPH.BK","CPI.BK","CPR-R.BK","CPN.BK","CPALL.BK","CPF-R.BK","CPN-R.BK","CPL.BK","CPH-R.BK","CRYSTAL.BK","CPI-R.BK","CPF.BK","CPR.BK","CPNCG.BK","CPNRF.BK","CPTGF.BK","CRANE.BK","CRANE-R.BK","CSP-R.BK","CSR.BK","CSP.BK","CSL-R.BK","CSR-R.BK","CSL.BK","CSC-R.BK","CSC.BK","CTW-R.BK","CTW.BK","CWT-R.BK","CWT.BK","DAII-R.BK","DAII.BK","DCON.BK","DCC-R.BK","DCC.BK","DCORP-R.BK","DCORP.BK","DCON-R.BK","DELTA.BK","PHOL.BK","SANKO.BK","DIMET.BK","DIMET-R.BK","TVD-R.BK","DIF.BK","SANKO-R.BK","TVD.BK","DNA-R.BK","DNA.BK","CHO-R.BK","CHO.BK","DRACO.BK","DRT.BK","DRT-R.BK","DRACO-R.BK","DSGT.BK","DSGT-R.BK","DTAC.BK","DTCI-R.BK","DTC.BK","DTAC-R.BK","DTCPF.BK","DTC-R.BK","DTCI.BK","EASTW.BK","EASON.BK","EPG-R.BK","ECF.BK","EPG.BK","EARTH-R.BK","EASON-R.BK","EARTH.BK","EASTW-R.BK","ECF-R.BK","ECL-R.BK","ECL.BK","NINE-R.BK","NINE.BK","EE.BK","EE-R.BK","EGCO.BK","EGATIF.BK","EGCO-R.BK","EIC-R.BK","UOB8TF.BK","EIC.BK","SCI.BK","SCI-R.BK","EMC-R.BK","EMC.BK","PTG.BK","T.BK","EPCO.BK","EPCO-R.BK","MGE.BK","ERW.BK","ERW-R.BK","ERWPF.BK","IMPACT.BK","ESTAR.BK","LHHOTEL.BK","S-R.BK","ESSO.BK","S.BK","ESTAR-R.BK","ESSO-R.BK","MIT.BK","UREKA.BK","UREKA-R.BK","EVER-R.BK","EVER.BK","SGF-R.BK","FANCY.BK","FANCY-R.BK","SGF.BK","FER.BK","FER-R.BK","NFC.BK","RP-R.BK","RP.BK","NFC-R.BK","FE-R.BK","FE.BK","FIRE.BK","FVC.BK","TMILL.BK","TMILL-R.BK","FMT.BK","FMT-R.BK","FNS.BK","FNS-R.BK","FOCUS-R.BK","FPI.BK","FSMART-R.BK","SFP-R.BK","POMPUI-R.BK","TFG-R.BK","FPI-R.BK","TKN.BK","FORTH-R.BK","FOCUS.BK","TFG.BK","FSMART.BK","TKN-R.BK","SFP.BK","FORTH.BK","FSS-R.BK","FSS.BK","SSTSS.BK","URBNPF.BK","M-STOR.BK","TLOGIS.BK","POPF.BK","FUTUREPF.BK","SSPF.BK","TIF1.BK","TRIF.BK","GOLDPF.BK","SCBSET.BK","UNIPF.BK","MIPF.BK","FVC-R.BK","GC.BK","GCAP-R.BK","GC-R.BK","GEL-R.BK","LPH.BK","GEL.BK","GENCO-R.BK","GENCO.BK","LPH-R.BK","GFPT-R.BK","GFPT.BK","GIFT-R.BK","GIFT.BK","GJS.BK","GJS-R.BK","GL-R.BK","UAC-R.BK","GLOW-R.BK","GPSC-R.BK","GLOW.BK","GPSC.BK","VGI-R.BK","STHAI.BK","SCAN.BK","GLOBAL-R.BK","GL.BK","STHAI-R.BK","VGI.BK","GLAND-R.BK","UAC.BK","GLOBAL.BK","SCAN-R.BK","GLAND.BK","SUTHA.BK","SUTHA-R.BK","GOLD.BK","GOLD-R.BK","PCSGH-R.BK","ICHI.BK","GRAMMY.BK","GSTEL.BK","GSTEL-R.BK","GTB-R.BK","GTB.BK","GUNKUL.BK","GUNKUL-R.BK","GYT-R.BK","GYT.BK","HANA.BK","HTECH.BK","HTECH-R.BK","THL-R.BK","THL.BK","HANA-R.BK","HFT.BK","HFT-R.BK","HMPRO.BK","HMPRO-R.BK","HOTPOT.BK","HPT.BK","HPT-R.BK","HTC.BK","HTC-R.BK","HYDRO.BK","HYDRO-R.BK","ICC-R.BK","ICC.BK","ICHI-R.BK","IEC.BK","IEC-R.BK","IFEC-R.BK","IFEC.BK","IFS.BK","IHL.BK","IHL-R.BK","ILINK.BK","ILINK-R.BK","IRPC-R.BK","IRPC.BK","IRCP.BK","IRC-R.BK","IRCP-R.BK","IRC.BK","ITD-R.BK","ITD.BK","IT.BK","IT-R.BK","LIT.BK","LIT-R.BK","IVL.BK","IVL-R.BK","JAS-R.BK","JAS.BK","JCT-R.BK","JCP.BK","JMART-R.BK","JMT.BK","JSP.BK","JSP-R.BK","JTS-R.BK","JUTHA-R.BK","JUTHA.BK","JUBILE-R.BK","JWD-R.BK","KAMART.BK","KASET-R.BK","KTIS.BK","KTIS-R.BK","KAMART-R.BK","KBS.BK","KBANK-R.BK","KBANK.BK","KBS-R.BK","KCE-R.BK","KCM-R.BK","KCM.BK","KCAR.BK","KC-R.BK","KCE.BK","KCAR-R.BK","KDH.BK","KDH-R.BK","KGI-R.BK","K-R.BK","KIAT-R.BK","K.BK","KIAT.BK","KKP.BK","KKP-R.BK","KKC-R.BK","KKC.BK","NPK.BK","KOOL.BK","KOOL-R.BK","KSL-R.BK","KSL.BK","KTP.BK","KTECH-R.BK","KTB-R.BK","KTECH.BK","KWC.BK","LALIN-R.BK","LANNA-R.BK","LALIN.BK","LANNA.BK","LDC.BK","LDC-R.BK","LEE.BK","TTLPF.BK","MTLS-R.BK","MTLS.BK","LEE-R.BK","LH-R.BK","LHBANK-R.BK","LHBANK.BK","LHK.BK","LHK-R.BK","LH.BK","TMI-R.BK","SR-R.BK","SPVI.BK","SPCG.BK","SMPC.BK","PPP.BK","MEGA.BK","COLOR.BK","PTG-R.BK","SYMC.BK","INSURE-R.BK","SPA.BK","NDR.BK","TTCL.BK","SAWAD-R.BK","SR.BK","SPVI-R.BK","MONO.BK","SCN.BK","SMART.BK","NUSA-R.BK","THANA.BK","HOTPOT-R.BK","LOXLEY.BK","LOXLEY-R.BK","NCL-R.BK","WICE-R.BK","WICE.BK","NCL.BK","LPN-R.BK","LPN.BK","LRH-R.BK","LRH.BK","LST.BK","LST-R.BK","LUXF.BK","LVT-R.BK","LVT.BK","MALEE-R.BK","PM-R.BK","MAJOR-R.BK","MANRIN.BK","MANRIN-R.BK","MACO.BK","MATI.BK","MAX.BK","PCSGH.BK","MBKET.BK","MBAX.BK","MBK.BK","MBK-R.BK","MBKET-R.BK","MBAX-R.BK","MCS.BK","MC-R.BK","MCOT.BK","MCOT-R.BK","MCS-R.BK","MC.BK","MDX.BK","MDX-R.BK","METCO.BK","PLANB-R.BK","2S.BK","2S-R.BK","MFEC-R.BK","MFC-R.BK","M-II.BK","MNIT.BK","MFEC.BK","MFC.BK","SMT.BK","MINT.BK","MJD.BK","MJD-R.BK","M.BK","MK.BK","MK-R.BK","M-R.BK","ML.BK","ML-R.BK","MNIT2.BK","MNRF.BK","MONTRI.BK","MONO-R.BK","MOONG-R.BK","PIMO-R.BK","MODERN.BK","MODERN-R.BK","MOONG.BK","PIMO.BK","MPIC-R.BK","MPG.BK","MPIC.BK","MPG-R.BK","MSC-R.BK","MSC.BK","MTI.BK","MTI-R.BK","NYT-R.BK","NBC.BK","NYT.BK","NBC-R.BK","NCH.BK","NC.BK","NCH-R.BK","NC-R.BK","NDR-R.BK","NEWS.BK","NEW.BK","NEP.BK","NEWS-R.BK","NEW-R.BK","NKI.BK","NKI-R.BK","NMG-R.BK","NMG.BK","NNCL-R.BK","NNCL.BK","NOBLE-R.BK","NOBLE.BK","NPP.BK","NPP-R.BK","NSI.BK","NSI-R.BK","NTV-R.BK","NTV.BK","NUSA.BK","NWR-R.BK","NWR.BK","OCEAN-R.BK","OCC.BK","OCEAN.BK","OCC-R.BK","SIRIP.BK","OGC.BK","OGC-R.BK","OHTL-R.BK","OHTL.BK","SEAOIL.BK","VPO-R.BK","SEAOIL-R.BK","OISHI.BK","OISHI-R.BK","VPO.BK","OTO.BK","OTO-R.BK","ORI.BK","ORI-R.BK","PPF.BK","SINGHA.BK","SPWPF.BK","PJW.BK","PAF.BK","PAP-R.BK","PB.BK","PB-R.BK","PDI-R.BK","PDG.BK","PDG-R.BK","PDI.BK","PERM-R.BK","PERM.BK","PE.BK","SPRC.BK","PE-R.BK","PF.BK","PF-R.BK","PG.BK","PG-R.BK","PICO-R.BK","PICO.BK","PJW-R.BK","PK-R.BK","PK.BK","PLE.BK","PPS.BK","RICHY.BK","PLAT.BK","PM.BK","POLAR-R.BK","SMC.BK","POLAR.BK","TPOLY-R.BK","PSTC-R.BK","TPCH-R.BK","TPOLY.BK","PSTC.BK","POST-R.BK","POST.BK","SAWAD.BK","PPM.BK","PPS-R.BK","PPP-R.BK","PPM-R.BK","PRG-R.BK","TRS-R.BK","PRG.BK","PR-R.BK","PRAKIT-R.BK","TLHPF.BK","PRECHA-R.BK","SLP.BK","SLP-R.BK","PRAKIT.BK","PR.BK","PREB.BK","PRIN-R.BK","PSL-R.BK","PS.BK","PS-R.BK","PSL.BK","PTT.BK","PTTE06P1602A.BK","PTL.BK","PTTEP-R.BK","PTTEP.BK","PTTGC.BK","PTL-R.BK","PT-R.BK","PTT-R.BK","PTTGC-R.BK","PT.BK","PACE-R.BK","TSR.BK","SAFARI.BK","PLAT-R.BK","TSI-R.BK","TNP.BK","TMI.BK","MEGA-R.BK","TT-R.BK","SMT-R.BK","WHA-R.BK","COM7.BK","INSURE.BK","ROCK.BK","SPCG-R.BK","TACC.BK","THANA-R.BK","COM7-R.BK","COLOR-R.BK","TMC.BK","TSE.BK","WORLD.BK","VTE.BK","SENA-R.BK","RWI-R.BK","VI-R.BK","SAPPE.BK","TT&T-R.BK","WINNER.BK","WP-R.BK","S11-R.BK","UWC.BK","COL.BK","WP.BK","TNP-R.BK","WINNER-R.BK","VTE-R.BK","TSE-R.BK","GREEN-R.BK","TPROP.BK","TAKUNI.BK","SMPC-R.BK","TTCL-R.BK","SAFARI-R.BK","BRC-R.BK","TWPC.BK","TACC-R.BK","SAPPE-R.BK","ROCK-R.BK","CHOW-R.BK","FIRE-R.BK","RICHY-R.BK","TSR-R.BK","PLANB.BK","TMC-R.BK","TAKUNI-R.BK","VI.BK","SYMC-R.BK","TVT-R.BK","SMART-R.BK","SCN-R.BK","VIH-R.BK","TVT.BK","TSI.BK","SENA.BK","BEAUTY.BK","RWI.BK","WR-R.BK","S11.BK","COL-R.BK","ADAM.BK","TU-R.BK","PYLON-R.BK","PYLON.BK","RAM-R.BK","RATCH-R.BK","RAM.BK","RATCH.BK","RCI-R.BK","RCL-R.BK","RCI.BK","RCL.BK","RICH.BK","RICH-R.BK","RML-R.BK","RML.BK","ROH.BK","ROH-R.BK","ROJNA.BK","ROJNA-R.BK","ROBINS-R.BK","ROBINS.BK","RPC.BK","RPC-R.BK","RS.BK","RS-R.BK","SAT.BK","SAM-R.BK","SALEE-R.BK","SAM.BK","SABINA.BK","SAMART.BK","SAMTEL.BK","SAWANG.BK","SALEE.BK","SAT-R.BK","SCC.BK","SCB.BK","SCG.BK","SCC-R.BK","SCP-R.BK","SCCC-R.BK","SCCC.BK","SC-R.BK","SCG-R.BK","SCP.BK","SCB-R.BK","SC.BK","SF-R.BK","SF.BK","SGP.BK","SGP-R.BK","SHANG-R.BK","SHANG.BK","SINGER-R.BK","SIRI-R.BK","SIAM.BK","SIMAT-R.BK","SITHAI-R.BK","SIM.BK","SITHAI.BK","SIAM-R.BK","SIMAT.BK","SIM-R.BK","SIS.BK","SIRI.BK","SINGER.BK","SIS-R.BK","SKR.BK","SKR-R.BK","SMK-R.BK","SMIT-R.BK","SMG-R.BK","SMK.BK","SMIT.BK","SMM.BK","SMG.BK","SMM-R.BK","SNP.BK","SNP-R.BK","SNC.BK","SNC-R.BK","SOLAR.BK","SORKON.BK","SOLAR-R.BK","SPORT.BK","SPPT-R.BK","SPI-R.BK","SPORT-R.BK","SPALI-R.BK","SPACK-R.BK","SPG.BK","SPI.BK","SPC-R.BK","SPC.BK","SRICHA.BK","SRICHA-R.BK","SST-R.BK","SSSC-R.BK","SSI-R.BK","SSF.BK","SSC-R.BK","SSC.BK","SSI.BK","SSSC.BK","SSTPF.BK","SST.BK","SSF-R.BK","STEC-R.BK","STANLY.BK","STAR.BK","STEC.BK","STPI-R.BK","STAR-R.BK","STA.BK","STA-R.BK","SUSCO.BK","SUPER.BK","SUPER-R.BK","SUSCO-R.BK","SUC-R.BK","SUC.BK","SVI-R.BK","SVOA-R.BK","SVI.BK","SVH-R.BK","SVOA.BK","SWC.BK","SWC-R.BK","SYNEX.BK","SYNTEC-R.BK","SYNEX-R.BK","SYNTEC.BK","TAPAC.BK","TAPAC-R.BK","TASCO.BK","TASCO-R.BK","TBSP.BK","TBSP-R.BK","TCAP.BK","TCCC-R.BK","TCOAT-R.BK","TCB-R.BK","TC-R.BK","TCMC-R.BK","TCC-R.BK","TCIF.BK","TCB.BK","TCAP-R.BK","TC.BK","TCJ-R.BK","TCMC.BK","TCCC.BK","TCJ.BK","TCC.BK","TCOAT.BK","TEAM.BK","TFI.BK","TFUND.BK","TF-R.BK","TFI-R.BK","TFD-R.BK","TFD.BK","TF.BK","TGCI.BK","TGCI-R.BK","TGROWTH.BK","TGPRO-R.BK","TGPRO.BK","INTUCH.BK","TU.BK","TTW.BK","TRUE.BK","TMT.BK","TKT.BK","TKS-R.BK","TK-R.BK","THAI.BK","TIW-R.BK","SAUCE-R.BK","TPA-R.BK","TKS.BK","TNH.BK","BAFS-R.BK","TPP.BK","SPACK.BK","PRANDA-R.BK","L&E-R.BK","TNDT.BK","PATO-R.BK","TRT.BK","LIVE.BK","MILL-R.BK","TMW-R.BK","TVI.BK","TNITY.BK","BAFS.BK","DEMCO.BK","TOP-R.BK","TUF.BK","TMD-R.BK","UV-R.BK","TPAC.BK","BAT-3K-R.BK","UMS.BK","THE-R.BK","SE-ED-R.BK","SEAFCO-R.BK","SEAFCO.BK","MAJOR.BK","UKEM.BK","TLUXE.BK","TPAC-R.BK","LTX-R.BK","WACOAL-R.BK","MATCH.BK","TIW.BK","SPG-R.BK","TH-R.BK","TIPCO.BK","TTI.BK","GRAND.BK","TICON.BK","TNL.BK","TWP.BK","TWFP.BK","INET.BK","TNH-R.BK","TVO-R.BK","A.BK","TRT-R.BK","MATI-R.BK","MATCH-R.BK","UKEM-R.BK","TSC.BK","UTP-R.BK","TTA.BK","THREL-R.BK","TR.BK","TPC.BK","F&D.BK","UBIS-R.BK","F&D-R.BK","TTL-R.BK","TWZ.BK","TVI-R.BK","TYCN.BK","S-&-J-R.BK","TEAM-R.BK","TPA.BK","U.BK","TMD.BK","TRC.BK","THRE-R.BK","GBX-R.BK","UOBKH.BK","UP-R.BK","INOX.BK","TT.BK","SAUCE.BK","TWZ-R.BK","TSTE-R.BK","T-R.BK","PL-R.BK","TKT-R.BK","TNPC-R.BK","TLUXE-R.BK","VIBHA-R.BK","TOPP.BK","THAI-R.BK","TOG.BK","INOX-R.BK","S-&-J.BK","GRAND-R.BK","VNT.BK","E-R.BK","TTW-R.BK","TIP-R.BK","UPOIC.BK","TSF.BK","SAMTEL-R.BK","TNPC.BK","TTL.BK","WAVE-R.BK","VNG-R.BK","UVAN-R.BK","UT-R.BK","TRC-R.BK","UEC-R.BK","THANI.BK","PRIN.BK","KYE.BK","SPPT.BK","STANLY-R.BK","TSTE.BK","TRUBB.BK","TIC-R.BK","TISCO-R.BK","TIPCO-R.BK","TIC.BK","TICON-R.BK","TIP.BK","TISCO.BK","TK.BK","TMT-R.BK","TMB-R.BK","TMB.BK","TMW.BK","TNL-R.BK","TNDT-R.BK","TNITY-R.BK","TOP.BK","TOG-R.BK","TOPP-R.BK","TPIPL.BK","TPCORP.BK","TPP-R.BK","TPC-R.BK","TPBI-R.BK","TPIPL-R.BK","TPCORP-R.BK","TPBI.BK","TRUBB-R.BK","TRS.BK","TSC-R.BK","TSTH.BK","TSTH-R.BK","TSF-R.BK","TTI-R.BK","TTTM-R.BK","TTA-R.BK","TTTM.BK","TUF-R.BK","TVO.BK","TWP-R.BK","TYCN-R.BK","UBIS.BK","UEC.BK","UMI-R.BK","UMS-R.BK","UMI.BK","UNIQ-R.BK","UOBKH-R.BK","UPF.BK","UPOIC-R.BK","UP.BK","UT.BK","UTP.BK","UVAN.BK","UV.BK","VARO-R.BK","VNT-R.BK","VNG.BK","PRO.BK","WAVE.BK","PRO-R.BK","WACOAL.BK","WG-R.BK","WIIK-R.BK","WIN.BK","WORK-R.BK","WORK.BK","BANPU-R.BK","BANPU.BK","BAT-3K.BK","BAY-R.BK","BEC.BK","BEM-R.BK","BROOK-R.BK","CHARAN.BK","CHARAN-R.BK","CHOTI.BK","CHOTI-R.BK","CNS-R.BK","DELTA-R.BK","DEMCO-R.BK","THIF.BK","GBX.BK","GRAMMY-R.BK","GREEN.BK","INTUCH-R.BK","KYE-R.BK","LIVE-R.BK","LTX.BK","MACO-R.BK","MAKRO.BK","MAKRO-R.BK","MALEE.BK","MAX-R.BK","METCO-R.BK","MIDA.BK","MIDA-R.BK","MILL.BK","MINT-R.BK","PAE-R.BK","PAE.BK","PAF-R.BK","PAP.BK","PATO.BK","PLE-R.BK","PRANDA.BK","PRECHA.BK","PREB-R.BK","PRINC-R.BK","PRINC.BK","SABINA-R.BK","SAMCO-R.BK","SAMART-R.BK","SAMCO.BK","SAWANG-R.BK","SORKON-R.BK","SPALI.BK","SPF.BK","STPI.BK","THANI-R.BK","THCOM-R.BK","THCOM.BK","THE.BK","THIP-R.BK","THIP.BK","THREL.BK","THRE.BK","TRU.BK","TRUE-R.BK","TRU-R.BK","INET-R.BK"]


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

