from prompts import ENGINEERING_SYSTEM_PROMPT
def generate_advanced_prompt(material_description):
    full_prompt= f"{ENGINEERING_SYSTEM_PROMPT}\n<user_input>{user_input}</user_input>"
    return full_prompt