from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.database.database import Base, engine

import app.models.user
import app.models.disaster
import app.models.earthquake
import app.models.nasa_event

from app.api.user_routes import router as user_router
from app.api.auth_routes import router as auth_router
from app.api.disaster_routes import router as disaster_router
from app.api.weather_routes import router as weather_router
from app.api.prediction_routes import router as prediction_router
from app.api.earthquake_routes import router as earthquake_router
from app.api.nasa_routes import router as nasa_router
from app.api.profile_routes import router as profile_router
from app.api.map_routes import router as map_router

from app.middleware.logging_middleware import LoggingMiddleware
from app.exceptions.handlers import register_exception_handlers

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Global Disaster Intelligence Platform",
    version="3.4.0",
    description="AI Powered Disaster Intelligence Platform"
)

app.add_middleware(
    LoggingMiddleware
)

register_exception_handlers(app)

app.include_router(user_router)
app.include_router(auth_router)
app.include_router(disaster_router)
app.include_router(weather_router)
app.include_router(prediction_router)
app.include_router(earthquake_router)
app.include_router(nasa_router)
app.include_router(profile_router)
app.include_router(map_router)

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)


@app.get("/")
def home():

    return {
        "message": "Global Disaster Intelligence Platform API"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }