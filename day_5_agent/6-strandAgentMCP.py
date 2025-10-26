# =============================================================================
# STRANDS AGENT WITH MCP (MODEL CONTEXT PROTOCOL) AND LANGFUSE
# =============================================================================
# This example demonstrates how to create a custom MCP server and integrate it
# with a Strands Agent alongside the AWS Documentation MCP server.
# You'll see how agents can combine custom and existing MCP tools seamlessly
# while maintaining full Langfuse observability.
# =============================================================================

import os
import json
from typing import Dict, List, Any
from dotenv import load_dotenv
from strands import Agent, tool
from strands_tools import calculator
from strands.models import BedrockModel
from langfuse import Langfuse, observe
from mcp import stdio_client, StdioServerParameters
from strands.tools.mcp import MCPClient

# Load environment variables
load_dotenv()

# Initialize Langfuse client
langfuse = Langfuse(
    public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
    secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
    host=os.getenv("LANGFUSE_HOST", "https://cloud.langfuse.com"),
)


# =============================================================================
# CUSTOM MCP SERVER IMPLEMENTATION
# =============================================================================
class AWSLabMCPServer:
    """
    A custom MCP (Model Context Protocol) server for managing AWS lab environments
    and project resources. This demonstrates how to build domain-specific MCP servers.

    This server manages:
    - Student AWS lab configurations
    - Project deployment status
    - AWS service usage tracking
    - Lab environment recommendations
    """

    def __init__(self):
        # Simulated AWS lab configurations for students
        self.lab_configs = {
            "STU001": {
                "name": "Alice Johnson",
                "project": "RAG Chatbot",
                "aws_services": ["Bedrock", "S3", "Lambda"],
                "region": "us-east-1",
                "status": "deployed",
                "estimated_cost": "$12.50/month",
                "last_deployment": "2025-10-25",
            },
            "STU002": {
                "name": "Bob Smith",
                "project": "Fine-tuning Pipeline",
                "aws_services": ["SageMaker", "S3", "ECR"],
                "region": "eu-west-3",
                "status": "in-progress",
                "estimated_cost": "$45.00/month",
                "last_deployment": "2025-10-24",
            },
            "STU003": {
                "name": "Carol Davis",
                "project": "Bedrock Agent",
                "aws_services": ["Bedrock Agents", "Lambda", "DynamoDB", "SNS"],
                "region": "us-east-1",
                "status": "testing",
                "estimated_cost": "$8.75/month",
                "last_deployment": "2025-10-26",
            },
        }

        # AWS service recommendations based on use cases
        self.service_recommendations = {
            "rag": {
                "services": [
                    "Amazon Bedrock Knowledge Bases",
                    "Amazon OpenSearch",
                    "S3",
                    "Lambda",
                ],
                "estimated_cost": "$10-50/month",
                "difficulty": "Intermediate",
            },
            "fine-tuning": {
                "services": ["Amazon SageMaker", "S3", "ECR", "CloudWatch"],
                "estimated_cost": "$40-200/month",
                "difficulty": "Advanced",
            },
            "agents": {
                "services": ["Amazon Bedrock Agents", "Lambda", "DynamoDB", "SNS"],
                "estimated_cost": "$5-30/month",
                "difficulty": "Intermediate",
            },
            "inference-optimization": {
                "services": ["Amazon Bedrock", "Lambda", "API Gateway", "CloudWatch"],
                "estimated_cost": "$15-100/month",
                "difficulty": "Advanced",
            },
        }

    def get_lab_config(self, student_id: str) -> Dict[str, Any]:
        """Retrieve AWS lab configuration for a student."""
        return self.lab_configs.get(
            student_id.upper(),
            {"error": f"No lab configuration found for {student_id}"},
        )

    def get_service_recommendations(self, use_case: str) -> Dict[str, Any]:
        """Get AWS service recommendations for a specific use case."""
        use_case_lower = use_case.lower()
        for key, value in self.service_recommendations.items():
            if key in use_case_lower:
                return {"use_case": key, **value}
        return {"error": f"No recommendations found for use case: {use_case}"}

    def list_all_projects(self) -> List[Dict[str, str]]:
        """List all student projects and their status."""
        return [
            {
                "student_id": student_id,
                "name": config["name"],
                "project": config["project"],
                "status": config["status"],
            }
            for student_id, config in self.lab_configs.items()
        ]

    def estimate_cost(
        self, services: List[str], hours_per_month: int = 720
    ) -> Dict[str, Any]:
        """Estimate AWS costs for given services."""
        # Simplified cost estimation (educational purposes)
        cost_per_service = {
            "Bedrock": 0.005 * hours_per_month,  # Per request pricing simplified
            "S3": 2.00,  # Storage
            "Lambda": 0.20 * (hours_per_month / 100),  # Invocations
            "SageMaker": 0.269 * (hours_per_month / 24),  # ml.m5.xlarge
            "DynamoDB": 1.25,  # On-demand pricing
            "SNS": 0.50,  # Notifications
            "Bedrock Agents": 0.01 * hours_per_month,
            "ECR": 1.00,
            "CloudWatch": 0.30,
            "OpenSearch": 15.00,
            "API Gateway": 3.50,
        }

        total = sum(cost_per_service.get(service, 5.0) for service in services)

        return {
            "services": services,
            "estimated_monthly_cost": f"${total:.2f}",
            "breakdown": {
                service: f"${cost_per_service.get(service, 5.0):.2f}"
                for service in services
            },
        }


