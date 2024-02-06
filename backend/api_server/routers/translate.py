# routers/translate.py

from fastapi import APIRouter, status, Request
from models.models import TranslateInput, TranslateOutput
from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer
from dotenv import load_dotenv
import json
import os

router = APIRouter()

load_dotenv()
LANG_CODE_LIST = json.loads(os.getenv('SUPPORTED_LANG_CODE_LIST'))
LANG_NAME_LIST = json.loads(os.getenv('SUPPORTED_LANG_NAME_LIST'))
SUPPORTED_LANG_DICT = dict(zip(LANG_NAME_LIST, LANG_CODE_LIST))

translateModel = M2M100ForConditionalGeneration.from_pretrained("facebook/m2m100_418M")
translateTokenizer = M2M100Tokenizer.from_pretrained("facebook/m2m100_418M")

@router.post(
    "/translate", 
    tags=["translate"],
    summary="Translate the input message to English",
    status_code=status.HTTP_200_OK,
    response_model=TranslateOutput,
)
def translate(request: Request, input_data: TranslateInput):
    # Get the prompt from the input data
    prompt = input_data.prompt
    ori_lang = SUPPORTED_LANG_DICT[input_data.originalLang]

    # Translate Detected Language to English
    translateTokenizer.src_lang = ori_lang
    encoded = translateTokenizer(prompt, return_tensors="pt")
    generated_tokens = translateModel.generate(**encoded, forced_bos_token_id=translateTokenizer.get_lang_id("en"))
    result = translateTokenizer.batch_decode(generated_tokens, skip_special_tokens=True)

    # Generate a response from the loaded translation model using the prompt
    response = result[0]

    # Return the response as output data
    return TranslateOutput(response=response)
