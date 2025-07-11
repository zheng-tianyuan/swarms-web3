"""
Simple Test Script

Quick test to verify the Web3FinanceAgent is working correctly.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_agent_initialization():
    """Test agent initialization"""
    try:
        from web3_finance_agent import Web3FinanceAgent
        
        # Check if API key is available
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            print("⚠️  Warning: No OpenAI API key found. Using mock data for testing.")
            print("   Please set OPENAI_API_KEY in your .env file for full functionality.")
        
        # Initialize agent
        agent = Web3FinanceAgent()
        print("✅ Agent initialized successfully!")
        
        return agent
        
    except Exception as e:
        print(f"❌ Error initializing agent: {e}")
        return None

def test_basic_functionality(agent):
    """Test basic functionality"""
    if not agent:
        return
    
    print("\n🧪 Testing basic functionality...")
    
    try:
        # Test price fetching
        print("Testing price fetching...")
        price_data = agent.price_fetcher.get_price("BTC")
        print(f"✅ BTC Price: ${price_data.get('price', 'N/A'):,.2f}")
        
        # Test risk calculation
        print("Testing risk calculation...")
        risk_data = agent.risk_calculator.get_asset_risk("ETH")
        print(f"✅ ETH Risk Score: {risk_data['risk_score']:.2f} ({risk_data['risk_level']})")
        
        # Test DeFi analysis (mock)
        print("Testing DeFi analysis...")
        defi_data = agent.defi_analyzer.get_protocol_data("Uniswap V3")
        print(f"✅ Uniswap V3 TVL: ${defi_data.get('tvl', 0):,.0f}")
        
        print("\n✅ All basic functionality tests passed!")
        
    except Exception as e:
        print(f"❌ Error in basic functionality test: {e}")

def test_prompt_generation():
    """Test prompt generation"""
    print("\n📝 Testing prompt generation...")
    
    try:
        from web3_finance_agent.prompts.web3_analysis import Web3AnalysisPrompts
        from web3_finance_agent.prompts.financial_advice import FinancialAdvicePrompts
        
        web3_prompts = Web3AnalysisPrompts()
        financial_prompts = FinancialAdvicePrompts()
        
        # Test DeFi prompt
        defi_prompt = web3_prompts.get_defi_analysis_prompt("Uniswap V3")
        print(f"✅ DeFi prompt generated ({len(defi_prompt)} characters)")
        
        # Test investment advice prompt
        investment_prompt = financial_prompts.get_investment_advice_prompt("ETH", "moderate", {"price": 3000})
        print(f"✅ Investment advice prompt generated ({len(investment_prompt)} characters)")
        
        print("✅ All prompt generation tests passed!")
        
    except Exception as e:
        print(f"❌ Error in prompt generation test: {e}")

def main():
    """Main test function"""
    print("🚀 Starting Web3FinanceAgent Tests...")
    print("=" * 50)
    
    # Test agent initialization
    agent = test_agent_initialization()
    
    # Test basic functionality
    test_basic_functionality(agent)
    
    # Test prompt generation
    test_prompt_generation()
    
    print("\n" + "=" * 50)
    print("🎉 All tests completed!")
    print("\nTo run the full examples:")
    print("  python examples/basic_usage.py")
    print("  python examples/advanced_analysis.py")
    print("\nMake sure to set your OPENAI_API_KEY in the .env file for full functionality.")

if __name__ == "__main__":
    main() 