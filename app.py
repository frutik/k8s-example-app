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
    app_port = int(os.getenv('APP_PORT', 9000))
    uvicorn.run(app, host="0.0.0.0", port=app_port)
