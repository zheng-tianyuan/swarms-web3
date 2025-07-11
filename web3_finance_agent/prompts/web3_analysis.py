"""
Web3 Analysis Prompt Templates

Contains DeFi protocol analysis, NFT project analysis, and other Web3-related prompts.
"""


class Web3AnalysisPrompts:
    """Web3 Analysis Prompts Class"""
    
    def get_defi_analysis_prompt(self, protocol_name: str) -> str:
        """
        Get DeFi protocol analysis prompt
        
        Args:
            protocol_name: Protocol name
            
        Returns:
            Analysis prompt
        """
        return f"""
        Please provide a comprehensive technical analysis of the DeFi protocol "{protocol_name}", including the following aspects:
        
        1. **Protocol Overview**:
           - Core functionality and positioning
           - Technical architecture and main components
           - Tokenomics model
        
        2. **Technical Analysis**:
           - Smart contract security assessment
           - Code audit status
           - Technical innovations and advantages
        
        3. **Market Analysis**:
           - TVL (Total Value Locked) trends
           - User activity and growth metrics
           - Competitive analysis
        
        4. **Risk Assessment**:
           - Smart contract risks
           - Liquidity risks
           - Regulatory risks
           - Market risks
        
        5. **Investment Recommendations**:
           - Suitable investment strategies
           - Risk-reward ratio assessment
           - Long-term development prospects
        
        Please provide detailed, professional, and objective analysis, focusing on technological innovation and practicality.
        """
    
    def get_nft_analysis_prompt(self, project_name: str) -> str:
        """
        Get NFT project analysis prompt
        
        Args:
            project_name: Project name
            
        Returns:
            Analysis prompt
        """
        return f"""
        Please provide an in-depth analysis of the NFT project "{project_name}", including the following aspects:
        
        1. **Project Background**:
           - Team and background
           - Project vision and goals
           - Community building and marketing strategies
        
        2. **Technical Features**:
           - Blockchain platform selection
           - Smart contract characteristics
           - Metadata storage solutions
           - Rarity algorithms
        
        3. **Market Performance**:
           - Floor price trends
           - Trading volume and activity
           - Holder distribution
           - Secondary market performance
        
        4. **Value Assessment**:
           - Artistic value and creativity
           - Utility and functionality
           - Brand value and influence
           - Long-term value potential
        
        5. **Risk Assessment**:
           - Market bubble risks
           - Technical risks
           - Regulatory risks
           - Liquidity risks
        
        6. **Investment Recommendations**:
           - Entry timing suggestions
           - Investment strategies
           - Risk control measures
        
        Please provide objective and comprehensive analysis, focusing on project uniqueness and long-term value.
        """
    
    def get_dao_analysis_prompt(self, dao_name: str) -> str:
        """
        Get DAO analysis prompt
        
        Args:
            dao_name: DAO name
            
        Returns:
            Analysis prompt
        """
        return f"""
        Please provide governance and investment analysis for the DAO "{dao_name}", including the following aspects:
        
        1. **Governance Structure**:
           - Voting mechanisms and weight distribution
           - Proposal process and execution mechanisms
           - Community participation levels
        
        2. **Financial Analysis**:
           - Treasury management and asset allocation
           - Revenue sources and expenditure
           - Tokenomics model
        
        3. **Project Evaluation**:
           - Investment portfolio quality
           - Project screening criteria
           - Risk management mechanisms
        
        4. **Community Analysis**:
           - Member activity levels
           - Governance participation
           - Community culture building
        
        5. **Investment Value**:
           - Token value assessment
           - Governance rights value
           - Long-term development prospects
        
        Please provide professional governance and investment analysis.
        """
    
    def get_layer2_analysis_prompt(self, solution_name: str) -> str:
        """
        Get Layer2 solution analysis prompt
        
        Args:
            solution_name: Solution name
            
        Returns:
            Analysis prompt
        """
        return f"""
        Please provide technical analysis of the Layer2 solution "{solution_name}", including the following aspects:
        
        1. **Technical Architecture**:
           - Scaling technology principles
           - Security mechanisms
           - Interaction with main chain
        
        2. **Performance Metrics**:
           - TPS (Transactions Per Second)
           - Confirmation times
           - Transaction fees
        
        3. **Ecosystem**:
           - Developer tools
           - Application ecosystem
           - User adoption metrics
        
        4. **Competitive Advantages**:
           - Technical advantages
           - Market positioning
           - Development roadmap
        
        5. **Risk Assessment**:
           - Technical risks
           - Security risks
           - Competitive risks
        
        Please provide in-depth technical analysis, focusing on innovation and practicality.
        """ 