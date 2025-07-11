"""
Advanced Analysis Example

Demonstrates advanced usage of the Web3FinanceAgent for comprehensive analysis.
"""

import os
import json
from datetime import datetime
from dotenv import load_dotenv
from web3_finance_agent import Web3FinanceAgent

# Load environment variables
load_dotenv()

def comprehensive_defi_analysis():
    """Perform comprehensive DeFi analysis"""
    print("=== Comprehensive DeFi Analysis ===")
    
    agent = Web3FinanceAgent()
    
    # List of major DeFi protocols to analyze
    protocols = [
        "Uniswap V3",
        "Aave",
        "Compound",
        "Curve Finance",
        "SushiSwap"
    ]
    
    results = {}
    
    for protocol in protocols:
        print(f"\nAnalyzing {protocol}...")
        try:
            analysis = agent.analyze_defi_protocol(protocol)
            results[protocol] = {
                "analysis": analysis["analysis"][:500],
                "tvl": analysis["protocol_data"].get("tvl", 0),
                "risk_score": analysis["risk_assessment"].get("overall_risk_score", 0),
                "risk_level": analysis["risk_assessment"].get("risk_level", "Unknown")
            }
            print(f"✓ {protocol} - TVL: ${results[protocol]['tvl']:,.0f}, Risk: {results[protocol]['risk_level']}")
        except Exception as e:
            print(f"✗ Error analyzing {protocol}: {e}")
    
    return results

def portfolio_risk_analysis():
    """Perform comprehensive portfolio risk analysis"""
    print("\n=== Portfolio Risk Analysis ===")
    
    agent = Web3FinanceAgent()
    
    # Different portfolio configurations
    portfolios = {
        "Conservative": ["BTC", "ETH"],
        "Balanced": ["BTC", "ETH", "SOL", "ADA"],
        "Aggressive": ["SOL", "ADA", "DOT", "LINK", "UNI", "AAVE"]
    }
    
    results = {}
    
    for portfolio_name, assets in portfolios.items():
        print(f"\nAnalyzing {portfolio_name} Portfolio...")
        try:
            # Get individual asset risks
            asset_risks = {}
            total_risk_score = 0
            
            for asset in assets:
                risk_data = agent.risk_calculator.get_asset_risk(asset)
                asset_risks[asset] = risk_data
                total_risk_score += risk_data["risk_score"]
            
            # Get portfolio optimization
            portfolio_advice = agent.get_portfolio_optimization(assets, "moderate")
            
            results[portfolio_name] = {
                "assets": assets,
                "asset_risks": asset_risks,
                "average_risk_score": total_risk_score / len(assets),
                "diversification_score": portfolio_advice["diversification_score"],
                "optimization_advice": portfolio_advice["optimization_advice"][:300]
            }
            
            print(f"✓ {portfolio_name} - Avg Risk: {results[portfolio_name]['average_risk_score']:.2f}, Diversification: {results[portfolio_name]['diversification_score']:.2f}")
            
        except Exception as e:
            print(f"✗ Error analyzing {portfolio_name} portfolio: {e}")
    
    return results

def market_sentiment_analysis():
    """Perform market sentiment analysis"""
    print("\n=== Market Sentiment Analysis ===")
    
    agent = Web3FinanceAgent()
    
    # Different asset categories
    asset_categories = {
        "Layer1": ["BTC", "ETH", "SOL", "ADA"],
        "DeFi": ["UNI", "AAVE", "COMP", "CRV"],
        "Layer2": ["MATIC", "ARB", "OP", "IMX"]
    }
    
    results = {}
    
    for category, assets in asset_categories.items():
        print(f"\nAnalyzing {category} sentiment...")
        try:
            market_data = agent.monitor_market(assets)
            
            results[category] = {
                "assets": assets,
                "sentiment": market_data["market_sentiment"],
                "price_data": market_data["price_data"],
                "analysis": market_data["market_analysis"][:300]
            }
            
            print(f"✓ {category} - Sentiment: {market_data['market_sentiment']}")
            
        except Exception as e:
            print(f"✗ Error analyzing {category} sentiment: {e}")
    
    return results

