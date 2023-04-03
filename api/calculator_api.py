from fastapi import FastAPI, HTTPException

from calculator import sub, div, mul

app = FastAPI()

@app.get("/api/mul")
async def api_mul(a: float, b: float):
    return {"result": mul(a, b)}

@app.get("/api/sub")
async def api_sub(a: float, b: float):
    return {"result": sub(a, b)}

@app.get("/api/div")
async def api_div(a: float, b: float):
    if b == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    return {"result": div(a, b)}

