FROM python:3.8-slim

RUN apt-get update && apt-get install -y curl

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "-m", "solver.app"]