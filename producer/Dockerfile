FROM python:3.10-slim

WORKDIR /app

USER root

RUN pip install kafka-python

# COPY kafka-producer.py .

# COPY /app/kafka_producer.py /kafka_producer.py

CMD ["python", "kafka-producer.py"]
