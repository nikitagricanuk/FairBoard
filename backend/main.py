from fastapi import FastAPI
app = FastAPI()

usersinfo=[('a3df763e-8723-4b98-91cf-fd2537dfbc9c', 'Вова', 'Роднин', '012345', 6),
            ('b9a217c4-e3b7-46e1-9f98-54a2f6a7d9e0', 'Никита', 'Грицанюк', '153401', 4)]


problems=[
    ('a3df763e-8723-4b98-91cf-fd2537dfbc9c', '17.2') ,
    ('b9a217c4-e3b7-46e1-9f98-54a2f6a7d9e0', '17.2')
         ]

@app.get("/problems")
def get_problems():
    return { "problems": problems }

@app.post("/assign")
def assign():
    return { 'tid': 1234, 'problems': ['12.1', '123.3'] }

@app.get("/info")
def info():
    return {"window": "current_window"}

@app.get("/list")
def list():
    return {"list":"list"}

@app.get("/")
async def read_root():
    return {"Hello": "World"}
