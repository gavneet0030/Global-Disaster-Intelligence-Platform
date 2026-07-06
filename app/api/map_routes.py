from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter(
    tags=["Map"]
)


@router.get("/map")
def disaster_map():

    return FileResponse(
        "app/static/map.html"
    )