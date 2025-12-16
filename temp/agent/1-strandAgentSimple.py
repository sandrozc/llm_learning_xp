# =============================================================================
# STRANDS AGENT SIMPLE EXAMPLE
# =============================================================================

import os 
from strands import Agent
from strands.models.gemini import GeminiModel
from dotenv import load_dotenv
load_dotenv()

# -----------------------------------------------------------------------------
# Agent Initialization
# -----------------------------------------------------------------------------
# Create an agent with default settings

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

agent = Agent(model = model)

# -----------------------------------------------------------------------------
# Agent Interaction
# -----------------------------------------------------------------------------
# Ask the agent a question
agent("Tell me about agentic AI, short answer")

# -----------------------------------------------------------------------------
# Execution Instructions
# -----------------------------------------------------------------------------
# Run this file with: python -u 1-strandAgentSimple.py
