# FROM bitnami/spark:3.5.0

# USER root

# RUN apt-get update && apt-get install -y python3-pip curl iputils-ping

# RUN pip3 install --upgrade pip && pip3 install elasticsearch pandas

# # Загружаем Spark Elasticsearch Connector
# RUN mkdir -p /opt/bitnami/spark/jars && \
#     curl -L -o /opt/bitnami/spark/jars/elasticsearch-spark-30_2.12-8.12.2.jar https://repo1.maven.org/maven2/org/elasticsearch/elasticsearch-spark-30_2.12/8.12.2/elasticsearch-spark-30_2.12-8.12.2.jar

# FROM python:3.8-slim

# Установим необходимые библиотеки
# RUN pip install pyspark kafka-python requests elasticsearch

# Копируем твой Python скрипт в контейнер
# COPY es_example.py /app/es_example.py

# Устанавливаем рабочую директорию
# WORKDIR /app

# Запускаем Python скрипт
# CMD ["python", "es_example.py"]
# =================================================
# FROM bitnami/spark:3.5.0

# USER root

# RUN apt-get update && apt-get install -y python3-pip curl iputils-ping

# RUN pip3 install --upgrade pip && pip3 install elasticsearch pandas pyspark kafka-python requests 

# # Загружаем Spark Elasticsearch Connector
# RUN mkdir -p /opt/bitnami/spark/jars && \
#     curl -L -o /opt/bitnami/spark/jars/elasticsearch-spark-30_2.12-8.12.2.jar https://repo1.maven.org/maven2/org/elasticsearch/elasticsearch-spark-30_2.12/8.12.2/elasticsearch-spark-30_2.12-8.12.2.jar

# ================================================================

FROM python:3.10-slim

WORKDIR /app

RUN pip install pyspark kafka-python elasticsearch

COPY spark_streaming.py .

CMD ["python", "spark_streaming.py"]