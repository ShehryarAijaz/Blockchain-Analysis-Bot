import requests
from config import ETHERSCAN_API_KEY
from web3 import Web3
import time

def get_dexscreener_data(address):
    """Safe DexScreener API call with retries and error handling"""
    url = f"https://api.dexscreener.com/latest/dex/tokens/{address}"
    retries = 3
    backoff = 1
    
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if isinstance(data, dict) and "pairs" in data:
                return data
            
            return {"pairs": []}
            
        except Exception as e:
            if attempt == retries - 1:
                return {"pairs": []}
            time.sleep(backoff * (attempt + 1))
    
    return {"pairs": []}


def get_token_metrics(address):
    """Get comprehensive token metrics with proper error handling"""
    metrics = {
        "liquidity": 0.0,
        "volume_24h": 0.0,
        "holders": 0,
        "price_change": 0.0,
        "lock_status": "unknown",
        "is_token": False
    }
    
    dex_data = get_dexscreener_data(address)
    
    if not dex_data or not isinstance(dex_data, dict) or "pairs" not in dex_data:
        dex_data = {"pairs": []}
    
    if dex_data and "pairs" in dex_data:
        metrics["is_token"] = len(dex_data["pairs"]) > 0
        
        if metrics["is_token"]:
            pair = dex_data["pairs"][0]
            metrics.update({
                "liquidity": float(pair.get("liquidity", {}).get("usd", 0)),
                "volume_24h": float(pair.get("volume", {}).get("h24", 0)),
                "price_change": float(pair.get("priceChange", {}).get("h24", 0)),
                "lock_status": "🔒 Locked" if pair.get("liquidity", {}).get("locked", False) else "🔓 Unlocked"
            })
    
    etherscan_url = f"https://api.etherscan.io/api?module=token&action=tokenholderlist&contractaddress={address}&apikey={ETHERSCAN_API_KEY}"
    try:
        holder_data = requests.get(etherscan_url, timeout=10).json()
        if holder_data.get("status") == "1" and holder_data.get("result"):
            metrics["holders"] = len(holder_data["result"])
    except:
        pass
    
    return metrics