# =============================================================================
# CUSTOM MCP-CONNECTED TOOLS
# =============================================================================
# Initialize the custom AWS Lab MCP server
aws_lab_mcp = AWSLabMCPServer()


@tool
def get_student_lab_config(student_id: str) -> str:
    """
    Get AWS lab configuration for a specific student including their project,
    deployed services, region, and estimated costs.

    Args:
        student_id (str): The student ID to look up (e.g., 'STU001')

    Returns:
        str: Student's AWS lab configuration as formatted JSON
    """
    result = aws_lab_mcp.get_lab_config(student_id)
    return json.dumps(result, indent=2)


@tool
def get_aws_recommendations(use_case: str) -> str:
    """
    Get AWS service recommendations for a specific use case like RAG,
    fine-tuning, agents, or inference optimization.

    Args:
        use_case (str): The use case (e.g., 'rag', 'fine-tuning', 'agents')

    Returns:
        str: Recommended AWS services with cost estimates and difficulty level
    """
    result = aws_lab_mcp.get_service_recommendations(use_case)
    return json.dumps(result, indent=2)


@tool
def list_student_projects() -> str:
    """
    List all student projects with their current deployment status.

    Returns:
        str: List of all projects as formatted JSON
    """
    projects = aws_lab_mcp.list_all_projects()
    return json.dumps(projects, indent=2)


@tool
def estimate_aws_cost(services: str) -> str:
    """
    Estimate monthly AWS costs for a comma-separated list of services.

    Args:
        services (str): Comma-separated AWS service names (e.g., 'Bedrock,S3,Lambda')

    Returns:
        str: Cost estimate with breakdown as formatted JSON
    """
    service_list = [s.strip() for s in services.split(",")]
    result = aws_lab_mcp.estimate_cost(service_list)
    return json.dumps(result, indent=2)


# =============================================================================
# EXISTING MCP INTEGRATION (AWS Documentation MCP)
# =============================================================================
# This integrates the official AWS Documentation MCP server from AWS Labs.
# It provides real-time access to AWS service documentation.
# Installation: uvx awslabs.aws-documentation-mcp-server@latest
stdio_mcp_client = MCPClient(
    lambda: stdio_client(
        StdioServerParameters(
            command="uvx", args=["awslabs.aws-documentation-mcp-server@latest"]
        )
    )
)


