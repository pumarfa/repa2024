from fastapi import FastAPI

app = FastAPI()
app.title = "REPA IAViM - 2024"
app.version = "0.0.1"

@app.get('/', tags=['Home'])
def message():
    return "Hello World!"
