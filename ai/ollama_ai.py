import ollama

CRYPTO_SLANG_PROMPT = """
Analyze this {analysis_type} with a crypto-degen perspective. Use Twitter slang like:
- "Based" for good projects
- "NGMI" for bad moves
- "WAGMI" for positive outlook
- "Rug pull" for exit scams
- "Ape in" for buying opportunities
- "Ser" for sir

Include these metrics where relevant:
{metrics}

Flagged status: {flagged}
Risk score: {risk_score}

Keep responses under 3 lines. Be brutally honest but humorous.
"""

def generate_analysis(data, analysis_type="wallet", flagged_status=None):
    """Generate crypto-native analysis using LLM"""
    if analysis_type == "query":
        return handle_freeform_query(data)
    
    prompt = build_analysis_prompt(data, analysis_type, flagged_status)
    return query_llama(prompt)

def build_analysis_prompt(data, analysis_type, flagged_status):
    """Construct context-aware analysis prompt"""
    metrics = []
    
    if analysis_type == "wallet":
        metrics = [
            f"Tx Count: {data.get('tx_count', 0)}",
            f"Volume: {data.get('volume_eth', 0):.2f} ETH",
            f"Risk Score: {data.get('risk_score', 0)}/100"
        ]
    elif analysis_type == "contract":
        metrics = [
            f"Liquidity: ${data.get('liquidity', 0):,.0f}",
            f"24h Volume: ${data.get('volume_24h', 0):,.0f}",
            f"Holders: {data.get('holders', 0)}",
            f"Price Change: {data.get('price_change', 0):.2f}%"
        ]
    
    return CRYPTO_SLANG_PROMPT.format(
        analysis_type=analysis_type,
        metrics="\n".join(metrics),
        flagged=flagged_status or "Clean",
        risk_score=data.get("risk_score", "N/A")
    )

def query_llama(prompt):
    """Query local LLM with error handling"""
    try:
        response = ollama.chat(
            model="llama3.2:1b",
            messages=[{
                "role": "user",
                "content": prompt
            }],
            options={"temperature": 0.7}
        )
        return response['message']['content'].strip()
    
    except Exception as e:
        return f"🚨 LLM's rekt, ser: {str(e)}"

def handle_freeform_query(query):
    """Handle non-address questions"""
    prompt = f"Degen question: {query}\nAnswer like crypto Twitter expert using slang. Max 2 sentences. Don't use too much slang just a mix of simple and straightforward slang like ser, based, anon. Don't act like a 9 year old lmao"
    return query_llama(prompt)