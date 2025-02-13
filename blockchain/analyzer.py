from .eth import get_wallet_activity, calculate_risk_score
from .tokens import get_token_metrics
from web3 import Web3

def analyze_address(address, address_type):
    """Collect comprehensive blockchain data for analysis"""
    checksum_addr = Web3.to_checksum_address(address)
    analysis = {"address": checksum_addr, "type": address_type}
    
    if address_type == "wallet":
        analysis.update(get_wallet_activity(checksum_addr))
        analysis["risk_score"] = calculate_risk_score(checksum_addr)
    elif address_type == "contract":
        token_data = get_token_metrics(checksum_addr)
        if not token_data["is_token"]:
            return {
                **analysis,
                "error": "This contract doesn't appear to be a token. Might be a DApp or other contract."
            }
        analysis.update(token_data)
    
    return analysis