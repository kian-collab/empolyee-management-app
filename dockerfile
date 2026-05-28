FROM python:3.11

WORKDIR /app

COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

CMD ["sh", "-c", "sleep 25 && python app.py"]
