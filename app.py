import os
import uvicorn

from fastapi import FastAPI
from fastapi.logger import logger


app = FastAPI()


@app.get("/status")
def status():
    logger.warning('Request!')
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)
