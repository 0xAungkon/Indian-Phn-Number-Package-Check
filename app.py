
from fastapi import FastAPI,Request
from fastapi import FastAPI, UploadFile, File,Request
from fastapi.responses import *
import uvicorn
import requests
import os
import io
import json
import urllib.parse
# %%
import time
from fastapi import FastAPI,Form
import os 
import requests


app = FastAPI()

def get_phn_packages(phn):
    try:
        headers = {
            'X-MClient': '0',
            'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
            'DNT': '1',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Referer': 'https://www.mobikwik.com/',
            'sec-ch-ua-platform': '"Linux"',
        }

        response = requests.get(
            'https://rapi.mobikwik.com/recharge/v1/rechargePlansAPI/140/19?cn='+phn+'&languageRegionId=:languageRegionId',
            headers=headers,
        )

        return response.text
    except Exception as e:
        print('Error',str(e))
        return False

def get_phn_oparator(phn):
    headers = {
        'X-MClient': '0',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'DNT': '1',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Referer': 'https://www.mobikwik.com/',
        'sec-ch-ua-platform': '"Linux"',
    }
    params = {
        'cn': phn,
    }
    response = requests.get('https://rapi.mobikwik.com/recharge/infobip/getconnectiondetails', params=params, headers=headers)
    return response.text

def get_dth_plans(phn):


    headers = {
        'X-MClient': '0',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'DNT': '1',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Referer': 'https://www.mobikwik.com/',
        'sec-ch-ua-platform': '"Linux"',
    }

    response = requests.get(
        'https://rapi.mobikwik.com/recharge/v1/rechargePlansAPI/23?cn='+phn+'&languageRegionId=:languageRegionId',
        headers=headers,
    )
    return response.text
def get_electricity_bill(cn,op):
    headers = {
        'X-MClient': '0',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'DNT': '1',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'Content-Type': 'application/json',
        'Accept': 'application/json, text/plain, */*',
        'Referer': 'https://www.mobikwik.com/',
        'sec-ch-ua-platform': '"Linux"',
    }

    json_data = {
        'adParams': {},
        'op': op,
        'cn': cn,
    }

    response = requests.post('https://rapi.mobikwik.com/recharge/v1/viewpayment', headers=headers, json=json_data)
    return response.text

