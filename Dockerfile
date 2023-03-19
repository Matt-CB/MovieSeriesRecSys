FROM tiangolo/uvicorn-gunicorn-fastapi

COPY ./app .

RUN pip install pandas
