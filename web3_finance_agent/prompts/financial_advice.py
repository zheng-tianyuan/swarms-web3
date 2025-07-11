"""
Financial Investment Advice Prompt Templates

Contains investment advice, risk assessment, portfolio optimization, and other financial-related prompts.
"""


class FinancialAdvicePrompts:
    """Financial Investment Advice Prompts Class"""
    
    def get_investment_advice_prompt(self, asset: str, risk_tolerance: str, price_data: dict) -> str:
        """
        Get investment advice prompt
        
        Args:
            asset: Asset name
            risk_tolerance: Risk tolerance level
            price_data: Price data
            
        Returns:
            Investment advice prompt
        """
        return f"""
        Based on current market data, provide professional investment advice for asset "{asset}".
        
        Current price data: {price_data}
        Investor risk tolerance: {risk_tolerance}
        
        Please provide the following analysis:
        
        1. **Technical Analysis**:
           - Price trend analysis
           - Support and resistance levels
           - Technical indicator interpretation
           - Short-term and long-term trend predictions
        
        2. **Fundamental Analysis**:
           - Project fundamental assessment
           - Team and development progress
           - Ecosystem development
           - Market position and competitive advantages
        
        3. **Risk Assessment**:
           - Market risk analysis
           - Technical risk assessment
           - Regulatory risk considerations
           - Liquidity risk analysis
        
        4. **Investment Recommendations**:
           - Investment strategies suitable for {risk_tolerance} risk tolerance
           - Entry timing suggestions
           - Position management advice
           - Stop-loss and take-profit settings
        
        5. **Risk Control**:
           - Capital management recommendations
           - Diversification strategies
           - Risk control measures
        
        Please provide objective and professional investment advice, emphasizing risk management and long-term investment value.
        """
    
    def get_portfolio_optimization_prompt(self, assets: list, risk_profile: str, asset_data: dict) -> str:
        """
        Get portfolio optimization prompt
        
        Args:
            assets: List of assets
            risk_profile: Risk profile
            asset_data: Asset data
            
        Returns:
            Portfolio optimization prompt
        """
        return f"""
        Optimize investment portfolio for investors with "{risk_profile}" risk profile.
        
        Current assets: {assets}
        Asset data: {asset_data}
        
        Please provide the following optimization recommendations:
        
        1. **Asset Allocation Analysis**:
           - Weight distribution across asset classes
           - Correlation analysis
           - Diversification effectiveness assessment
        
        2. **Risk-Return Optimization**:
           - Risk-adjusted return analysis
           - Sharpe ratio optimization
           - Maximum drawdown control
        
        3. **Rebalancing Strategy**:
           - Regular rebalancing recommendations
           - Trigger condition settings
           - Adjustment frequency suggestions
        
        4. **New Asset Recommendations**:
           - Recommended new assets
           - Allocation ratio suggestions
           - Entry timing
        
        5. **Risk Management**:
           - Overall risk control
           - Single asset risk limits
           - Liquidity management
        
        6. **Monitoring Indicators**:
           - Key monitoring indicators
           - Alert mechanisms
           - Adjustment trigger conditions
        
        Please provide professional portfolio optimization advice, balancing risk and return.
        """
    
    def get_market_timing_prompt(self, market_conditions: dict) -> str:
        """
        Get market timing analysis prompt
        
        Args:
            market_conditions: Market conditions
            
        Returns:
            Market timing analysis prompt
        """
        return f"""
        Conduct timing analysis based on current market conditions:
        
        Market conditions: {market_conditions}
        
        Please analyze the following aspects:
        
        1. **Market Cycle Analysis**:
           - Current market cycle stage
           - Bull/bear market characteristics
           - Cycle transition signals
        
        2. **Sentiment Indicators**:
           - Fear and greed index
           - Market sentiment analysis
           - Extreme sentiment signals
        
        3. **Technical Indicators**:
           - Major technical indicator interpretation
           - Overbought/oversold signals
           - Trend confirmation signals
        
        4. **Fundamental Signals**:
           - Macroeconomic indicators
           - Regulatory policy impact
           - Institutional fund flows
        
        5. **Timing Recommendations**:
           - Optimal entry timing
           - Staged position building strategies
           - Risk control measures
        
        Please provide professional market timing analysis to help investors capture the best investment opportunities.
        """
    
    def get_risk_assessment_prompt(self, investment_strategy: str) -> str:
        """
        Get risk assessment prompt
        
        Args:
            investment_strategy: Investment strategy
            
        Returns:
            Risk assessment prompt
        """
        return f"""
        Conduct comprehensive risk assessment for investment strategy "{investment_strategy}":
        
        Please assess the following risk dimensions:
        
        1. **Market Risk**:
           - Systematic risk
           - Market volatility risk
           - Liquidity risk
        
        2. **Technical Risk**:
           - Smart contract risk
           - Cybersecurity risk
           - Technical failure risk
        
        3. **Regulatory Risk**:
           - Policy change risk
           - Compliance risk
           - Legal uncertainty
        
        4. **Operational Risk**:
           - Private key management risk
           - Trading platform risk
           - Human error risk
        
        5. **Project Risk**:
           - Team risk
           - Technology development risk
           - Competitive risk
        
        6. **Risk Mitigation Measures**:
           - Risk control strategies
           - Insurance measures
           - Emergency response plans
        
        Please provide detailed risk assessment report, including risk levels and mitigation recommendations.
        """ 