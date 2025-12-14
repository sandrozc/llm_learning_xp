# Day 5: Agentic AI with Observability

## Overview

This module focuses on building production-ready AI agents using AWS Strands Agent Framework, with emphasis on observability, monitoring, and the Model Context Protocol (MCP). You'll learn how to track agent behavior, integrate external context sources, and build maintainable agentic systems.

## Learning Objectives

By the end of this module, you will:
- Build AI agents using AWS Strands Agent Framework
- Integrate Langfuse for comprehensive agent observability
- Track custom metrics and trace agent interactions
- Implement Model Context Protocol (MCP) for structured context
- Combine multiple tools and context sources in production agents
- Monitor and debug agentic systems effectively

## Exercises

### 1. Simple Strands Agent (`1-strandAgentSimple.py`)

**What you'll learn:**
- Basic Strands Agent setup and configuration
- Working with AWS Bedrock models
- Simple agent-user interactions

**Key concepts:** Agent initialization, model configuration, basic prompting

---

### 2. Strands Agent with Tools (`2-strandAgentBasic.py`)

**What you'll learn:**
- Create custom tools using the `@tool` decorator
- Integrate built-in tools from strands-tools package
- Enable agents to perform calculations and access real-time data
- Handle multi-step reasoning with tool chains

**Key concepts:** Tool creation, function calling, tool orchestration

---

### 3. Advanced Agent Patterns (`3-strandAgentAsTools.py`)

**What you'll learn:**
- Use agents as tools for other agents
- Build hierarchical agent architectures
- Implement specialized agents for specific tasks
- Chain multiple agents together

**Key concepts:** Agent composition, hierarchical reasoning, task delegation

---

### 4. Multi-Agent Swarms (`4-strandAgentSwarm.py`)

**What you'll learn:**
- Coordinate multiple agents working together
- Implement swarm intelligence patterns
- Handle parallel agent execution
- Aggregate results from multiple agents

**Key concepts:** Swarm intelligence, parallel processing, result aggregation

---

### 5. Agent Observability with Langfuse (`5-strandAgentObs.py`)

**What you'll learn:**
- Integrate Langfuse for agent tracing and monitoring
- Track tool usage and execution metrics
- Implement custom scoring and metrics
- Debug agent behavior with detailed traces
- Monitor session-based interactions

**Key concepts:** Observability, tracing, custom metrics, session tracking, debugging

**Tools implemented:**
- Calculator (built-in)
- Web search (custom simulated)
- Text analyzer (custom)

---

### 6. Model Context Protocol (MCP) Integration (`6-strandAgentMCP.py`)

**What you'll learn:**
- Understand Model Context Protocol (MCP) fundamentals
- Build a custom MCP server for AWS lab management
- Integrate existing MCP servers (AWS Documentation)
- Combine multiple MCP sources in a single agent
- Provide external context to agents via MCP
- Track MCP usage with Langfuse observability

**Key concepts:** MCP architecture, dual MCP integration, AWS service recommendations, cost estimation

**MCP implementations:**
- **Custom MCP:** AWS Lab configurations with student projects, service recommendations, and cost estimation
- **AWS Documentation MCP:** Official AWS service documentation lookup (real-time)
- **Tools:** Lab config queries, AWS recommendations, cost calculator, project status, AWS docs search

---

## Prerequisites
- **AWS Account** with Bedrock access (us-east-1 or eu-west-3)
- **Langfuse Account** (free tier available at https://cloud.langfuse.com)
- Environment variables configured in `.env` file


1. **Create and activate virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   # or
   .venv\Scripts\activate  # Windows
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables:**
   - Create a [LangFuse Account](https://cloud.langfuse.com/)
   - Copy `.env.example`, rename it `.env` template and add your credentials
   - Required: AWS Bearer Token, Langfuse Public Key, Langfuse Secret Key

