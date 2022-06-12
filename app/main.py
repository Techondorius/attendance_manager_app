from fastapi import FastAPI

app = FastAPI(port=5000)


@app.get("/")
def read_root():
    return {"Hello": "World"}