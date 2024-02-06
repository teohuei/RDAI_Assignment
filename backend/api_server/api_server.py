# api_server.py

from fastapi import FastAPI
from routers import status, supportedlanguages, detect, translate

app = FastAPI()

app.include_router(status.router)
app.include_router(supportedlanguages.router)
app.include_router(detect.router)
app.include_router(translate.router)
