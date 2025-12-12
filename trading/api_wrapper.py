import requests
import json
import os
from django.conf import settings
from typing import Dict, Any, Optional

class KoreaInvestmentAPI:
    """
    Wrapper for Korea Investment Securities API (KIS API).
    """
    BASE_URL = "https://openapi.koreainvestment.com:9443"  # Real (Use simulation URL for testing if needed)
    # Simulation URL: https://openapivts.koreainvestment.com:29443
    
    def __init__(self):
        self.app_key = os.getenv('API_KEY')
        self.app_secret = os.getenv('API_SECRET')
        self.account_number = os.getenv('ACCOUNT_NUMBER')
        self.access_token = None
        
        if not self.app_key or not self.app_secret:
            print("WARNING: API_KEY or API_SECRET not set in environment.")

    def get_access_token(self) -> Optional[str]:
        """
        Request OAuth access token.
        """
        path = "oauth2/tokenP"
        url = f"{self.BASE_URL}/{path}"
        headers = {"content-type": "application/json"}
        body = {
            "grant_type": "client_credentials",
            "appkey": self.app_key,
            "appsecret": self.app_secret
        }
        
        try:
            res = requests.post(url, headers=headers, data=json.dumps(body))
            if res.status_code == 200:
                data = res.json()
                self.access_token = data.get('access_token')
                return self.access_token
            else:
                print(f"Error getting token: {res.text}")
                return None
        except Exception as e:
            print(f"Exception requesting token: {e}")
            return None

    def get_current_price(self, code: str) -> Dict[str, Any]:
        """
        Get current price for a stock code.
        """
        if not self.access_token:
            self.get_access_token()
            
        path = "uapi/domestic-stock/v1/quotations/inquire-price"
        url = f"{self.BASE_URL}/{path}"
        
        headers = {
            "content-type": "application/json",
            "authorization": f"Bearer {self.access_token}",
            "appkey": self.app_key,
            "appsecret": self.app_secret,
            "tr_id": "FHKST01010100"  # Transaction ID for current price
        }
        
        params = {
            "fid_cond_mrkt_div_code": "J",
            "fid_input_iscd": code
        }
        
        try:
            res = requests.get(url, headers=headers, params=params)
            if res.status_code == 200:
                return res.json().get('output', {})
            else:
                print(f"Error getting price: {res.text}")
                return {}
        except Exception as e:
            print(f"Exception requesting price: {e}")
            return {}
