# Blockchain Analysis Bot

This bot is designed to analyze blockchain wallet and token addresses, providing detailed insights such as transaction history, risk scores, wallet behaviors, and safety ratings. It supports multiple chains and generates human-readable, AI-driven analysis with crypto-native slang for a more engaging experience.

---

## Features
- Analyze wallet and token addresses across multiple chains.
- Fetch transaction history and risk assessment.
- Provide safety ratings and creator wallet behavior insights.
- Real-time analysis and human-like response style.
- Uses slang for crypto-native communication.

---

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/blockchain-analysis-bot.git
   cd blockchain-analysis-bot
   ```

2. **Install Dependencies:**
   Ensure you have Node.js installed, then run:
   ```bash
   npm install
   ```

3. **Install Python Dependencies:**
   Make sure Python 3 is installed, then install required libraries:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Environment Variables:**
   Create a `.env` file in the root directory and add the following:
   ```env
   ETHERSCAN_API_KEY=your_etherscan_api_key
   INFURA_PROJECT_ID=your_infura_project_id
   INFURA_PROJECT_SECRET=your_infura_secret
   ```

---

## Usage

1. **Start the Bot:**
   Run the following command to start the bot:
   ```bash
   npm run start
   ```

2. **Run Python Scripts (if applicable):**
   For additional analysis:
   ```bash
   python analyze_address.py
   ```

3. **Interact:**
   The bot can now process requests such as:
   - "Analyze (address)"
   - "Is this safe? (address)"
   - "What's the transaction history of this wallet?"

---

## Dependencies

### Node.js Libraries:
- `express`
- `axios`
- `ethers`
- `dotenv`

### Python Libraries:
- `requests`
- `web3`

---

## Contributing
Feel free to submit issues or pull requests to enhance the bot.

---

## License
This project is licensed under the MIT License.
