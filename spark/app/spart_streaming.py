from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, IntegerType, StringType
from elasticsearch import Elasticsearch

# Инициализация Spark
spark = SparkSession.builder \
    .appName("KafkaToElasticsearch") \
    .master("spark://spark-master:7077") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# Схема для JSON
schema = StructType() \
    .add("id", IntegerType()) \
    .add("text", StringType())

# Чтение данных из Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "test-topic") \
    .load()

# Парсинг JSON
parsed_df = df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

# Отправка в Elasticsearch
def write_to_es(batch_df, batch_id):
    if not batch_df.rdd.isEmpty():
        docs = batch_df.toPandas().to_dict(orient="records")
        es = Elasticsearch("http://elasticsearch:9200")
        for doc in docs:
            es.index(index="messages", document=doc)

# Запуск стриминга
query = parsed_df.writeStream \
    .foreachBatch(write_to_es) \
    .outputMode("update") \
    .start()

query.awaitTermination()
