import os
from dotenv import load_dotenv

load_dotenv()

INFURA_URL = os.getenv("INFURA_URL")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
ETHERSCAN_API_KEY= os.getenv("ETHERSCAN_API_KEY")
DISCORD_KEY = os.getenv("DISCORD_KEY")

# Flagged scam wallets
FLAGGED_ADDRESSES = {
    "0x5aAeb6053F3E94C9b9A09f33669435E7Ef1BeAed": "Known Scam",
    "0x742d35Cc6634C0532925a3b844Bc454e4438f44e": "Exchange Wallet",
}
