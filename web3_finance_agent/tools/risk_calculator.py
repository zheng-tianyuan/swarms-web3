"""
Risk Calculator Tool

Tool for calculating various risk metrics and assessments for crypto investments.
"""

import numpy as np
from typing import Dict, Any, List, Optional
import time


class RiskCalculator:
    """Risk Calculator Class for investment risk assessment"""
    
    def __init__(self):
        """Initialize RiskCalculator"""
        self.risk_weights = {
            "market_risk": 0.3,
            "volatility_risk": 0.25,
            "liquidity_risk": 0.2,
            "concentration_risk": 0.15,
            "regulatory_risk": 0.1
        }
    
    def calculate_risk_score(self, asset: str, risk_tolerance: str = "moderate") -> float:
        """
        Calculate overall risk score for an asset
        
        Args:
            asset: Asset symbol
            risk_tolerance: Risk tolerance level (low/moderate/high)
            
        Returns:
            Risk score (0-1, where 1 is highest risk)
        """
        # Get individual risk components
        market_risk = self._calculate_market_risk(asset)
        volatility_risk = self._calculate_volatility_risk(asset)
        liquidity_risk = self._calculate_liquidity_risk(asset)
        concentration_risk = self._calculate_concentration_risk(asset)
        regulatory_risk = self._calculate_regulatory_risk(asset)
        
        # Calculate weighted risk score
        risk_score = (
            market_risk * self.risk_weights["market_risk"] +
            volatility_risk * self.risk_weights["volatility_risk"] +
            liquidity_risk * self.risk_weights["liquidity_risk"] +
            concentration_risk * self.risk_weights["concentration_risk"] +
            regulatory_risk * self.risk_weights["regulatory_risk"]
        )
        
        # Adjust based on risk tolerance
        risk_score = self._adjust_for_risk_tolerance(risk_score, risk_tolerance)
        
        return min(max(risk_score, 0), 1)  # Ensure between 0 and 1
    
    def assess_defi_risk(self, protocol_name: str) -> Dict[str, Any]:
        """
        Assess DeFi protocol risk
        
        Args:
            protocol_name: Protocol name
            
        Returns:
            Risk assessment dictionary
        """
        # This would typically integrate with DeFiAnalyzer
        # For now, return mock assessment
        return {
            "smart_contract_risk": self._get_random_risk_score(),
            "liquidity_risk": self._get_random_risk_score(),
            "concentration_risk": self._get_random_risk_score(),
            "regulatory_risk": self._get_random_risk_score(),
            "overall_risk_score": self._get_random_risk_score(),
            "risk_level": self._get_risk_level(self._get_random_risk_score()),
            "recommendations": self._get_risk_recommendations()
        }
    
    def assess_nft_value(self, project_name: str) -> Dict[str, Any]:
        """
        Assess NFT project value and risk
        
        Args:
            project_name: NFT project name
            
        Returns:
            NFT valuation dictionary
        """
        return {
            "intrinsic_value": self._get_random_risk_score(),
            "market_sentiment": self._get_random_risk_score(),
            "liquidity_score": self._get_random_risk_score(),
            "community_health": self._get_random_risk_score(),
            "overall_valuation": self._get_random_risk_score(),
            "risk_level": self._get_risk_level(self._get_random_risk_score()),
            "valuation_factors": self._get_nft_valuation_factors()
        }
    
    def get_asset_risk(self, asset: str) -> Dict[str, Any]:
        """
        Get comprehensive risk assessment for an asset
        
        Args:
            asset: Asset symbol
            
        Returns:
            Asset risk assessment dictionary
        """
        risk_score = self.calculate_risk_score(asset)
        
        return {
            "asset": asset,
            "risk_score": risk_score,
            "risk_level": self._get_risk_level(risk_score),
            "risk_components": {
                "market_risk": self._calculate_market_risk(asset),
                "volatility_risk": self._calculate_volatility_risk(asset),
                "liquidity_risk": self._calculate_liquidity_risk(asset),
                "concentration_risk": self._calculate_concentration_risk(asset),
                "regulatory_risk": self._calculate_regulatory_risk(asset)
            },
            "recommendations": self._get_asset_recommendations(asset, risk_score)
        }
    
    def calculate_diversification_score(self, assets: List[str]) -> float:
        """
        Calculate portfolio diversification score
        
        Args:
            assets: List of asset symbols
            
        Returns:
            Diversification score (0-1, where 1 is most diversified)
        """
        if len(assets) <= 1:
            return 0.0
        
        # Calculate correlation-based diversification
        # This is a simplified version - real implementation would use historical correlation data
        n_assets = len(assets)
        base_diversification = min(n_assets / 10, 1.0)  # Scale with number of assets
        
        # Add some randomness to simulate correlation effects
        correlation_factor = np.random.uniform(0.8, 1.0)
        
        diversification_score = base_diversification * correlation_factor
        
        return min(max(diversification_score, 0), 1)
    
    def calculate_var(self, asset: str, confidence_level: float = 0.95, time_horizon: int = 1) -> float:
        """
        Calculate Value at Risk (VaR) for an asset
        
        Args:
            asset: Asset symbol
            confidence_level: Confidence level (e.g., 0.95 for 95%)
            time_horizon: Time horizon in days
            
        Returns:
            VaR value as percentage
        """
        # This would typically use historical price data
        # For now, return mock VaR based on asset characteristics
        base_volatility = self._get_asset_volatility(asset)
        var_percentage = base_volatility * np.sqrt(time_horizon) * (1 - confidence_level)
        
        return min(max(var_percentage, 0), 1)  # Ensure between 0 and 1
    
    def _calculate_market_risk(self, asset: str) -> float:
        """Calculate market risk for an asset"""
        # Mock implementation - would use real market data
        asset_risks = {
            "BTC": 0.3,
            "ETH": 0.4,
            "SOL": 0.7,
            "ADA": 0.6,
            "DOT": 0.5,
            "LINK": 0.5,
            "UNI": 0.6,
            "AAVE": 0.7
        }
        return asset_risks.get(asset, 0.5)
    
    def _calculate_volatility_risk(self, asset: str) -> float:
        """Calculate volatility risk for an asset"""
        # Mock implementation - would use historical volatility data
        asset_volatilities = {
            "BTC": 0.4,
            "ETH": 0.5,
            "SOL": 0.8,
            "ADA": 0.7,
            "DOT": 0.6,
            "LINK": 0.6,
            "UNI": 0.7,
            "AAVE": 0.8
        }
        return asset_volatilities.get(asset, 0.6)
    
    def _calculate_liquidity_risk(self, asset: str) -> float:
        """Calculate liquidity risk for an asset"""
        # Mock implementation - would use trading volume data
        asset_liquidity = {
            "BTC": 0.2,
            "ETH": 0.3,
            "SOL": 0.6,
            "ADA": 0.5,
            "DOT": 0.4,
            "LINK": 0.4,
            "UNI": 0.5,
            "AAVE": 0.6
        }
        return asset_liquidity.get(asset, 0.5)
    
    def _calculate_concentration_risk(self, asset: str) -> float:
        """Calculate concentration risk for an asset"""
        # Mock implementation - would analyze market concentration
        return np.random.uniform(0.3, 0.7)
    
    def _calculate_regulatory_risk(self, asset: str) -> float:
        """Calculate regulatory risk for an asset"""
        # Mock implementation - would analyze regulatory environment
        return np.random.uniform(0.4, 0.8)
    
    def _adjust_for_risk_tolerance(self, risk_score: float, risk_tolerance: str) -> float:
        """Adjust risk score based on risk tolerance"""
        if risk_tolerance == "low":
            return risk_score * 1.2  # Increase perceived risk
        elif risk_tolerance == "high":
            return risk_score * 0.8  # Decrease perceived risk
        else:  # moderate
            return risk_score
    
    def _get_risk_level(self, risk_score: float) -> str:
        """Get risk level description"""
        if risk_score < 0.3:
            return "Low"
        elif risk_score < 0.6:
            return "Medium"
        else:
            return "High"
    
    def _get_random_risk_score(self) -> float:
        """Get random risk score for mock data"""
        return np.random.uniform(0.2, 0.8)
    
    def _get_asset_volatility(self, asset: str) -> float:
        """Get asset volatility for VaR calculation"""
        volatilities = {
            "BTC": 0.4,
            "ETH": 0.5,
            "SOL": 0.8,
            "ADA": 0.7,
            "DOT": 0.6,
            "LINK": 0.6,
            "UNI": 0.7,
            "AAVE": 0.8
        }
        return volatilities.get(asset, 0.6)
    
    def _get_risk_recommendations(self) -> List[str]:
        """Get risk management recommendations"""
        return [
            "Diversify across multiple protocols",
            "Monitor smart contract risks",
            "Set appropriate position sizes",
            "Regular portfolio rebalancing",
            "Stay informed about regulatory changes"
        ]
    
    def _get_nft_valuation_factors(self) -> Dict[str, float]:
        """Get NFT valuation factors"""
        return {
            "rarity_score": np.random.uniform(0.3, 0.9),
            "community_engagement": np.random.uniform(0.4, 0.8),
            "utility_value": np.random.uniform(0.2, 0.7),
            "brand_strength": np.random.uniform(0.3, 0.8),
            "market_trend": np.random.uniform(0.4, 0.9)
        }
    
    def _get_asset_recommendations(self, asset: str, risk_score: float) -> List[str]:
        """Get asset-specific recommendations"""
        recommendations = []
        
        if risk_score > 0.7:
            recommendations.extend([
                "Consider reducing position size",
                "Implement strict stop-loss orders",
                "Monitor closely for adverse developments"
            ])
        elif risk_score < 0.4:
            recommendations.extend([
                "Suitable for conservative portfolios",
                "Consider as core holding",
                "Lower monitoring requirements"
            ])
        else:
            recommendations.extend([
                "Moderate position sizing recommended",
                "Regular monitoring advised",
                "Balance with other assets"
            ])
        
        return recommendations 