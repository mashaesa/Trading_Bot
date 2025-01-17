import time
import hmac
import hashlib
import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("WOOX_API_KEY")
API_SECRET = os.getenv("WOOX_API_SECRET")

def get_timestamp():
    """Generate 13 digit Unix timestamp in milliseconds"""
    return str(int(time.time() * 1000))

def create_signature(api_secret, content):
    """Generate HMAC signature"""
    return hmac.new(
        api_secret.encode('utf-8'),
        content.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

def fetch_trade_history(symbol="PERP_POWR_USDT", start_time=None, end_time=None, page=1, size=25):
    """Fetch trade history for the last 6 months"""
    base_url = "https://api.woox.io/v1/client/trades"
    
    query_params = {
        "symbol": symbol,
        "start_t": start_time or get_timestamp(),
        "end_t": end_time or get_timestamp(),
        "page": page,
        "size": size
    }
    
    query_string = "&".join(f"{key}={value}" for key, value in sorted(query_params.items()) if value)
    
    timestamp = get_timestamp()
    content_to_sign = f"{query_string}|{timestamp}"
    signature = create_signature(API_SECRET, content_to_sign)
    
   
    headers = {
        "x-api-key": API_KEY,
        "x-api-signature": signature,
        "x-api-timestamp": timestamp,
        "Content-Type": "application/json"
    }
    
    # debug any prints
    print("Request URL:", base_url)
    print("Headers:", headers)
    print("Query String:", query_string)
    print("Signature String:", content_to_sign)
    print("Signature:", signature)
    
    # Send the request
    try:
        response = requests.get(base_url, headers=headers, params=query_params)
        print("Response Status Code:", response.status_code)
        print("Response Content:", response.text)  
        response.raise_for_status()  # Raise error for non-2xx HTTP codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

start_time = str(int((time.time() - 180 * 24 * 60 * 60) * 1000))  # 180days ago in milliseconds!!
end_time = get_timestamp() 
result = fetch_trade_history(start_time=start_time, end_time=end_time)

if result:
    print("Trade History:", result)
else:
    print("Failed to fetch trade history.")
