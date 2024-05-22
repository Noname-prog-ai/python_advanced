FROM python:3.7.9-slim-stretch

RUN mkdir /app.py

COPY requirements.txt /app/

RUN python -m pip install -r /app.py/requirements.txt

COPY app.py /app/

WORKDIR /app

ENTRYPOINT ["python", "app.py"]