from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database.database import (
    Base,
    engine
)

# ==========================
# Import Models
# ==========================

from app.models.user import User
from app.models.disaster import Disaster
from app.models.earthquake import Earthquake
from app.models.nasa_event import NASAEvent

# ==========================
# Routers
# ==========================

from app.api.user_routes import router as user_router
from app.api.auth_routes import router as auth_router
from app.api.nasa_routes import router as nasa_router
from app.api.earthquake_routes import router as earthquake_router
from app.api.agent_routes import router as agent_router

# ==========================
# Middleware
# ==========================

from app.middleware.logging_middleware import LoggingMiddleware

# ==========================
# Scheduler
# ==========================

from app.jobs.scheduler import start_scheduler


# ==========================
# Create Tables
# ==========================

Base.metadata.create_all(bind=engine)


# ==========================
# Lifespan
# ==========================

@asynccontextmanager
async def lifespan(app: FastAPI):

    print("=" * 60)
    print("Global Disaster Intelligence Platform Started")
    print("=" * 60)

    start_scheduler()

    yield

    print("=" * 60)
    print("Application Shutdown")
    print("=" * 60)


# ==========================
# FastAPI
# ==========================

app = FastAPI(

    title="Global Disaster Intelligence Platform",

    version="4.0.0",

    lifespan=lifespan

)


# ==========================
# Middleware
# ==========================

app.add_middleware(

    LoggingMiddleware

)


# ==========================
# Routers
# ==========================

app.include_router(user_router)

app.include_router(auth_router)

app.include_router(nasa_router)

app.include_router(earthquake_router)

app.include_router(agent_router)


# ==========================
# Root
# ==========================

@app.get("/")

def home():

    return {

        "message": "Global Disaster Intelligence Platform",

        "version": "4.0.0",

        "status": "Running"

    }


# ==========================
# Health Check
# ==========================

@app.get("/health")

def health():

    return {

        "status": "healthy",

        "database": "connected",

        "scheduler": "running"

    }