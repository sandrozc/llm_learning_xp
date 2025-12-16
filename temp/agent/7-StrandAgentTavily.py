# =============================================================================
# EXERCISE: WEB SEARCH AGENT WITH TAVILY MCP AND LANGFUSE
# =============================================================================
# In this exercise, you will:
# 1. Create a web search agent using Tavily MCP for AI-optimized search
# 2. Implement comprehensive Langfuse observability to track agent behavior
# 3. Build custom tools that work with search results
# 4. Log all interactions, tool calls, and responses to Langfuse
# 5. Run and evaluate the agent's performance


import os
from typing import Dict, List, Any, Optional
from strands import Agent, tool
from strands.models.gemini import GeminiModel
from langfuse import observe
from mcp import stdio_client, StdioServerParameters
from strands.tools.mcp import MCPClient
from dotenv import load_dotenv

load_dotenv()


# =============================================================================
# TODO 1: INITIALIZE LANGFUSE CLIENT
# =============================================================================

langfuse = None  # TODO: Initialize Langfuse client


# =============================================================================
# TODO 2: SET UP TAVILY MCP CLIENT
# =============================================================================

tavily_mcp_client = None  # TODO: Initialize MCPClient for Tavily


# =============================================================================
# TODO 3: BUILD CUSTOM TOOLS FOR SEARCH RESULT PROCESSING
# =============================================================================

# TODO 3.1: Create a tool to summarize results

@tool
def summarize_search_results(search_results: str, max_results: int = 5) -> str:
    """
    Summarize the top search results into a concise format.

    Args:
        search_results (str): Raw search results from Tavily
        max_results (int): Maximum number of results to include in summary

    Returns:
        str: Summarized search results with key information
    """
    # TODO: Implement summarization logic
    # HINT: Extract title, URL, and snippet from each result
    # HINT: Format as numbered list with key details
    # HINT: Limit to max_results items
    pass


# TODO 3.2: Create a tool to filter results by domain
@tool
def filter_results_by_domain(search_results: str, allowed_domains: str) -> str:
    """
    Filter search results to only include specific domains.

    Args:
        search_results (str): Raw search results from Tavily
        allowed_domains (str): Comma-separated list of domains (e.g., "github.com,stackoverflow.com")

    Returns:
        str: Filtered search results as JSON
    """
    # TODO: Implement domain filtering
    # HINT: Parse allowed_domains string into a list
    # HINT: Check if result URL contains any allowed domain
    # HINT: Return filtered results as JSON string
    pass


# =============================================================================
# TODO 4: CREATE THE WEB SEARCH AGENT
# =============================================================================

def create_web_search_agent():
    """
    Create and configure a web search agent with Tavily MCP and custom tools.

    Returns:
        Agent: Configured agent ready to handle search queries
    """

    # TODO 4.1: Initialize the LLM model
    # HINT: Use GeminiModel with google API key
    # HINT: Set appropriate parameters (temperature, max_output_tokens, etc.)
    model = None  # TODO: Create GeminiModel instance

    # TODO 4.2: Gather all available tools
    # HINT: Get Tavily tools using tavily_mcp_client.list_tools_sync()
    # HINT: Combine with your custom tools (summarize, filter, extract)
    all_tools = []  # TODO: Collect all tools

    # TODO 4.3: Define the agent's system prompt
    # HINT: Describe the agent's purpose and capabilities
    # HINT: Explain when to use each tool
    # HINT: Encourage structured, helpful responses
    system_prompt = """
    TODO: Write a comprehensive system prompt for your web search agent
    """

    # TODO 4.4: Create the Agent instance
    agent = None  # TODO: Create Agent with model, tools, and system_prompt

    return agent


# =============================================================================
# TODO 5: IMPLEMENT TRACED AGENT EXECUTION
# =============================================================================


@observe(name="web_search_agent_execution")
def execute_search_query(agent: Agent, query: str, session_id: str = "default") -> Dict[str, Any]:
    """
    Execute a search query using the agent with full Langfuse tracing.

    Args:
        agent: The web search agent
        query: User's search query
        session_id: Session identifier for grouping related queries
    """
    
    
    pass


# =============================================================================
# TODO 5: IMPLEMENT ANY AGENT EVALUATION TYPE OF YOUR CHOICE
# =============================================================================
# HINT: https://strandsagents.com/latest/documentation/docs/user-guide/evals-sdk/evaluators/

# =============================================================================
# TODO 6: MAKE THINGS RUN
# =============================================================================
if __name__ == "__main__":

    pass

# -----------------------------------------------------------------------------
# Execution Instructions
# -----------------------------------------------------------------------------
# 1. Run this file with: python -u 7-strandAgentObs.py
# 2. View traces in your Langfuse dashboard at https://cloud.langfuse.com