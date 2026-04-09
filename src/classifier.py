import json

def generate_advanced_prompt(material_description):
    """
    Implements Chain-of-Thought (CoT) and Domain-Specific constraints.
    """
    prompt = f"""
    Task: Classify plastic material for 3D printing suitability.
    
    Context: We are using a household recycler. Safety is the priority.
    
    Instructions:
    1. Analyze physical characteristics: {material_description}
    2. Identify if it is a Thermoplastic (meltable) or Thermoset (burns/charred). 
       *Crucial: If it is a Thermoset, 'printable' must be NO.*
    3. Determine Resin Code (1-7).
    4. Evaluate toxic fume risk (e.g., PVC/Code 3 is dangerous).
    
    Format your response:
    - Reasoning: [Step-by-step logic]
    - Result: {{ "code": "", "type": "", "is_thermoset": bool, "printable": "YES/NO" }}
    """
    return prompt

if __name__ == "__main__":
    # Test case: A common household item
    test_waste = "A yellow detergent bottle, very thick, waxy surface, doesn't snap when bent."
    
    # Generate the prompt
    final_prompt = generate_advanced_prompt(test_waste)
    
    # Print the output to see your engineering work
    print("--- PREPARED PROMPT ---")
    print(final_prompt)

    p = generate_advanced_prompt("A clear, rigid bottle with a '3' on the bottom.")
    print(p)