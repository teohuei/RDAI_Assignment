# routers/status.py

from fastapi import APIRouter, status
from models.models import StatusCheck

router = APIRouter()

@router.get(
    "/status",
    tags=["statuscheck"],
    summary="Perform a Status Check",
    status_code=status.HTTP_200_OK,
    response_model=StatusCheck,
)
def get_status() -> StatusCheck:
    return StatusCheck(status="OK")
