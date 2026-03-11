from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from app.chains import pet_info, math_explanation
from app.tools import calculate
from app.memory import add_memory, get_memory

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

@app.get("/dog")
def search_dog(breed: str):

    description, countries = pet_info(breed)

    add_memory(f"Dog searched: {breed}")

    return {
        "description": description,
        "countries": countries
    }

@app.get("/pet")
def get_pet(breed: str):

    description, countries = pet_info(breed)

    add_memory(f"Breed searched: {breed}")

    return {
        "description": description,
        "countries": countries
    }


@app.get("/math")
def solve_math(expression: str):

    result = calculate(expression)

    explanation = math_explanation(expression)

    add_memory(f"Math: {expression} = {result}")

    return {
        "result": result,
        "explanation": explanation
    }