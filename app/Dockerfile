FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install flask

RUN mkdir /data

EXPOSE 5000

CMD ["python", "app.py"]