# =============================================================================
# MAIN EXECUTION
# =============================================================================
if __name__ == "__main__":
    with stdio_mcp_client:

        @observe(name="strands_agent_mcp_interaction")
        def run_agent_with_mcp(message: str, session_id: str = "default"):
            """
            Run the agent with dual MCP server integration:
            1. Custom AWS Lab MCP (student projects, cost estimation)
            2. AWS Documentation MCP (official AWS docs)

            Plus full Langfuse observability tracking.

            Args:
                message (str): The user message to process
                session_id (str): Session identifier for tracking conversations
            """
            # Configure Bedrock model
            bedrock_model = BedrockModel(
                model_id="eu.amazon.nova-pro-v1:0",
            )

            # Combine custom tools with AWS Documentation MCP tools
            # This demonstrates how agents can use multiple MCP servers simultaneously
            custom_tools = [
                calculator,
                get_student_lab_config,
                get_aws_recommendations,
                list_student_projects,
                estimate_aws_cost,
            ]

            # Add AWS Documentation MCP tools
            aws_docs_tools = [t for t in stdio_mcp_client.list_tools_sync()]

            all_tools = custom_tools + aws_docs_tools

            agent = Agent(model=bedrock_model, tools=all_tools)

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
        print("STRANDS AGENT WITH DUAL MCP SERVERS AND LANGFUSE - DEMO")
        print("=" * 80 + "\n")

        # Example 1: Custom MCP - Student Lab Configuration
        message_1 = """
        I'm student STU003. Can you:
        1. Show me my current AWS lab configuration
        2. Tell me what AWS services I'm using
        3. What's my estimated monthly cost?
        """

        print("\n--- Example 1: Custom MCP - Student Lab Query ---")
        run_agent_with_mcp(message_1, session_id="mcp_session_001")

        # Example 2: Combining Custom MCP + AWS Docs MCP
        message_2 = """
        I want to build a RAG application for my project. Can you:
        1. What AWS services do you recommend for RAG?
        2. Look up AWS Bedrock Knowledge Bases documentation to explain how it works
        3. Estimate the monthly cost for: Bedrock, S3, Lambda, OpenSearch
        """

        print("\n--- Example 2: Dual MCP - Custom Recommendations + AWS Docs ---")
        run_agent_with_mcp(message_2, session_id="mcp_session_002")

        # Example 3: AWS Documentation MCP - Technical Deep Dive
        message_3 = """
        I'm working with Amazon Bedrock Agents for my project. Can you:
        1. Search AWS documentation for how Bedrock Agents work
        2. What's the difference between Bedrock Agents and regular Lambda functions?
        3. List all current student projects and their status
        """

        print("\n--- Example 3: AWS Docs MCP + Project Status ---")
        run_agent_with_mcp(message_3, session_id="mcp_session_003")

        # Example 4: Cost Planning with Multiple Services
        message_4 = """
        I'm planning a fine-tuning project. Can you:
        1. Get AWS service recommendations for fine-tuning
        2. Calculate the estimated cost for: SageMaker, S3, ECR, CloudWatch
        3. Compare it with the cost of a RAG-based approach
        """

        print("\n--- Example 4: Cost Analysis and Planning ---")
        run_agent_with_mcp(message_4, session_id="mcp_session_004")

        # Flush Langfuse to ensure all traces are sent
        langfuse.flush()

        print("\n" + "=" * 80)
        print("DUAL MCP DEMO COMPLETED!")
        print("=" * 80 + "\n")


# =============================================================================
# EXECUTION INSTRUCTIONS
# =============================================================================
# 1. Install AWS Documentation MCP server:
#    uvx awslabs.aws-documentation-mcp-server@latest
#
# 2. Set up your .env file with AWS and Langfuse credentials
#
# 3. Run this file with: python -u 6-strandAgentMCP.py
#
# 4. View traces in your Langfuse dashboard at https://cloud.langfuse.com
#
# 5. Observe how the agent:
#    - Uses custom MCP (AWS Lab config) for student-specific data
#    - Uses AWS Docs MCP for official AWS documentation
#    - Seamlessly combines both MCP sources
#    - Tracks all interactions in Langfuse
#
# Key Learning Points:
# - Custom MCP servers can be built for domain-specific needs
# - Existing MCP servers (like AWS Docs) provide real-time information
# - Agents can use multiple MCP servers simultaneously
# - Langfuse provides full observability into MCP usage
