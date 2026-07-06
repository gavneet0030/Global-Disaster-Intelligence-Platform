from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.routes import router
from app.api.map_routes import router as map_router
from app.api.earthquake_routes import router as earthquake_router

from app.database.database import Base, engine

import app.models.user
import app.models.disaster
import app.models.earthquake

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Global Disaster Intelligence Platform",
    description="AI Powered Disaster Intelligence System",
    version="2.2.0"
)

app.include_router(router)

app.include_router(map_router)

app.include_router(earthquake_router)

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)