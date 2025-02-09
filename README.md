# Number Classification API

## Overview
This API classifies a given number and returns interesting mathematical properties along with a fun fact. It is built using **FastAPI** and deployed on **Render**.

## Features
- Accepts a number as a query parameter.
- Determines if the number is **prime**, **perfect**, or **an Armstrong number**.
- Identifies if the number is **odd** or **even**.
- Computes the **sum of its digits**.
- Fetches a **fun fact** about the number from the Numbers API.
- Returns JSON responses.

---
## API Endpoint
### **GET /api/classify-number?number=371**

#### **Successful Response (200 OK)**
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

#### **Error Response (400 Bad Request)**
```json
{
    "number": "alphabet",
    "error": true
}
```

---
## Tech Stack
- **Language**: Python
- **Framework**: FastAPI
- **Server**: Uvicorn
- **Deployment**: Render
- **External API**: [Numbers API](http://numbersapi.com)

---
## Setup & Installation

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/fawemimo-olukorede-A/number-classifier.git
cd number-classifier
```

### **2️⃣ Create a Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Run Locally**
```sh
uvicorn main:app --host 0.0.0.0 --port 10000
```

### **5️⃣ Test the API**
Open your browser and visit:
```
http://localhost:8080/api/classify-number?number=371
```

---
## Deployment on Render
### **1️⃣ Push Code to GitHub**
```sh
git add .
git commit -m "Initial commit"
git push origin main
```

### **2️⃣ Deploy on Render**
1. Go to [Render](https://render.com/) and log in.
2. Click **New Web Service** and connect your GitHub repository.
3. Set the **runtime** to Python.
4. Configure:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port 10000`
5. Click **Deploy** and wait for Render to assign a live URL.

### **3️⃣ Test Your Live API**
Once deployed, visit:
```
https://numberFastAPI.onrender.com/api/classify-number?number=371
```

---
## Contributing
Pull requests are welcome. For major changes, please open an issue first.

