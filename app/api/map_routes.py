from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter()


@router.get("/map")
def disaster_map():
    return FileResponse("app/static/map.html")