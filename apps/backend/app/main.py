from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def hw():
    return "Hello World!"
