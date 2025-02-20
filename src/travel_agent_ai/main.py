#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from travel_agent_ai.crew import TravelAgentAi

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def get_user_input(prompt, allow_empty=False):
    """Helper function to get user input with validation."""
    while True:
        value = input(prompt).strip()
        if value or allow_empty:
            return value
        print("This field cannot be empty. Please try again.")

def run(webhook_inputs=None):
    """
    Run the crew with either interactive user input or webhook inputs.
    
    Args:
        webhook_inputs (dict, optional): Inputs received from Zapier webhook
    """
    if webhook_inputs:
        inputs = {
            'source_location': webhook_inputs.get('source_location'),
            'destination_location': webhook_inputs.get('destination_location'),
            'travel_date': webhook_inputs.get('travel_date'),
            'travel_duration': webhook_inputs.get('travel_duration'),
            'number_of_travelers': webhook_inputs.get('number_of_travelers'),
            'travel_companions_type': webhook_inputs.get('travel_companions_type'),
            'budget_per_person': webhook_inputs.get('budget_per_person'),
            'preferred_travel_mode': webhook_inputs.get('preferred_travel_mode'),
            'accommodation_type': webhook_inputs.get('accommodation_type'),
            'meal_preferences': webhook_inputs.get('meal_preferences'),
            'interests': webhook_inputs.get('interests'),
            'accessibility_needs': webhook_inputs.get('accessibility_needs', ''),
            'dietary_restrictions': webhook_inputs.get('dietary_restrictions', ''),
            'special_requests': webhook_inputs.get('special_requests', ''),
            'date': datetime.now().isoformat()
        }
    else:
        inputs = {
            # Basic Travel Details
            'source_location': get_user_input("Enter source location: "),
            'destination_location': get_user_input("Enter destination location: "),
            'travel_date': get_user_input("Enter travel date (YYYY-MM-DD): "),
            'travel_duration': get_user_input("Enter travel duration (e.g., 5 days): "),
            
            # Travel Group & Budget
            'number_of_travelers': get_user_input("Enter number of travelers: "),
            'travel_companions_type': get_user_input("Enter travel companions type (Family/Friends/Solo/Couple): "),
            'budget_per_person': get_user_input("Enter budget per person (in INR): "),
            
            # Preferences
            'preferred_travel_mode': get_user_input("Enter preferred travel mode (Flight/Train/Car): "),
            'accommodation_type': get_user_input("Enter accommodation type (Hotel/Resort/Homestay): "),
            'meal_preferences': get_user_input("Enter meal preferences (Vegetarian/Non-Vegetarian): "),
            
            # Interests
            'interests': get_user_input("Enter interests (comma-separated: Adventure,Culture,Nature,Food,Shopping): "),
            
            # Special Requirements
            'accessibility_needs': get_user_input("Enter accessibility needs (or 'None'): ", allow_empty=True),
            'dietary_restrictions': get_user_input("Enter dietary restrictions (or 'None'): ", allow_empty=True),
            'special_requests': get_user_input("Enter any special requests: ", allow_empty=True),
            
            'date': datetime.now().isoformat()
        }
    
    try:
        TravelAgentAi().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

