from langchain_core.prompts import ChatPromptTemplate

description_prompt = ChatPromptTemplate.from_template(
"""
You are a pet expert.

Describe the pet breed: {breed}.
"""
)

country_prompt = ChatPromptTemplate.from_template(
"""
List the top 3 countries where {breed} is popular.
Return only country names.
"""
)

math_prompt = ChatPromptTemplate.from_template(
"""
Explain step-by-step how to solve the math expression:

{expression}
"""
)