from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    return sum([i for i in range(1, n) if n % i == 0]) == n

def digit_sum(n):
    return sum(int(digit) for digit in str(abs(n)))

def get_fun_fact(n):
    url = f"http://numbersapi.com/{n}/math?json"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json().get("text", "No fun fact found.")
    except:
        return "Could not fetch a fun fact."
    return "No fun fact available."

@app.get("/api/classify-number")
def classify_number(number: str):
    # Validate input: Ensure it's a number
    try:
        num = int(number)
    except ValueError:
        raise HTTPException(status_code=400, detail={"number": number, "error": True})

    # Determine properties
    properties = []
    if is_prime(num):
        properties.append("prime")
    if is_perfect(num):
        properties.append("perfect")
    if num == sum(int(d) ** len(str(num)) for d in str(num)):  # Armstrong check
        properties.append("armstrong")
    properties.append("odd" if num % 2 != 0 else "even")

    # Build response
    response = {
        "number": num,
        "is_prime": is_prime(num),
        "is_perfect": is_perfect(num),
        "properties": properties,
        "digit_sum": digit_sum(num),
        "fun_fact": get_fun_fact(num)
    }
    
    return response
