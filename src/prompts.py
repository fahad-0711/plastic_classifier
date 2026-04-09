# src/prompts.py

ENGINEERING_SYSTEM_PROMPT = """
<system_instructions>
Task: Chemical Safety Analysis for 3D Printing.
Domain: Chemical Engineering / Waste Management.

Rules:
1. Identify Chemical Formula & Combustion Byproducts.
2. Check RoHS Compliance.
3. If Code 3 (PVC), trigger immediate SAFETY_REFUSAL.
</system_instructions>
"""

# src/prompts.py

# Claude-style (Uses XML and Human/Assistant tags)
CLAUDE_PROMPT = """
Human: <instructions>
Identify the plastic resin code and chemical safety. 
Input: {material}
</instructions>

Assistant: <analysis>
"""

# Titan-style (Uses clear bullet points and newlines)
TITAN_PROMPT = """
Instruction: Classify the following plastic material.
Context: 3D Printing Safety.
Input: {material}

Output Indicator: Provide 3 bullet points.\n
"""