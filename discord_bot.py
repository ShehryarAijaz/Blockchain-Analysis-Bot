import discord
from discord.ext import commands
from web3 import Web3
from blockchain.analyzer import analyze_address
from ai.ollama_ai import generate_analysis
from config import FLAGGED_ADDRESSES, INFURA_URL, DISCORD_KEY

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

web3 = Web3(Web3.HTTPProvider(f'''{INFURA_URL}'''))

@bot.command()
async def analyze(ctx, address: str):
    """Analyze an Ethereum address and return a summary."""
    
    if not web3.is_address(address):
        await ctx.send("🤖 Not a valid ETH address, ser. Try again.")
        return

    address_type = detect_address_type(address)
    flagged_status = format_flagged_status(address)

    if address_type == "invalid":
        await ctx.send("🤖 Not a valid ETH address, ser. Try again.")
        return
    
    analysis_data = analyze_address(address, address_type)
    
    if "error" in analysis_data:
        await ctx.send(f"🤖 Bot: {analysis_data['error']}")
        return

    response = generate_analysis(analysis_data, address_type, flagged_status)
    await ctx.send(f"🤖 Bot: {response}")

@bot.command()
async def ask(ctx, *, question: str):
    """Handle free-form questions and return an analysis."""
    response = generate_analysis(question, "query")
    await ctx.send(f"🤖 Bot: {response}")

def detect_address_type(address):
    """Determine if the address is a contract or an EOA."""
    if not web3.is_address(address):
        return "invalid"
    
    checksum_addr = web3.to_checksum_address(address)
    code = web3.eth.get_code(checksum_addr)
    
    if code.hex() != '0x':
        return "contract"
    return "wallet"

def format_flagged_status(address):
    """Check if the address is flagged in the config file."""
    checksum_addr = web3.to_checksum_address(address)
    return FLAGGED_ADDRESSES.get(checksum_addr, None)

bot.run(f'''{DISCORD_KEY}''')
