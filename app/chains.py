from app.llm import llm
from app.prompts import description_prompt, country_prompt, math_prompt

description_chain = description_prompt | llm
country_chain = country_prompt | llm
math_chain = math_prompt | llm


def pet_info(breed):

    description = description_chain.invoke({"breed": breed}).content
    countries = country_chain.invoke({"breed": breed}).content

    return description, countries


def math_explanation(expression):

    explanation = math_chain.invoke({"expression": expression}).content

    return explanation