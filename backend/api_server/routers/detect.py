# routers/detect.py

from fastapi import APIRouter, status, Request
from models.models import DetectInput, DetectOutput
from transformers import pipeline

router = APIRouter()

detectModel = pipeline("text-classification", model="ivanlau/language-detection-fine-tuned-on-xlm-roberta-base")

@router.post(
    "/detect",
    tags=["detect"],
    summary="Detect the input message's language",
    status_code=status.HTTP_200_OK,
    response_model=DetectOutput,
)
def detect(request: Request, input_data: DetectInput):
    # Get the prompt from the input data
    prompt = input_data.prompt

    # Generate a response from the loaded detection model using the prompt
    result = detectModel(prompt)[0]
    response = result["label"]
    confidence = format(result["score"], ".0%")

    # Return the response as output data
    return DetectOutput(response=response, confidence=confidence)
