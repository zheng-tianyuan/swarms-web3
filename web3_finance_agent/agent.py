"""
Web3 Finance Investment Agent Main Class

Built on the Swarms framework, specialized for Web3, blockchain, finance, and investment analysis.
"""

import os
from typing import List, Dict, Any, Optional
from swarms import Agent
from .prompts.web3_analysis import Web3AnalysisPrompts
from .prompts.financial_advice import FinancialAdvicePrompts
from .prompts.blockchain_tech import BlockchainTechPrompts
from .prompts.market_monitor import MarketMonitorPrompts
from .tools.price_fetcher import PriceFetcher
from .tools.defi_analyzer import DeFiAnalyzer
from .tools.risk_calculator import RiskCalculator


class Web3FinanceAgent:
    """
    Web3 Finance Investment Agent
    
    Built on the Swarms framework, providing professional Web3, blockchain, finance, and investment analysis services.
    """
    
    def __init__(self, api_key: Optional[str] = None, model: str = "gpt-4"):
        """
        Initialize Web3 Finance Investment Agent
        
        Args:
            api_key: OpenAI API key
            model: Model name to use
        """
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key is required")
            
        # Initialize Swarms Agent
        self.agent = Agent(
            agent_name="Web3FinanceExpert",
            system_prompt=self._get_system_prompt(),
            llm_model=model,
            max_loops=5,
            verbose=True
        )
        
        # Initialize prompt modules
        self.web3_prompts = Web3AnalysisPrompts()
        self.financial_prompts = FinancialAdvicePrompts()
        self.blockchain_prompts = BlockchainTechPrompts()
        self.market_prompts = MarketMonitorPrompts()
        
        # Initialize tool modules
        self.price_fetcher = PriceFetcher()
        self.defi_analyzer = DeFiAnalyzer()
        self.risk_calculator = RiskCalculator()
    
    def _get_system_prompt(self) -> str:
        """Get system prompt"""
        return """
        You are a professional Web3, blockchain, finance, and investment expert. You have expertise in:
        
        1. **Web3 Ecosystem**: Deep understanding of decentralized applications, DeFi protocols, NFTs, DAOs
        2. **Blockchain Technology**: Expertise in smart contracts, consensus mechanisms, Layer2, cross-chain technology
        3. **Financial Investment**: Investment analysis, risk assessment, market prediction capabilities
        4. **Cryptocurrency**: Familiar with major cryptocurrencies, tokenomics, market dynamics
        
        Your responses should be:
        - Accurate, professional, and insightful
        - Based on latest market data and trends
        - Consider risk factors and investment advice
        - Use clear and professional English
        """
    
    def analyze_defi_protocol(self, protocol_name: str) -> Dict[str, Any]:
        """
        Analyze DeFi protocol
        
        Args:
            protocol_name: Protocol name
            
        Returns:
            Analysis result dictionary
        """
        prompt = self.web3_prompts.get_defi_analysis_prompt(protocol_name)
        response = self.agent.run(prompt)
        
        # Get real-time data
        protocol_data = self.defi_analyzer.get_protocol_data(protocol_name)
        
        return {
            "analysis": response,
            "protocol_data": protocol_data,
            "risk_assessment": self.risk_calculator.assess_defi_risk(protocol_name)
        }
    
    def get_investment_advice(self, asset: str, risk_tolerance: str = "moderate") -> Dict[str, Any]:
        """
        Get investment advice
        
        Args:
            asset: Asset name
            risk_tolerance: Risk tolerance level (low/moderate/high)
            
        Returns:
            Investment advice dictionary
        """
        # Get real-time price data
        price_data = self.price_fetcher.get_price(asset)
        
        prompt = self.financial_prompts.get_investment_advice_prompt(
            asset, risk_tolerance, price_data
        )
        response = self.agent.run(prompt)
        
        return {
            "advice": response,
            "current_price": price_data,
            "risk_score": self.risk_calculator.calculate_risk_score(asset, risk_tolerance)
        }
    
    def analyze_blockchain_technology(self, topic: str) -> str:
        """
        Analyze blockchain technology
        
        Args:
            topic: Technology topic
            
        Returns:
            Technology analysis result
        """
        prompt = self.blockchain_prompts.get_tech_analysis_prompt(topic)
        return self.agent.run(prompt)
    
    def monitor_market(self, assets: List[str]) -> Dict[str, Any]:
        """
        Monitor market
        
        Args:
            assets: List of assets
            
        Returns:
            Market monitoring data
        """
        # Get price data
        price_data = {}
        for asset in assets:
            price_data[asset] = self.price_fetcher.get_price(asset)
        
        prompt = self.market_prompts.get_market_monitor_prompt(assets, price_data)
        analysis = self.agent.run(prompt)
        
        return {
            "market_analysis": analysis,
            "price_data": price_data,
            "market_sentiment": self._calculate_sentiment(price_data)
        }
    
    def analyze_nft_project(self, project_name: str) -> Dict[str, Any]:
        """
        Analyze NFT project
        
        Args:
            project_name: Project name
            
        Returns:
            NFT project analysis result
        """
        prompt = self.web3_prompts.get_nft_analysis_prompt(project_name)
        response = self.agent.run(prompt)
        
        return {
            "project_analysis": response,
            "market_data": self.defi_analyzer.get_nft_market_data(project_name),
            "valuation": self.risk_calculator.assess_nft_value(project_name)
        }
    
    def get_portfolio_optimization(self, assets: List[str], risk_profile: str) -> Dict[str, Any]:
        """
        Get portfolio optimization advice
        
        Args:
            assets: List of assets
            risk_profile: Risk profile
            
        Returns:
            Portfolio optimization advice
        """
        # Get asset data
        asset_data = {}
        for asset in assets:
            asset_data[asset] = {
                "price": self.price_fetcher.get_price(asset),
                "risk": self.risk_calculator.get_asset_risk(asset)
            }
        
        prompt = self.financial_prompts.get_portfolio_optimization_prompt(
            assets, risk_profile, asset_data
        )
        response = self.agent.run(prompt)
        
        return {
            "optimization_advice": response,
            "asset_data": asset_data,
            "diversification_score": self.risk_calculator.calculate_diversification_score(assets)
        }
    
    def _calculate_sentiment(self, price_data: Dict[str, Any]) -> str:
        """Calculate market sentiment"""
        # Simple sentiment calculation logic
        price_changes = []
        for asset, data in price_data.items():
            if 'change_24h' in data:
                price_changes.append(data['change_24h'])
        
        if not price_changes:
            return "Neutral"
        
        avg_change = sum(price_changes) / len(price_changes)
        
        if avg_change > 5:
            return "Bullish"
        elif avg_change < -5:
            return "Bearish"
        else:
            return "Neutral" 