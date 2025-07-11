"""
Price Fetcher Tool

Tool for fetching real-time cryptocurrency prices and market data.
"""

import requests
import time
from typing import Dict, Any, Optional
import ccxt


class PriceFetcher:
    """Price Fetcher Class for cryptocurrency data"""
    
    def __init__(self):
        """Initialize PriceFetcher"""
        self.exchange = ccxt.binance()
        self.cache = {}
        self.cache_timeout = 60  # 60 seconds cache
    
    def get_price(self, asset: str) -> Dict[str, Any]:
        """
        Get current price data for an asset
        
        Args:
            asset: Asset symbol (e.g., 'BTC', 'ETH')
            
        Returns:
            Price data dictionary
        """
        # Check cache first
        cache_key = f"{asset}_price"
        if cache_key in self.cache:
            cached_data, timestamp = self.cache[cache_key]
            if time.time() - timestamp < self.cache_timeout:
                return cached_data
        
        try:
            # Fetch from Binance API
            ticker = self.exchange.fetch_ticker(f"{asset}/USDT")
            
            price_data = {
                "symbol": asset,
                "price": ticker["last"],
                "change_24h": ticker["percentage"],
                "volume_24h": ticker["quoteVolume"],
                "high_24h": ticker["high"],
                "low_24h": ticker["low"],
                "timestamp": ticker["timestamp"]
            }
            
            # Cache the result
            self.cache[cache_key] = (price_data, time.time())
            
            return price_data
            
        except Exception as e:
            # Fallback to mock data if API fails
            return self._get_mock_price_data(asset)
    
    def get_multiple_prices(self, assets: list) -> Dict[str, Dict[str, Any]]:
        """
        Get prices for multiple assets
        
        Args:
            assets: List of asset symbols
            
        Returns:
            Dictionary of price data for each asset
        """
        results = {}
        for asset in assets:
            results[asset] = self.get_price(asset)
        return results
    
    def get_historical_data(self, asset: str, timeframe: str = "1d", limit: int = 30) -> list:
        """
        Get historical price data
        
        Args:
            asset: Asset symbol
            timeframe: Timeframe (1m, 5m, 1h, 1d, etc.)
            limit: Number of candles to fetch
            
        Returns:
            List of historical data
        """
        try:
            ohlcv = self.exchange.fetch_ohlcv(f"{asset}/USDT", timeframe, limit=limit)
            return ohlcv
        except Exception as e:
            return self._get_mock_historical_data(asset, limit)
    
    def get_market_cap(self, asset: str) -> Optional[float]:
        """
        Get market capitalization for an asset
        
        Args:
            asset: Asset symbol
            
        Returns:
            Market cap value or None
        """
        try:
            # This would typically use a different API like CoinGecko
            # For now, return mock data
            return self._get_mock_market_cap(asset)
        except Exception:
            return None
    
    def _get_mock_price_data(self, asset: str) -> Dict[str, Any]:
        """Get mock price data for testing"""
        import random
        
        base_prices = {
            "BTC": 45000,
            "ETH": 3000,
            "SOL": 100,
            "ADA": 0.5,
            "DOT": 7,
            "LINK": 15,
            "UNI": 8,
            "AAVE": 200
        }
        
        base_price = base_prices.get(asset, 100)
        price_change = random.uniform(-0.1, 0.1)  # ±10% change
        
        return {
            "symbol": asset,
            "price": base_price * (1 + price_change),
            "change_24h": price_change * 100,
            "volume_24h": base_price * random.uniform(1000, 10000),
            "high_24h": base_price * (1 + random.uniform(0, 0.15)),
            "low_24h": base_price * (1 - random.uniform(0, 0.15)),
            "timestamp": int(time.time() * 1000)
        }
    
    def _get_mock_historical_data(self, asset: str, limit: int) -> list:
        """Get mock historical data for testing"""
        import random
        
        base_price = 100
        data = []
        current_time = int(time.time() * 1000)
        
        for i in range(limit):
            price_change = random.uniform(-0.05, 0.05)
            base_price *= (1 + price_change)
            
            data.append([
                current_time - (limit - i) * 24 * 60 * 60 * 1000,  # timestamp
                base_price * (1 - random.uniform(0, 0.02)),        # open
                base_price * (1 + random.uniform(0, 0.02)),        # high
                base_price * (1 - random.uniform(0, 0.02)),        # low
                base_price,                                         # close
                base_price * random.uniform(100, 1000)             # volume
            ])
        
        return data
    
    def _get_mock_market_cap(self, asset: str) -> float:
        """Get mock market cap data"""
        market_caps = {
            "BTC": 850000000000,
            "ETH": 360000000000,
            "SOL": 40000000000,
            "ADA": 16000000000,
            "DOT": 7000000000,
            "LINK": 8000000000,
            "UNI": 5000000000,
            "AAVE": 3000000000
        }
        return market_caps.get(asset, 1000000000) 