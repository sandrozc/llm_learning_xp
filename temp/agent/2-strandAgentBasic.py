# =============================================================================
# STRANDS AGENT BASIC EXAMPLE
# =============================================================================


import os
from strands import Agent, tool
from strands_tools import calculator, current_time
from strands.models.gemini import GeminiModel
from dotenv import load_dotenv
load_dotenv()

# -----------------------------------------------------------------------------
# Custom Tool Definition
# -----------------------------------------------------------------------------
# Define a custom tool as a Python function using the @tool decorator
@tool
def letter_counter(word: str, letter: str) -> int:
    """
    Count occurrences of a specific letter in a word.

    Args:
        word (str): The input word to search in
        letter (str): The specific letter to count

    Returns:
        int: The number of occurrences of the letter in the word
    """
    if not isinstance(word, str) or not isinstance(letter, str):
        return 0

    if len(letter) != 1:
        raise ValueError("The 'letter' parameter must be a single character")

    return word.lower().count(letter.lower())


# -----------------------------------------------------------------------------
# Agent Configuration
# -----------------------------------------------------------------------------
# Select your model
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

# Create an agent with tools from the strands-tools example tools package
# as well as our custom letter_counter tool
agent = Agent(model=model, tools=[calculator, current_time, letter_counter])


# -----------------------------------------------------------------------------
# Agent Interaction
# -----------------------------------------------------------------------------
# Ask the agent a question that uses the available tools
message = """
I have 3 requests:

1. What is the time right now?
2. Calculate 3111696 / 74088
3. Tell me how many letter R's are in the word "strawberry" 🍓

Be straightforward and concise in your answers.
"""
agent(message)


# -----------------------------------------------------------------------------
# Execution Instructions
# -----------------------------------------------------------------------------
# Run this file with: python -u 2-strandAgentBasic.py
