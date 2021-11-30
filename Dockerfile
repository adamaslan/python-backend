FROM python:3.8.3-slim
RUN apt-get update
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache -r requirements.txt
EXPOSE 5000
COPY . .
COPY .env.docker .env
CMD ["flask", "run"]