import os
import uvicorn

from fastapi import FastAPI, Form
from fastapi.logger import logger


app = FastAPI()

@app.on_event("startup")
def startup_event():
    logger.warning('Application startup')


@app.on_event("shutdown")
def shutdown_event():
    logger.warning('Application shutdown')


@app.get("/status")
def status():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)