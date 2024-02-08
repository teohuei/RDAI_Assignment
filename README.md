# About Project #

This is a language translation project that uses AI models to do language detection and translation.

This project contains a web application built using gradio and a backend service serving out APIs using FastAPI to support the functions on the web application.

## Web Application ##

The codes are in the frontend directory of this project.

It is using a tabbed interface design to handle two key functions that were implemented in the project.

First function is the language detection of a given text. (Refer to sample screenshot: Detect_Sample.png)
![Detect_Sample.png](https://github.com/teohuei/RDAI_Assignment/blob/main/Detect_Sample.png?raw=true)
Second function is to translate the text to English. (Refer to sample screenshot: Translate_Sample.png)
![Translate_Sample.png](https://github.com/teohuei/RDAI_Assignment/blob/main/Translate_Sample.PNG?raw=true)

The docker image of gradio application can be built by running "docker build -t translation-app ." in frontend folder directory where the Dockerfile reside.

## Backend Service ##

The codes are in the backend directory of this project.

It serves 4 different APIs.

1) Status endpoint: Check if the service is running.
2) Detect endpoint: Allow a post method to detect the language of a given text. It is using a fine-tuned version of xlm-roberta-base on the common language dataset.
3) Supported Languages endpoint: It returns a list of languages that can be translated by the service.
4) Translate endpoint: It will translate the given text and selected original language to English text. It is using facebook/m2m100_418M model that is train for many-to-many multilingual translation.

The docker image of backend service can be built by running "docker build -t translation-svc ." in backend folder directory where the Dockerfile reside.

## Starting the application and service ##

Both application and backend service can be started by running "docker-compose up -d" in the root folder where docker-compose.yml and .env file reside.
(Note: The list of support languages can be edited in the env file before starting the service. Ensure that the languages are supported by both the AI models.)

Please be patient, and wait for the models to be loaded into the backend (approx. 5 to 10mins)

The gradio application is accessible at http://localhost:7860.
<br>The OpenAPI specification of the service is accessible at http://localhost:8000/docs.