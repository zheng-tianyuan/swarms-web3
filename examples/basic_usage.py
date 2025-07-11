"""
Basic Usage Example

Demonstrates basic usage of the Web3FinanceAgent.
"""

import os
from dotenv import load_dotenv
from web3_finance_agent import Web3FinanceAgent

# Load environment variables
load_dotenv()

def main():
    """Main function demonstrating basic usage"""
    
    # Initialize the agent
    agent = Web3FinanceAgent()
    
    print("=== Web3 Finance Investment Agent Demo ===\n")
    
    # Example 1: Analyze DeFi Protocol
    print("1. Analyzing DeFi Protocol (Uniswap V3)")
    print("-" * 50)
    defi_analysis = agent.analyze_defi_protocol("Uniswap V3")
    print(f"Analysis: {defi_analysis['analysis'][:200]}...")
    print(f"Protocol Data: {defi_analysis['protocol_data']}")
    print(f"Risk Assessment: {defi_analysis['risk_assessment']}")
    print()
    
    # Example 2: Get Investment Advice
    print("2. Getting Investment Advice for ETH")
    print("-" * 50)
    investment_advice = agent.get_investment_advice("ETH", risk_tolerance="moderate")
    print(f"Advice: {investment_advice['advice'][:200]}...")
    print(f"Current Price: {investment_advice['current_price']}")
    print(f"Risk Score: {investment_advice['risk_score']}")
    print()
    
    # Example 3: Monitor Market
    print("3. Monitoring Market for BTC, ETH, SOL")
    print("-" * 50)
    market_data = agent.monitor_market(["BTC", "ETH", "SOL"])
    print(f"Market Analysis: {market_data['market_analysis'][:200]}...")
    print(f"Price Data: {market_data['price_data']}")
    print(f"Market Sentiment: {market_data['market_sentiment']}")
    print()
    
    # Example 4: Analyze NFT Project
    print("4. Analyzing NFT Project (Bored Ape Yacht Club)")
    print("-" * 50)
    nft_analysis = agent.analyze_nft_project("Bored Ape Yacht Club")
    print(f"Project Analysis: {nft_analysis['project_analysis'][:200]}...")
    print(f"Market Data: {nft_analysis['market_data']}")
    print(f"Valuation: {nft_analysis['valuation']}")
    print()
    
    # Example 5: Portfolio Optimization
    print("5. Portfolio Optimization")
    print("-" * 50)
    portfolio_advice = agent.get_portfolio_optimization(
        assets=["BTC", "ETH", "SOL", "ADA"],
        risk_profile="moderate"
    )
    print(f"Optimization Advice: {portfolio_advice['optimization_advice'][:200]}...")
    print(f"Asset Data: {portfolio_advice['asset_data']}")
    print(f"Diversification Score: {portfolio_advice['diversification_score']}")
    print()
    
    # Example 6: Blockchain Technology Analysis
    print("6. Blockchain Technology Analysis (Layer2 Solutions)")
    print("-" * 50)
    tech_analysis = agent.analyze_blockchain_technology("Layer2 Scaling Solutions")
    print(f"Technology Analysis: {tech_analysis[:300]}...")
    print()

if __name__ == "__main__":
    main() 