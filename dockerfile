FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt .

RUN apk add --no-cache pip

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]
