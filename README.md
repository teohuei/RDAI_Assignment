# About Project #

This is a language translation project that uses AI models to do language detection and translation.

This project contains a web application built using gradio and a backend service serving out APIs using FastAPI to support the functions on the web application.

## Web Application ##

The codes are in the frontend directory of this project.

It is using a tabbed interface design to handle two key functions that were implemented in the project.

First function is the language detection of a given text. (Refer to sample screenshot: Detect_Sample.png)
Second function is to translate the text to English. (Refer to sample screenshot: Translate_Sample.png)

This demo web application can be started by running "python app.py" in the folder where app.py reside and access the application at http://127.0.0.1:7860.

## Backend Service ##

The codes are in the backend directory of this project.

It serves 4 different APIs.

1) Status endpoint: Check if the service is running.
2) Detect endpoint: Allow a post method to detect the language of a given text. It is using a fine-tuned version of xlm-roberta-base on the common language dataset.
3) Supported Languages endpoint: It returns a list of languages that can be translated by the service. (Note: The list of support languages can be edited in the env file before building the docker image.)
4) Translate endpoint: It will translate the given text and selected original language to English text. It is using facebook/m2m100_418M model that is train for many-to-many multilingual translation.

The docker image of backend service can be built by running "docker build -t translation-svc ."
After building, it can be started up by running "docker run -p 8000:8000 translation-svc"

The OpenAPI specification can be accessible at http://localhost:8000/docs.