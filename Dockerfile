FROM python:3.9

RUN pip install --upgrade pip

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

# CMD ["fastapi", "run", "--proxy-headers","--port", "80", "app/main.py"]
ENTRYPOINT ["uvicorn"]
CMD ["app.main:app", "--reload", "--host", "0.0.0.0", "--port", "80"]
