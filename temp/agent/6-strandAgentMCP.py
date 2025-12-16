# =============================================================================
# STRANDS AGENT WITH MCP (MODEL CONTEXT PROTOCOL) AND LANGFUSE
# =============================================================================

import os
from typing import Dict, List, Any
from strands import Agent, tool
from strands_tools import calculator
from strands.models import BedrockModel
from langfuse import Langfuse, observe
from mcp import stdio_client, StdioServerParameters
from strands.tools.mcp import MCPClient
from strands.models.gemini import GeminiModel
from fastmcp import FastMCP
from dotenv import load_dotenv
load_dotenv()


# Initialize Langfuse client
langfuse = Langfuse(
    public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
    secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
    host=os.getenv("LANGFUSE_HOST", "https://cloud.langfuse.com"),
)


# -----------------------------------------------------------------------------
# MCP CLIENT SETUP
# -----------------------------------------------------------------------------

stdio_mcp_client = MCPClient(
    lambda: stdio_client(
        StdioServerParameters(
            command="uvx", args=["awslabs.aws-documentation-mcp-server@latest"]
        )
    )
)

# -----------------------------------------------------------------------------
# MAIN EXECUTION
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    with stdio_mcp_client:

        @observe(name="strands_agent_mcp_interaction")
        def run_agent_with_mcp(message: str, session_id: str = "default"):
            """
            Run the agent with dual MCP server integration:
            1. Custom AWS Lab MCP (student projects, cost estimation) - built with fastMCP
            2. AWS Documentation MCP (official AWS docs)

            Plus full Langfuse observability tracking.

            Args:
                message (str): The user message to process
                session_id (str): Session identifier for tracking conversations
            """
            # Configure model
            model = GeminiModel(
                client_args={
                    "api_key": os.getenv("GOOGLE_API_KEY"),
                },
                model_id="gemini-2.5-flash-lite",
                params={
                    "temperature": 0.7,
                    "max_output_tokens": 2048,
                    "top_p": 0.9,
                    "top_k": 40
                }
            )

            # Get tools from AWS Documentation MCP
            aws_docs_tools = [t for t in stdio_mcp_client.list_tools_sync()]

            # Add calculator tool for good measure
            all_tools = [calculator] + aws_docs_tools

            agent = Agent(model=model, tools=all_tools)

            # Execute agent
            print(f"\n{'='*80}")
            print(f"USER MESSAGE: {message}")
            print(f"{'='*80}\n")

            response = agent(message)
            print(f"\n{'='*80}")
            print("AGENT RESPONSE COMPLETED")
            print(f"{'='*80}\n")

            return response

        print("\n" + "=" * 80)
        print("STRANDS AGENT WITH FASTMCP AND AWS DOCUMENTATION MCP - DEMO")
        print("=" * 80 + "\n")

        # Example: Architecture recommendaiton and cost estimation
        prompt = """
        I am planning a student project using AWS services. 
        What are the latest release on Amazon Bedrock? 
        """
        
        run_agent_with_mcp(prompt)

        # Flush Langfuse to ensure all traces are sent
        langfuse.flush()

        print("\n" + "=" * 80)
        print("MCP DEMO COMPLETED!")
        print("=" * 80 + "\n")

# -----------------------------------------------------------------------------
# Execution Instructions
# -----------------------------------------------------------------------------
# Run this file with: python -u 6-strandAgentMCP.py