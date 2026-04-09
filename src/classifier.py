import boto3 # Standard AWS SDK
import json

def classify_plastic(user_input):
    # This is a FEW-SHOT prompt.
    # We give examples to guide the AI's logic.
    prompt_data = f"""
    Task: Classify the type of plastic and determine if it's 3D printable.
    
    Example 1:
    Input: "A clear water bottle with a crinkly sound."
    Output: {{ "type": "PET", "recyclable": true, "3D_printable": "No (requires industrial processing)" }}

    Example 2:
    Input: "A white milk jug, feels slightly waxy."
    Output: {{ "type": "HDPE", "recyclable": true, "3D_printable": "Yes (good for structural parts)" }}

    Input: "{user_input}"
    Output:
    """

    # In a real job, you'd use boto3 to call AWS Bedrock here.
    # For today, print the prompt to prove you engineered the structure.
    print("--- GENERATED PROMPT ---")
    print(prompt_data)
    print("--- END ---")

if __name__ == "__main__":
    test_waste = "A yellow detergent bottle, very thick plastic."
    classify_plastic(test_waste)