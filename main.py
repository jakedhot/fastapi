from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# HTML template for the calculator
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculator</title>
</head>
<body>
    <h1>Simple Calculator</h1>
    <form action="/calculate" method="get">
        <input type="number" name="num1" placeholder="Number 1" required>
        <select name="operation" required>
            <option value="+">+</option>
            <option value="-">-</option>
            <option value="*">*</option>
            <option value="/">/</option>
        </select>
        <input type="number" name="num2" placeholder="Number 2" required>
        <button type="submit">Calculate</button>
    </form>
    <div id="result"></div>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return html_content

@app.get("/calculate")
async def calculate(num1: float, num2: float, operation: str):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            return {"error": "Cannot divide by zero"}
        result = num1 / num2
    else:
        return {"error": "Invalid operation"}

    return {"result": result}
