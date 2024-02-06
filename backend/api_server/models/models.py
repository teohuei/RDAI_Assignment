# models/models.py

from pydantic import BaseModel, field_validator
from typing import Optional
from dotenv import load_dotenv
import json
import os

load_dotenv()
LANG_CODE_LIST = json.loads(os.getenv('SUPPORTED_LANG_CODE_LIST'))
LANG_NAME_LIST = json.loads(os.getenv('SUPPORTED_LANG_NAME_LIST'))
SUPPORTED_LANG_DICT = dict(zip(LANG_NAME_LIST, LANG_CODE_LIST))

class StatusCheck(BaseModel):
    """Response model to validate and return when performing a status check."""
    status: str = "OK"

class SupportedLang(BaseModel):
    """Response model to validate and return supported languages list."""
    supported_lang: Optional[list] = LANG_NAME_LIST

class DetectInput(BaseModel):
    """Request model to validate the input to be a string."""
    prompt: str

class DetectOutput(BaseModel):
    """Response model to validate and return detect language and the model's confidence level."""
    response: str
    confidence: str

class TranslateInput(BaseModel):
    """Request model to validate the inputs to be a string."""
    prompt: str
    originalLang: str

    @field_validator('originalLang')
    def validate_originalLang(cls, v):
        if v not in LANG_NAME_LIST:
            raise ValueError(f"{v} is not a valid value for originalLang")
        return v

class TranslateOutput(BaseModel):
    """Response model to validate and return translated English text."""
    response: str
