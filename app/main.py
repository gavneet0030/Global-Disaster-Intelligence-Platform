from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.routes import router
from app.api.map_routes import router as map_router

from app.database.database import Base, engine

import app.models.user
import app.models.disaster

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Global Disaster Intelligence Platform",
    version="2.0.0"
)

app.include_router(router)
app.include_router(map_router)

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)