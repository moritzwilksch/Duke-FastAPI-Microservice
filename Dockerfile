# install python in the container
FROM python:3.8.8-slim
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
EXPOSE 8080
COPY ./ /app
WORKDIR /app
CMD uvicorn app:app --app-dir src --host 0.0.0.0 --port 8080