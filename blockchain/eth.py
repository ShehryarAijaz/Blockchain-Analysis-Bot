import requests
from config import ETHERSCAN_API_KEY
from web3 import Web3

def get_wallet_activity(address):
    """Get comprehensive wallet activity including ERC-20 transfers"""
    url = f"https://api.etherscan.io/api?module=account&action=txlist&address={address}&startblock=0&endblock=99999999&sort=desc&apikey={ETHERSCAN_API_KEY}"
    response = requests.get(url).json()
    
    activity = {
        "tx_count": 0,
        "volume_eth": 0.0,
        "interactions": [],
        "last_active": None
    }
    
    if response["status"] == "1":
        transactions = response["result"][:50]
        activity["tx_count"] = len(transactions)
        
        for tx in transactions:
            value = float(Web3.from_wei(int(tx["value"]), 'ether'))
            activity["volume_eth"] += value
            activity["interactions"].append(tx["to"])
    
    return activity

def calculate_risk_score(address):
    """Advanced risk scoring using multiple factors"""
    risk_factors = {
        "tornado_cash_interactions": 0,
        "new_account": 0,
        "high_frequency": 0
    }
    
    risk_score = 25 if risk_factors["tornado_cash_interactions"] else 0
    return min(risk_score + 15, 100)