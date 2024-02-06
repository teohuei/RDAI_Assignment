# main.py

from api_server import app
from dotenv import load_dotenv
import uvicorn
import sys, os

if __name__ == "__main__":
    if sys.version_info[0:2] != (3, 9):
        raise Exception('Requires python 3.9')
    load_dotenv()
    HOSTNAME = os.getenv('HOSTNAME')
    uvicorn.run("api_server:app", host=HOSTNAME)
