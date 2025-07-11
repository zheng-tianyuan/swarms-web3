# Web3 Finance Investment Agent Package

A professional Web3, blockchain, finance, and investment agent package built on the Swarms framework.

## Features

- **Web3 Analysis**: Intelligent analysis of blockchain projects, DeFi protocols, NFT markets
- **Financial Investment**: Investment advice, risk assessment, market analysis
- **Blockchain Technology**: Deep understanding of smart contracts, consensus mechanisms, Layer2 solutions
- **Market Monitoring**: Real-time tracking of cryptocurrency prices, trading volume, market sentiment

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```python
from web3_finance_agent import Web3FinanceAgent

# Create agent instance
agent = Web3FinanceAgent()

# Analyze DeFi protocol
response = agent.analyze_defi_protocol("Uniswap V3")

# Get investment advice
advice = agent.get_investment_advice("ETH", risk_tolerance="moderate")

# Monitor market
market_data = agent.monitor_market(["BTC", "ETH", "SOL"])
```

## Project Structure

```
web3_finance_agent/
├── __init__.py
├── agent.py              # Main agent class
├── prompts/              # Prompt templates
│   ├── web3_analysis.py
│   ├── financial_advice.py
│   ├── blockchain_tech.py
│   └── market_monitor.py
├── tools/                # Tool functions
│   ├── price_fetcher.py
│   ├── defi_analyzer.py
│   └── risk_calculator.py
└── examples/             # Usage examples
    ├── basic_usage.py
    └── advanced_analysis.py
``` 