def nft_market_analysis():
    """Perform NFT market analysis"""
    print("\n=== NFT Market Analysis ===")
    
    agent = Web3FinanceAgent()
    
    # Popular NFT projects
    nft_projects = [
        "Bored Ape Yacht Club",
        "CryptoPunks",
        "Doodles",
        "Azuki",
        "Moonbirds"
    ]
    
    results = {}
    
    for project in nft_projects:
        print(f"\nAnalyzing {project}...")
        try:
            analysis = agent.analyze_nft_project(project)
            
            results[project] = {
                "analysis": analysis["project_analysis"][:400],
                "market_data": analysis["market_data"],
                "valuation": analysis["valuation"]
            }
            
            print(f"✓ {project} - Floor Price: ${analysis['market_data'].get('floor_price', 0):.2f}")
            
        except Exception as e:
            print(f"✗ Error analyzing {project}: {e}")
    
    return results

def blockchain_technology_comparison():
    """Compare different blockchain technologies"""
    print("\n=== Blockchain Technology Comparison ===")
    
    agent = Web3FinanceAgent()
    
    # Different blockchain technologies
    technologies = [
        "Proof of Stake Consensus",
        "Layer2 Scaling Solutions",
        "Cross-chain Bridges",
        "Zero Knowledge Proofs",
        "Decentralized Identity"
    ]
    
    results = {}
    
    for tech in technologies:
        print(f"\nAnalyzing {tech}...")
        try:
            analysis = agent.analyze_blockchain_technology(tech)
            
            results[tech] = {
                "analysis": analysis[:500],
                "timestamp": datetime.now().isoformat()
            }
            
            print(f"✓ {tech} - Analysis completed")
            
        except Exception as e:
            print(f"✗ Error analyzing {tech}: {e}")
    
    return results

def generate_report(all_results):
    """Generate comprehensive analysis report"""
    print("\n" + "="*60)
    print("COMPREHENSIVE WEB3 FINANCE ANALYSIS REPORT")
    print("="*60)
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*60)
    
    # DeFi Analysis Summary
    if "defi_analysis" in all_results:
        print("\n📊 DeFi Protocol Analysis Summary:")
        defi_results = all_results["defi_analysis"]
        for protocol, data in defi_results.items():
            print(f"  • {protocol}: TVL ${data['tvl']:,.0f}, Risk: {data['risk_level']}")
    
    # Portfolio Analysis Summary
    if "portfolio_analysis" in all_results:
        print("\n💼 Portfolio Risk Analysis Summary:")
        portfolio_results = all_results["portfolio_analysis"]
        for portfolio, data in portfolio_results.items():
            print(f"  • {portfolio}: Avg Risk {data['average_risk_score']:.2f}, Diversification {data['diversification_score']:.2f}")
    
    # Market Sentiment Summary
    if "market_sentiment" in all_results:
        print("\n📈 Market Sentiment Summary:")
        sentiment_results = all_results["market_sentiment"]
        for category, data in sentiment_results.items():
            print(f"  • {category}: {data['sentiment']}")
    
    # NFT Analysis Summary
    if "nft_analysis" in all_results:
        print("\n🎨 NFT Market Analysis Summary:")
        nft_results = all_results["nft_analysis"]
        for project, data in nft_results.items():
            floor_price = data['market_data'].get('floor_price', 0)
            print(f"  • {project}: Floor Price ${floor_price:.2f}")
    
    print("\n" + "="*60)
    print("Report completed successfully!")
    print("="*60)

def main():
    """Main function for advanced analysis"""
    
    print("🚀 Starting Advanced Web3 Finance Analysis...")
    print("This may take several minutes to complete all analyses.\n")
    
    all_results = {}
    
    try:
        # Run all analyses
        all_results["defi_analysis"] = comprehensive_defi_analysis()
        all_results["portfolio_analysis"] = portfolio_risk_analysis()
        all_results["market_sentiment"] = market_sentiment_analysis()
        all_results["nft_analysis"] = nft_market_analysis()
        all_results["blockchain_tech"] = blockchain_technology_comparison()
        
        # Generate comprehensive report
        generate_report(all_results)
        
        # Save results to file
        with open("advanced_analysis_results.json", "w") as f:
            json.dump(all_results, f, indent=2, default=str)
        print("\n💾 Results saved to 'advanced_analysis_results.json'")
        
    except Exception as e:
        print(f"\n❌ Error during analysis: {e}")
        print("Please check your API key and internet connection.")

if __name__ == "__main__":
    main() 