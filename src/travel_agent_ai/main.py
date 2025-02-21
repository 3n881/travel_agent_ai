#!/usr/bin/env python
import sys
# import warnings

from datetime import datetime

from travel_agent_ai.crew import TravelAgentAi

# warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
            "source_location": "New York, USA",
            "destination_location": "Paris, France",
            "travel_date": "2025-03-15",
            "travel_duration": "7 days",
            "number_of_travelers": 2,
            "travel_companions_type": "Family",
            "budget_per_person": 1500,
            "preferred_travel_mode": "Flight",
            "accommodation_type": "Hotel",
            "meal_preferences": "Vegetarian",
            "interests": ["Museums", "Historical Sites", "Food Tasting"],
            "accessibility_needs": "Wheelchair accessible hotel room",
            "dietary_restrictions": "Gluten-free",
            "special_requests": "Early check-in and city view room",
            "date": datetime.now().isoformat(),
    }
    TravelAgentAi().crew().kickoff(inputs=inputs)

# if __name__ == "__main__":
#     run()

def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {"topic": "AI LLMs"}
    try:
        TravelAgentAi().crew().train(
            n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        TravelAgentAi().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {"topic": "AI LLMs"}
    try:
        TravelAgentAi().crew().test(
            n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