@app.get("/")
def root():
  return {
            'Electricity Oparators':{"0":"Adani Electricity Mumbai Limited","1":"M.P. Madhya Kshetra Vidyut Vitaran - URBAN","2":"Uttar Haryana Bijli Vitran Nigam Limited Prepaid","3":"Power and Electricity Department - Mizoram","4":"TP Southen Odisha Distribution Ltd-Smart Prepaid Meter Recharge","5":"Dadra and Nagar Haveli and Daman and Diu Power Distribution Corporation Limited","6":"India Power Corporation Limited (IPCL)","7":"Purvanchal Vidyut Vitran Nigam Limited(PUVVNL)(Postpaid and Smart Prepaid Meter Recharge)","8":"Hukkeri Rural Electric CoOperative Society Ltd","9":"Western Electricity Supply Company Of Odisha Limited","10":"TP Renewables Microgrid Ltd.","11":"Central Power Distribution Corporation Ltd. of Andhra Pradesh (APCPDCL)","12":"India Power Corporation - West Bengal","13":"India Power Corporation - Bihar","14":"BSES Rajdhani Prepaid Meter Recharge","15":"BSES Yamuna Prepaid Meter Recharge","16":"Jharkhand Bijli Vitran Nigam Limited - Prepaid Meter Recharge","17":"Dakshinanchal Vidyut Vitran Nigam Limited (DVVNL)(Postpaid and Smart Prepaid Meter Recharge)","18":"Madhyanchal Vidyut Vitran Nigam Limited (MVVNL)(Postpaid and Smart Prepaid Meter Recharge)","19":"MePDCL Smart Prepaid Meter Recharge","20":"Vaghani Energy Limited","21":"M.P. Madhya Kshetra Vidyut Vitaran - RURAL","22":"Ajmer Vidyut Vitran Nigam Limited (AVVNL)","23":"Assam Power Distribution Company Ltd (NON-RAPDR)","24":"Assam Power Distribution Company Ltd (RAPDR)","25":"Bangalore Electricity Supply Co. Ltd (BESCOM)","26":"B.E.S.T Mumbai","27":"Bhagalpur Electricity Distribution Company (P) Ltd","28":"Bharatpur Electricity Services Ltd. (BESL)","29":"Bikaner Electricity Supply Limited (BkESL)","30":"BSES Rajdhani Power Limited","31":"BSES Yamuna Power Limited","32":"Calcutta Electric Supply Corporation (CESC)","33":"TP Central Odisha Distribution Limited - TPCODL","34":"Chamundeshwari Electricity Supply Corp Ltd (CESCOM)","35":"Chhattisgarh State Power Distribution Co. Ltd","36":"Dakshin Gujarat Vij Company Limited (DGVCL)","37":"Dakshin Haryana Bijli Vitran Nigam (DHBVN)","38":"Daman and Diu Electricity","39":"DNHPDCL - DADRA & NAGAR HAVELI","40":"Paschimanchal Vidyut Vitran Nigam Limited (PVVNL)(Postpaid and Smart Prepaid Meter Recharge)","41":"Department of Power, Government of Arunachal Pradesh","42":"Department of Power, Government of Arunachal Pradesh - Prepaid","43":"Department of Power, Nagaland","44":"DNH Power Distribution Company Limited","45":"Electricity Department Chandigarh","46":"Gift Power Company Limited","47":"Goa Electricity Department","48":"Government of Puducherry Electricity Department","49":"Gulbarga Electricity Supply Company Limited","50":"Himachal Pradesh State Electricity Board","51":"Hubli Electricity Supply Company Ltd (HESCOM)","52":"Jamshedpur Utilities","53":"Jharkhand Bijli Vitran Nigam Limited (JBVNL)","54":"Jaipur Vidyut Vitran Nigam Ltd","55":"Jammu and Kashmir Power Development Department","56":"Jodhpur Vidyut Vitran Nigam Limited (JDVVNL)","57":"Kannan Devan Hills Plantations Company Private Limited","58":"Kanpur Electricity Supply Company Ltd","59":"Kerala State Electricity Board Ltd. (KSEBL)","60":"APEPDCL - Eastern Power Distribution CO AP Ltd.","61":"APSPDCL - Southern Power Distribution CO AP Ltd.","62":"Kota Electricity Distribution Limited (KEDL)","63":"Lakshadweep Electricity Department","64":"Madhya Gujarat Vij Company Limited (MGVCL)","65":"Madhya Pradesh Paschim Kshetra Vidyut Vitaran","66":"Madhya Pradesh Poorv Kshetra Vidyut Vitaran-RURAL","67":"Maharashtra State Electricity Distbn Co Ltd","68":"Meghalaya Power Dist Corp Ltd","69":"Mangalore Electricity Supply Co. Ltd (MESCOM) – RAPDR","70":"Mangalore Electricity Supply Company LTD (Non RAPDR)","71":"NESCO, Odisha","72":"New Delhi Municipal Council (NDMC)","73":"Noida Power","74":"North Bihar Power Distribution Company Ltd.","75":"Paschim Gujarat Vij Company Limited (PGVCL)","76":"Punjab State Power Corporation Ltd (PSPCL)","77":"Sikkim Power-RURAL","78":"Sikkim Power - URBAN","79":"South Bihar Power Distribution Company Ltd.","80":"TP Southern Odisha Distribution Limited","81":"Tamil Nadu Electricity Board (TNEB)","82":"Tata Power - Delhi","83":"Tata Power - Mumbai","84":"Thrissur Corporation Electricity Department","85":"Torrent power","86":"TP Ajmer Distribution Ltd (TPADL)","87":"Tripura Electricity Corp Ltd","88":"Uttar Gujarat Vij Company Limited (UGVCL)","89":"Uttar Haryana Bijli Vitran Nigam (UHBVN)","90":"Uttar Pradesh Power Corp Ltd (UPPCL) - RURAL","91":"Uttarakhand Power Corporation Limited","92":"WESCO Utility","93":"Spurt Electric Limited","94":"West Bengal State Electricity Distribution Co. Ltd"},
            'DTH Oparators':{"Airtel DTH":0,
                "Dish TV":1,
                "Sun Direct TV":2,
                "Tata Play":3,
                "d2h":4,
            },
            'Sim Oparator':{
                "0":"Airtel",
                "1":"BSNL",
                "2":"Jio",
                "3":"MTNL",
                "4":"Vi",
                "5":"Tata Docomo CDMA Postpaid"
            }
        }

@app.get("/get_phn_packages/")
async def get_phn_packages_main(phn):
    return json.loads(get_phn_packages(phn))

@app.get("/get_phn_oparator/")
async def get_phn_oparator_main(phn):
    return json.loads(get_phn_oparator(phn))

@app.get("/get_dth_plans/")
async def get_dth_plans_main(phn):
    return json.loads(get_dth_plans(phn))

@app.get("/get_electricity_bill/")
async def get_electricity_bill_main(cn,op):
    return json.loads(get_electricity_bill(cn,op))


# https://example-ip.com/get_phn_packages/?phn={PHN}
# https://example-ip.com/get_phn_oparator/?phn={PHN}
# https://example-ip.com/get_dth_plans/?phn={PHN}
# https://example-ip.com/get_electricity_bill/?cn={CN}&op={OP}


if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=8000)

# %%
