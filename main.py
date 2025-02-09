from flask import Flask, jsonify, request
import requests
import math

app = Flask(__name__)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n):
    num_str = str(n)
    num_len = len(num_str)
    return sum(int(digit) ** num_len for digit in num_str) == n

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    num = request.args.get('number')
    
    if not num or not num.isdigit():
        return jsonify({"number": num, "error": True}), 400

    num = int(num)
    properties = []
    
    if is_armstrong(num):
        properties.append("armstrong")
    properties.append("odd" if num % 2 != 0 else "even")

    # Fetch fun fact
    fun_fact_url = f"http://numbersapi.com/{num}/math"
    fun_fact_response = requests.get(fun_fact_url)
    fun_fact = fun_fact_response.text if fun_fact_response.status_code == 200 else "No fun fact available"

    return jsonify({
        "number": num,
        "is_prime": is_prime(num),
        "is_perfect": is_perfect(num),
        "properties": properties,
        "digit_sum": sum(int(digit) for digit in str(num)),
        "fun_fact": fun_fact
    })
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
