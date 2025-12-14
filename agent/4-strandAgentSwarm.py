# =============================================================================
# STRANDS AGENT SWARM EXAMPLE
# =============================================================================
# This example demonstrates how to create a swarm of specialized agents that
# can collaborate on complex tasks. The swarm includes researchers, coders,
# reviewers, and architects working together.
# =============================================================================

import logging
from strands import Agent
from strands.multiagent import Swarm
from strands.models import BedrockModel

# -----------------------------------------------------------------------------
# Logging Configuration
# -----------------------------------------------------------------------------
# Enable debug logs and print them to stderr
logging.getLogger("strands.multiagent").setLevel(logging.DEBUG)
logging.basicConfig(
    format="%(levelname)s | %(name)s | %(message)s", handlers=[logging.StreamHandler()]
)

# -----------------------------------------------------------------------------
# Model Configuration
# -----------------------------------------------------------------------------
# Configure the Bedrock model to use for all agents
bedrock_model = BedrockModel(
    model_id="eu.anthropic.claude-3-7-sonnet-20250219-v1:0", temperature=0.2
)

# -----------------------------------------------------------------------------
# Specialized Agent Definitions
# -----------------------------------------------------------------------------
# Create specialized agents with different roles and expertise
researcher = Agent(
    name="researcher",
    system_prompt="You are a research specialist...",
    model=bedrock_model,
)
coder = Agent(
    name="coder", system_prompt="You are a coding specialist...", model=bedrock_model
)
reviewer = Agent(
    name="reviewer",
    system_prompt="You are a code review specialist...",
    model=bedrock_model,
)
architect = Agent(
    name="architect",
    system_prompt="You are a system architecture specialist...",
    model=bedrock_model,
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
# Execute the swarm on a task
result = swarm("Design and implement a simple REST API for a todo app")

# -----------------------------------------------------------------------------
# Result Analysis
# -----------------------------------------------------------------------------
# Access the final result
print(f"Status: {result.status}")
print(f"Node history: {[node.node_id for node in result.node_history]}")


# -----------------------------------------------------------------------------
# Execution Instructions
# -----------------------------------------------------------------------------
# Run this file with: python 4-strandAgentSwarm.py
