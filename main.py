from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json

app = FastAPI()

class NumberResponse(BaseModel):
    number: float
    is_prime: bool
    is_perfect: bool
    properties: list
    digit_sum: int
    fun_fact: str

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    if n < 1:
        return False
    return sum([i for i in range(1, n) if n % i == 0]) == n

def classify_number(number):
    properties = []
    if number % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")

    if is_prime(number):
        properties.append("prime")
    
    if is_perfect(number):
        properties.append("perfect")

    digit_sum = sum(int(digit) for digit in str(abs(int(number))))

    fun_fact = f"{number} is an interesting number!"

    return {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": digit_sum,
        "fun_fact": fun_fact
    }

@app.get("/classify-number")
async def classify(number: str):
    try:
        number = float(number)
        return NumberResponse(**classify_number(number))
    except ValueError:
        return {
            "number": number,
            "error": "Invalid number format"
        }, 400
