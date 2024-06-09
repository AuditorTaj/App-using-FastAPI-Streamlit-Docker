from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Designed by": "TAJ AHMED - PGD DS & AI (B5)"}

