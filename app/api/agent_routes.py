from fastapi import APIRouter

from app.agents.coordinator import Coordinator


router = APIRouter(
    prefix="/agent",
    tags=["Agentic AI"]
)


@router.get("/run")
def run_agent():

    coordinator = Coordinator()

    return coordinator.execute()