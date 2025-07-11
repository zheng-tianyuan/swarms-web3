"""
DeFi Analyzer Tool

Tool for analyzing DeFi protocols, TVL data, and DeFi metrics.
"""

import requests
import time
from typing import Dict, Any, Optional, List
import json


class DeFiAnalyzer:
    """DeFi Analyzer Class for protocol analysis"""
    
    def __init__(self):
        """Initialize DeFiAnalyzer"""
        self.cache = {}
        self.cache_timeout = 300  # 5 minutes cache
        self.base_urls = {
            "defillama": "https://api.llama.fi",
            "coingecko": "https://api.coingecko.com/api/v3"
        }
    
    def get_protocol_data(self, protocol_name: str) -> Dict[str, Any]:
        """
        Get protocol data from DeFi Llama
        
        Args:
            protocol_name: Protocol name
            
        Returns:
            Protocol data dictionary
        """
        cache_key = f"protocol_{protocol_name}"
        if cache_key in self.cache:
            cached_data, timestamp = self.cache[cache_key]
            if time.time() - timestamp < self.cache_timeout:
                return cached_data
        
        try:
            # Try to get from DeFi Llama API
            url = f"{self.base_urls['defillama']}/protocol/{protocol_name.lower().replace(' ', '-')}"
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                protocol_data = {
                    "name": data.get("name", protocol_name),
                    "tvl": data.get("tvl", 0),
                    "chains": data.get("chains", []),
                    "category": data.get("category", "Unknown"),
                    "audits": data.get("audits", 0),
                    "audit_links": data.get("audit_links", []),
                    "url": data.get("url", ""),
                    "description": data.get("description", ""),
                    "timestamp": int(time.time())
                }
            else:
                # Fallback to mock data
                protocol_data = self._get_mock_protocol_data(protocol_name)
            
            # Cache the result
            self.cache[cache_key] = (protocol_data, time.time())
            
            return protocol_data
            
        except Exception as e:
            return self._get_mock_protocol_data(protocol_name)
    
    def get_tvl_data(self, protocol_name: str) -> Dict[str, Any]:
        """
        Get TVL (Total Value Locked) data for a protocol
        
        Args:
            protocol_name: Protocol name
            
        Returns:
            TVL data dictionary
        """
        try:
            # Get historical TVL data
            url = f"{self.base_urls['defillama']}/protocol/{protocol_name.lower().replace(' ', '-')}/historical"
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                return {
                    "current_tvl": data.get("tvl", [{}])[-1].get("totalLiquidityUSD", 0),
                    "historical_tvl": data.get("tvl", []),
                    "timestamp": int(time.time())
                }
            else:
                return self._get_mock_tvl_data(protocol_name)
                
        except Exception:
            return self._get_mock_tvl_data(protocol_name)
    
    def get_defi_market_data(self) -> Dict[str, Any]:
        """
        Get overall DeFi market data
        
        Returns:
            DeFi market data dictionary
        """
        try:
            url = f"{self.base_urls['defillama']}/overview/fees"
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                return {
                    "total_tvl": data.get("total", 0),
                    "protocols": data.get("protocols", []),
                    "timestamp": int(time.time())
                }
            else:
                return self._get_mock_defi_market_data()
                
        except Exception:
            return self._get_mock_defi_market_data()
    
    def get_nft_market_data(self, project_name: str) -> Dict[str, Any]:
        """
        Get NFT market data for a project
        
        Args:
            project_name: NFT project name
            
        Returns:
            NFT market data dictionary
        """
        try:
            # This would typically use OpenSea or similar API
            # For now, return mock data
            return self._get_mock_nft_market_data(project_name)
        except Exception:
            return self._get_mock_nft_market_data(project_name)
    
    def analyze_protocol_risk(self, protocol_name: str) -> Dict[str, Any]:
        """
        Analyze protocol risk factors
        
        Args:
            protocol_name: Protocol name
            
        Returns:
            Risk analysis dictionary
        """
        protocol_data = self.get_protocol_data(protocol_name)
        
        risk_factors = {
            "smart_contract_risk": self._assess_smart_contract_risk(protocol_data),
            "liquidity_risk": self._assess_liquidity_risk(protocol_data),
            "concentration_risk": self._assess_concentration_risk(protocol_data),
            "regulatory_risk": self._assess_regulatory_risk(protocol_data),
            "overall_risk_score": 0
        }
        
        # Calculate overall risk score
        risk_factors["overall_risk_score"] = sum([
            risk_factors["smart_contract_risk"],
            risk_factors["liquidity_risk"],
            risk_factors["concentration_risk"],
            risk_factors["regulatory_risk"]
        ]) / 4
        
        return risk_factors
    
    def _assess_smart_contract_risk(self, protocol_data: Dict[str, Any]) -> float:
        """Assess smart contract risk"""
        audits = protocol_data.get("audits", 0)
        audit_links = protocol_data.get("audit_links", [])
        
        if audits >= 3 and len(audit_links) >= 2:
            return 0.2  # Low risk
        elif audits >= 1:
            return 0.5  # Medium risk
        else:
            return 0.8  # High risk
    
    def _assess_liquidity_risk(self, protocol_data: Dict[str, Any]) -> float:
        """Assess liquidity risk"""
        tvl = protocol_data.get("tvl", 0)
        
        if tvl > 1000000000:  # > $1B
            return 0.2  # Low risk
        elif tvl > 100000000:  # > $100M
            return 0.5  # Medium risk
        else:
            return 0.8  # High risk
    
    def _assess_concentration_risk(self, protocol_data: Dict[str, Any]) -> float:
        """Assess concentration risk"""
        chains = protocol_data.get("chains", [])
        
        if len(chains) >= 5:
            return 0.2  # Low risk
        elif len(chains) >= 2:
            return 0.5  # Medium risk
        else:
            return 0.8  # High risk
    
    def _assess_regulatory_risk(self, protocol_data: Dict[str, Any]) -> float:
        """Assess regulatory risk"""
        # This would typically involve more complex analysis
        # For now, return a moderate risk score
        return 0.6
    
    def _get_mock_protocol_data(self, protocol_name: str) -> Dict[str, Any]:
        """Get mock protocol data for testing"""
        import random
        
        mock_protocols = {
            "Uniswap V3": {
                "name": "Uniswap V3",
                "tvl": 3500000000,
                "chains": ["Ethereum", "Polygon", "Arbitrum", "Optimism"],
                "category": "DEX",
                "audits": 3,
                "audit_links": ["https://audit1.com", "https://audit2.com"],
                "url": "https://uniswap.org",
                "description": "Decentralized exchange protocol"
            },
            "Aave": {
                "name": "Aave",
                "tvl": 12000000000,
                "chains": ["Ethereum", "Polygon", "Avalanche"],
                "category": "Lending",
                "audits": 4,
                "audit_links": ["https://audit1.com", "https://audit2.com", "https://audit3.com"],
                "url": "https://aave.com",
                "description": "Decentralized lending protocol"
            },
            "Compound": {
                "name": "Compound",
                "tvl": 8000000000,
                "chains": ["Ethereum"],
                "category": "Lending",
                "audits": 3,
                "audit_links": ["https://audit1.com", "https://audit2.com"],
                "url": "https://compound.finance",
                "description": "Algorithmic interest rate protocol"
            }
        }
        
        return mock_protocols.get(protocol_name, {
            "name": protocol_name,
            "tvl": random.uniform(1000000, 1000000000),
            "chains": ["Ethereum"],
            "category": "Unknown",
            "audits": random.randint(0, 2),
            "audit_links": [],
            "url": "",
            "description": "Unknown protocol"
        })
    
    def _get_mock_tvl_data(self, protocol_name: str) -> Dict[str, Any]:
        """Get mock TVL data for testing"""
        import random
        
        return {
            "current_tvl": random.uniform(1000000, 10000000000),
            "historical_tvl": [
                {"date": int(time.time()) - i * 86400, "totalLiquidityUSD": random.uniform(1000000, 10000000000)}
                for i in range(30)
            ],
            "timestamp": int(time.time())
        }
    
    def _get_mock_defi_market_data(self) -> Dict[str, Any]:
        """Get mock DeFi market data for testing"""
        return {
            "total_tvl": 45000000000,
            "protocols": [
                {"name": "Uniswap V3", "tvl": 3500000000},
                {"name": "Aave", "tvl": 12000000000},
                {"name": "Compound", "tvl": 8000000000}
            ],
            "timestamp": int(time.time())
        }
    
    def _get_mock_nft_market_data(self, project_name: str) -> Dict[str, Any]:
        """Get mock NFT market data for testing"""
        import random
        
        return {
            "project_name": project_name,
            "floor_price": random.uniform(1, 100),
            "total_volume": random.uniform(1000000, 100000000),
            "total_supply": random.randint(1000, 10000),
            "holders": random.randint(500, 5000),
            "timestamp": int(time.time())
        } 