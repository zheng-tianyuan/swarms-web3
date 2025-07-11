"""
Blockchain Technology Analysis Prompt Templates

Contains blockchain technology analysis, smart contract analysis, and other technical prompts.
"""


class BlockchainTechPrompts:
    """Blockchain Technology Analysis Prompts Class"""
    
    def get_tech_analysis_prompt(self, topic: str) -> str:
        """
        Get blockchain technology analysis prompt
        
        Args:
            topic: Technology topic
            
        Returns:
            Technology analysis prompt
        """
        return f"""
        Please provide a comprehensive analysis of blockchain technology topic "{topic}", including the following aspects:
        
        1. **Technical Fundamentals**:
           - Core technology principles
           - Key components and architecture
           - Consensus mechanisms involved
        
        2. **Innovation Analysis**:
           - Technical innovations and breakthroughs
           - Advantages over existing solutions
           - Scalability and performance characteristics
        
        3. **Security Assessment**:
           - Security mechanisms and protocols
           - Potential vulnerabilities and risks
           - Best practices and recommendations
        
        4. **Implementation Challenges**:
           - Technical implementation difficulties
           - Resource requirements
           - Adoption barriers
        
        5. **Market Impact**:
           - Industry applications and use cases
           - Competitive landscape
           - Future development potential
        
        6. **Investment Considerations**:
           - Technology maturity assessment
           - Development timeline
           - Investment risk factors
        
        Please provide detailed technical analysis with practical insights and investment implications.
        """
    
    def get_smart_contract_analysis_prompt(self, contract_name: str) -> str:
        """
        Get smart contract analysis prompt
        
        Args:
            contract_name: Contract name
            
        Returns:
            Smart contract analysis prompt
        """
        return f"""
        Please analyze the smart contract "{contract_name}" from technical and security perspectives:
        
        1. **Contract Architecture**:
           - Code structure and organization
           - Function design and logic
           - Gas optimization techniques
        
        2. **Security Analysis**:
           - Vulnerability assessment
           - Attack vector identification
           - Security best practices compliance
        
        3. **Functionality Review**:
           - Core functionality implementation
           - Business logic validation
           - Edge case handling
        
        4. **Audit Considerations**:
           - Code quality assessment
           - Testing coverage
           - Documentation completeness
        
        5. **Risk Assessment**:
           - Technical risks
           - Financial risks
           - Operational risks
        
        6. **Recommendations**:
           - Security improvements
           - Optimization suggestions
           - Best practices implementation
        
        Please provide comprehensive technical analysis with security focus.
        """
    
    def get_consensus_mechanism_prompt(self, mechanism: str) -> str:
        """
        Get consensus mechanism analysis prompt
        
        Args:
            mechanism: Consensus mechanism name
            
        Returns:
            Consensus mechanism analysis prompt
        """
        return f"""
        Please analyze the consensus mechanism "{mechanism}" in detail:
        
        1. **Technical Principles**:
           - Consensus algorithm explanation
           - Network participation requirements
           - Block validation process
        
        2. **Performance Characteristics**:
           - Transaction throughput
           - Confirmation times
           - Scalability limitations
        
        3. **Security Model**:
           - Attack resistance mechanisms
           - Byzantine fault tolerance
           - Economic security considerations
        
        4. **Energy and Resource Requirements**:
           - Computational requirements
           - Energy consumption
           - Hardware requirements
        
        5. **Decentralization Analysis**:
           - Network distribution
           - Centralization risks
           - Governance implications
        
        6. **Comparative Analysis**:
           - Advantages over other mechanisms
           - Trade-offs and limitations
           - Use case suitability
        
        Please provide in-depth technical analysis with practical implications.
        """
    
    def get_layer2_solution_prompt(self, solution: str) -> str:
        """
        Get Layer2 solution analysis prompt
        
        Args:
            solution: Layer2 solution name
            
        Returns:
            Layer2 solution analysis prompt
        """
        return f"""
        Please provide comprehensive analysis of Layer2 solution "{solution}":
        
        1. **Scaling Technology**:
           - Scaling approach and methodology
           - Data availability solutions
           - State management mechanisms
        
        2. **Security and Trust Model**:
           - Security assumptions
           - Trust requirements
           - Fraud proof mechanisms
        
        3. **Performance Metrics**:
           - Transaction throughput
           - Latency characteristics
           - Cost efficiency
        
        4. **Ecosystem Integration**:
           - Main chain compatibility
           - Developer tooling
           - User experience considerations
        
        5. **Economic Model**:
           - Token economics
           - Fee structures
           - Incentive mechanisms
        
        6. **Adoption and Competition**:
           - Market positioning
           - Competitive advantages
           - Adoption challenges
        
        Please provide detailed analysis focusing on technical innovation and practical value.
        """ 