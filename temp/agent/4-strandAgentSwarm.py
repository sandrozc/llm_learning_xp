# =============================================================================
# STRANDS AGENT SWARM EXAMPLE
# =============================================================================


import os
import logging
from strands import Agent
from strands.multiagent import Swarm
from strands.models.gemini import GeminiModel
from dotenv import load_dotenv
load_dotenv()

# -----------------------------------------------------------------------------
# Logging Configuration
# -----------------------------------------------------------------------------

logging.getLogger("strands.multiagent").setLevel(logging.DEBUG)
logging.basicConfig(
    format="%(levelname)s | %(name)s | %(message)s", handlers=[logging.StreamHandler()]
)

# -----------------------------------------------------------------------------
# Model Configuration
# -----------------------------------------------------------------------------
# Configure the Gemini model to use for all agents
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
# -----------------------------------------------------------------------------
# Specialized Agent Definitions
# -----------------------------------------------------------------------------
# Create specialized agents with different roles and expertise
researcher = Agent(
    name="researcher",
    system_prompt="You are a research specialist...",
    model=model,
)
coder = Agent(
    name="coder", system_prompt="You are a coding specialist...", model=model
)
reviewer = Agent(
    name="reviewer",
    system_prompt="You are a code review specialist...",
    model=model,
)
architect = Agent(
    name="architect",
    system_prompt="You are a system architecture specialist...",
    model=model,
)

# -----------------------------------------------------------------------------
# Swarm Configuration
# -----------------------------------------------------------------------------
# Create a swarm with these agents
swarm = Swarm(
    [researcher, coder, reviewer, architect],
    max_handoffs=20,
    execution_timeout=900.0,  # 15 minutes
    node_timeout=300.0,  # 5 minutes per agent
    repetitive_handoff_detection_window=8,  # There must be >= 3 unique agents in the last 8 handoffs
)

# -----------------------------------------------------------------------------
# Swarm Execution
# -----------------------------------------------------------------------------

result = swarm("Design and implement a simple REST API for a todo app")

# -----------------------------------------------------------------------------
# Result Analysis
# -----------------------------------------------------------------------------

print(f"Status: {result.status}")
print(f"Node history: {[node.node_id for node in result.node_history]}")


# -----------------------------------------------------------------------------
# Execution Instructions
# -----------------------------------------------------------------------------
# Run this file with: python 4-strandAgentSwarm.py
