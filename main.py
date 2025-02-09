from fastapi import FastAPI
import requests
import math

#python code

app = FastAPI()

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    if n < 1:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n):
    digits = [int(digit) for digit in str(n)]
    power = len(digits)
    return sum(d ** power for d in digits) == n

def get_fun_fact(n):
    try:
        response = requests.get(f"http://numbersapi.com/{n}/math", timeout=5)
        return response.text if response.status_code == 200 else "No fun fact found"
    except requests.RequestException:
        return "No fun fact found"

@app.get("/api/classify-number")
def classify_number(number: str):
    if not number.lstrip('-').isdigit():
        return {"number": number, "error": True}

    number = int(number)
    properties = ["armstrong" if is_armstrong(number) else "", "odd" if number % 2 != 0 else "even"]
    properties = list(filter(None, properties))

    response_data = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": sum(int(d) for d in str(number)),
        "fun_fact": get_fun_fact(number)
    }

    return response_data
