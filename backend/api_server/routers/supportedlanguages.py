# routers/supportedlanguages.py

from fastapi import APIRouter, status
from models.models import SupportedLang

router = APIRouter()

@router.get(
    "/supportedlanguages", 
    tags=["supportedlanguages"],
    summary="Get Supported Languages List",
    status_code=status.HTTP_200_OK,
    response_model=SupportedLang,
)
def get_supported_languages() -> SupportedLang:
    return SupportedLang()
