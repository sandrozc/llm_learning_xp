# =============================================================================
# STRANDS AGENT AS TOOLS EXAMPLE
# =============================================================================

import os
from strands import Agent, tool
import json
from datetime import datetime
import random
from strands.models.gemini import GeminiModel
from dotenv import load_dotenv
load_dotenv()

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
# Weather Data Tool
# -----------------------------------------------------------------------------
@tool
def get_weather(location: str) -> str:
    """
    Get current weather for a location (simulated).

    Args:
        location: City name or location

    Returns:
        Weather information in JSON format
    """
    # Simulate weather data (no external API needed)
    weather_conditions = ["sunny", "cloudy", "rainy", "snowy", "windy", "stormy"]
    temperatures = {
        "sunny": (75, 95),
        "cloudy": (60, 75),
        "rainy": (50, 65),
        "snowy": (20, 35),
        "windy": (55, 70),
        "stormy": (45, 65),
    }

    # Generate random but plausible weather
    condition = random.choice(weather_conditions)
    temp_range = temperatures[condition]
    temperature = random.randint(temp_range[0], temp_range[1])

    # Create weather data
    weather_data = {
        "location": location,
        "condition": condition,
        "temperature": temperature,
        "humidity": random.randint(30, 90),
        "wind_speed": random.randint(0, 25),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

    return json.dumps(weather_data, indent=2)


# -----------------------------------------------------------------------------
# Weather Analysis Agent
# -----------------------------------------------------------------------------
@tool
def weather_analyst(location: str) -> str:
    """
    Analyze weather conditions and provide a summary.

    Args:
        location: City name or location

    Returns:
        Weather analysis and summary
    """
    # Create a specialized weather analysis agent
    weather_agent = Agent(
        system_prompt="""
        You are a weather analysis expert. Given weather data:
        1. Summarize the current conditions in a friendly way
        2. Explain what the weather means for people's comfort
        3. Mention if any precautions should be taken
        
        Keep your response concise and helpful. Be short and concise.
        """,
        tools=[get_weather],  # Use our custom weather tool
        model=model,
    )

    # Format the output with clear section headers
    response = weather_agent(f"Analyze the weather in {location}")

    # Add visual formatting to make the output clear
    formatted_response = f"""
╔══════════════════════════════════════════════╗
║             WEATHER ANALYSIS                 ║
╚══════════════════════════════════════════════╝

📍 Location: {location}

{response}
"""
    return formatted_response


# -----------------------------------------------------------------------------
# Activity Recommendation Agent
# -----------------------------------------------------------------------------
@tool
def activity_recommender(weather_info: str) -> str:
    """
    Recommend activities based on weather conditions.

    Args:
        weather_info: Description of weather conditions

    Returns:
        List of recommended activities
    """
    # Create a specialized activity recommendation agent
    activity_agent = Agent(
        system_prompt="""
        You are an activity recommendation specialist. Based on weather conditions:
        1. Suggest 3-5 appropriate activities
        2. Explain why each activity is suitable for the weather
        3. Include both indoor and outdoor options when appropriate

        Be creative and practical with your suggestions. Be short and concise.
        """,
        model=model,
        # No additional tools needed for this agent
    )

    # Get recommendations based on weather
    response = activity_agent(f"Recommend activities for this weather: {weather_info}")

    # Format the output with clear section headers
    formatted_response = f"""
╔══════════════════════════════════════════════╗
║           ACTIVITY RECOMMENDATIONS           ║
╚══════════════════════════════════════════════╝

{response}
"""
    return formatted_response


# -----------------------------------------------------------------------------
# Main Orchestrator Agent
# -----------------------------------------------------------------------------
def main():
    # Create the orchestrator with a clear, helpful prompt
    orchestrator = Agent(
        system_prompt="""
        You are a Weather-Aware Activity Planner that helps people plan their day.
        
        WORKFLOW:
        1. First, use the weather_analyst tool to get current weather for the location
        2. Then, use the activity_recommender tool to suggest activities based on the weather
        3. Finally, summarize the plan in a friendly, helpful way
        
        Always follow this sequence and clearly explain what you're doing at each step.
        Make your responses visually appealing and easy to understand. Be short and concise.
        """,
        tools=[weather_analyst, activity_recommender],
        model=model,
    )

    # Print welcome message
    print(
        """
╔═══════════════════════════════════════════════════════════════════════╗
║                WEATHER-AWARE ACTIVITY PLANNER DEMO                    ║
╚═══════════════════════════════════════════════════════════════════════╝
    """
    )

    # Interactive demo
    while True:
        user_input = input("\n🔍 Your question (or 'exit' to quit): ")
        if user_input.lower() in ["exit", "quit", "q"]:
            print("\nThank you for using the Weather-Aware Activity Planner! Goodbye!")
            break

        print("\n⏳ Planning your activities...\n")
        response = orchestrator(user_input)
        print(f"\n{response}\n")
        print("=" * 80)

if __name__ == "__main__":
    main()


# -----------------------------------------------------------------------------
# Execution Instructions
# -----------------------------------------------------------------------------
# Run this file with: python 3-strandAgentAsTools.py
# -->Plan my activities for this week-end in Paris
