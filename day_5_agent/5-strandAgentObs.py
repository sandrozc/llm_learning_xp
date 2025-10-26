# =============================================================================
# STRANDS AGENT WITH LANGFUSE OBSERVABILITY
# =============================================================================
# This example demonstrates how to integrate Langfuse observability with a
# Strands Agent to track agent interactions, tool usage, and custom metrics.
# =============================================================================

import os
from dotenv import load_dotenv
from strands import Agent, tool
from strands_tools import calculator
from strands.models import BedrockModel
from langfuse import Langfuse, observe

# Load environment variables
load_dotenv()

# Initialize Langfuse client
langfuse = Langfuse(
    public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
    secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
    host=os.getenv("LANGFUSE_HOST", "https://cloud.langfuse.com"),
)


# -----------------------------------------------------------------------------
# Custom Tool Definitions with Observability
# -----------------------------------------------------------------------------
@tool
def web_search(query: str) -> str:
    """
    Simulate a web search tool that returns relevant information.

    Args:
        query (str): The search query

    Returns:
        str: Simulated search results
    """
    # Simulate web search results
    search_results = {
        "weather": "The current weather is sunny with a temperature of 72°F (22°C).",
        "python": "Python is a high-level, interpreted programming language known for its simplicity and readability.",
        "aws": "Amazon Web Services (AWS) is a comprehensive cloud computing platform offering over 200 services.",
    }

    # Find best match
    for key in search_results:
        if key.lower() in query.lower():
            return search_results[key]

    return f"Search results for '{query}': No specific information found. This is a simulated search result."


@tool
def text_analyzer(text: str) -> dict:
    """
    Analyze text and return various metrics.

    Args:
        text (str): The text to analyze

    Returns:
        dict: Analysis results including word count, character count, and sentence count
    """
    words = text.split()
    sentences = text.split(".")

    analysis = {
        "word_count": len(words),
        "character_count": len(text),
        "sentence_count": len([s for s in sentences if s.strip()]),
        "average_word_length": (
            sum(len(word) for word in words) / len(words) if words else 0
        ),
    }

    return analysis


# -----------------------------------------------------------------------------
# Observed Agent Function
# -----------------------------------------------------------------------------
@observe(name="strands_agent_interaction")
def run_agent_with_observability(message: str, session_id: str = "default"):
    """
    Run the agent with full Langfuse observability tracking.

    Args:
        message (str): The user message to process
        session_id (str): Session identifier for tracking conversations
    """
    # Configure Bedrock model
    bedrock_model = BedrockModel(
        model_id="eu.amazon.nova-pro-v1:0",
    )

    # Create agent with tools
    agent = Agent(model=bedrock_model, tools=[calculator, web_search, text_analyzer])

    # Execute agent
    print(f"\n{'='*80}")
    print(f"USER MESSAGE: {message}")
    print(f"{'='*80}\n")

    response = agent(message)

    print(f"\n{'='*80}")
    print("AGENT RESPONSE COMPLETED")
    print(f"{'='*80}\n")

    return response


# -----------------------------------------------------------------------------
# Main Execution
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    print("\n" + "=" * 80)
    print("STRANDS AGENT WITH LANGFUSE OBSERVABILITY - DEMO")
    print("=" * 80 + "\n")

    # Example 1: Multi-tool interaction
    message_1 = """
    I have 3 tasks for you:

    1. Search for information about Python programming language
    2. Calculate the result of (1234 + 5678) * 2
    3. Analyze this text: "Artificial intelligence is transforming the world. Machine learning powers modern applications."
    """

    print("\n--- Example 1: Multi-Tool Interaction ---")
    run_agent_with_observability(message_1, session_id="session_001")

    # Example 2: Web search focused
    message_2 = "What's the current weather like?"

    print("\n--- Example 2: Web Search Query ---")
    run_agent_with_observability(message_2, session_id="session_002")

    # Flush Langfuse to ensure all traces are sent
    langfuse.flush()

    print("\n" + "=" * 80)
    print("DEMO COMPLETED - Check your Langfuse dashboard for traces!")
    print("=" * 80 + "\n")


# -----------------------------------------------------------------------------
# Execution Instructions
# -----------------------------------------------------------------------------
# 1. Run this file with: python -u 5-strandAgentObs.py
# 2. View traces in your Langfuse dashboard at https://cloud.langfuse.com
