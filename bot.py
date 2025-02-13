from web3 import Web3
from blockchain.analyzer import analyze_address
from ai.ollama_ai import generate_analysis
from config import FLAGGED_ADDRESSES
from config import INFURA_URL

web3 = Web3(Web3.HTTPProvider(f'''{INFURA_URL}'''))

def detect_address_type(address):
    """Determine if address is contract or EOA with additional checks"""
    if not web3.is_address(address):
        return "invalid"
    
    checksum_addr = web3.to_checksum_address(address)
    code = web3.eth.get_code(checksum_addr)
    
    if code.hex() != '0x':
        return "contract"
    return "wallet"

def format_flagged_status(address):
    """Check if address is flagged in config"""
    checksum_addr = web3.to_checksum_address(address)
    return FLAGGED_ADDRESSES.get(checksum_addr, None)

while True:
    user_input = input("\n💬 You: ").strip()
    
    if user_input.lower() in ["exit", "quit"]:
        print("👋 Later, anon. Stay based!")
        break

    if web3.is_address(user_input):
        address_type = detect_address_type(user_input)
        flagged_status = format_flagged_status(user_input)
        
        if address_type == "invalid":
            print("🤖 Not a valid ETH address, ser. Try again.")
            continue
            
        analysis_data = analyze_address(user_input, address_type)
        
        if "error" in analysis_data:
            print(f"\n🤖 Bot: {analysis_data['error']}")
            continue
            
        response = generate_analysis(analysis_data, address_type, flagged_status)
        
    else:
        response = generate_analysis(user_input, "query")
    
    print(f"\n🤖 Bot: {response}")