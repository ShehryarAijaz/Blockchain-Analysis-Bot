from blockchain.eth import fetch_wallet_data

def get_risk_score(address):
    wallet_data, risk_score = fetch_wallet_data(address)

    if "0x905b63fff465b9ffbf41dea908ceb12478ec7603a" in wallet_data:
        risk_score += 30  

    for line in wallet_data.split("\n"):
        if "ETH" in line:
            value = float(line.split("|")[1].replace("ETH", "").strip())
            if value > 100:
                risk_score += 20  

    return min(risk_score, 100)