import time, hmac, hashlib, json, requests
import os

API_KEY = os.getenv("XT_API_KEY")
API_SECRET = os.getenv("XT_API_SECRET")

BASE_URL = "https://www.xt.com"

def get_server_time():
    return str(int(time.time() * 1000))

def create_signature(secret, method, path, timestamp, query_string=''):
    payload = f"{timestamp}{method.upper()}{path}{query_string}"
    return hmac.new(secret.encode(), payload.encode(), hashlib.sha256).hexdigest()

def get_balance():
    path = "/api/v4/balance"
    url = BASE_URL + path
    timestamp = get_server_time()
    signature = create_signature(API_SECRET, "GET", path, timestamp)
    
    headers = {
        "Content-Type": "application/json",
        "X-ACCESS-KEY": API_KEY,
        "X-ACCESS-SIGN": signature,
        "X-ACCESS-TIMESTAMP": timestamp
    }
    
    res = requests.get(url, headers=headers)
    print(res.json())

if __name__ == "__main__":
    get_balance()
