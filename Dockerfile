FROM mirror.gcr.io/python:3.13

WORKDIR /app

COPY backend/requirements.txt /app/requirements.txt
RUN pip install wheel
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["fastapi", "dev", "backend/main.py"]