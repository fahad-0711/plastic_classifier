# src/classifier.py
from prompts import ENGINEERING_SYSTEM_PROMPT, CLAUDE_PROMPT, TITAN_PROMPT

# NEW: Bedrock Parameter Configuration
# We use a low temperature (0.1) for safety and accuracy.
MODEL_CONFIG = {
    "temperature": 0.9, 
    "maxTokenCount": 300,
    "topP": 0.9,
    "stopSequences": ["</analysis>", "Output:"]
}

def generate_model_specific_prompt(material, model_type="CLAUDE"):
    if model_type == "CLAUDE":
        return CLAUDE_PROMPT.format(material=material)
    else:
        return TITAN_PROMPT.format(material=material)

if __name__ == "__main__":
    # Test the new logic
    test_material = "Rigid white plastic with a waxy feel."
    print(f"Using Config: Temp={MODEL_CONFIG['temperature']}")
    print(generate_model_specific_prompt(test_material, "CLAUDE"))