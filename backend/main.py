from fastapi import FastAPI
app = FastAPI()

@app.get("/problems")
def problems():
    return { "problems": problems }

@app.post("assign")
def assign():
    return {"message": "Вы записались"}

@app.get("info")
def info():
    return {"window": "current_window"}

@app.get("list")
def list():
    return {"list":"list"}