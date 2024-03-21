import uvicorn
from fastapi import FastAPI
from routes import routes

app = FastAPI()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload="True")


@app.get("/", tags=["Root"])
async def root() -> dict:
    return {"message": "Hello World"}


app.include_router(routes)
