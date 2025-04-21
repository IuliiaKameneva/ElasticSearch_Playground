from pyspark.sql import SparkSession

es_host = "http://elasticsearch:9200"

spark = SparkSession.builder \
    .appName("PySpark-ES-Test") \
    .config("spark.es.nodes", "elasticsearch") \
    .config("spark.es.port", "9200") \
    .config("spark.es.nodes.wan.only", "true") \
    .getOrCreate()

# Пример данных
data = [
    {"id": 1, "title": "Elasticsearch with PySpark"},
    {"id": 2, "title": "Streaming data to ES"}
]
df = spark.createDataFrame(data)

# Запись в ES
df.write \
  .format("es") \
  .option("es.resource", "books") \
  .option("es.nodes", "elasticsearch") \
  .option("es.port", "9200") \
  .mode("overwrite") \
  .save()

# Чтение из ES
es_df = spark.read \
    .format("org.elasticsearch.spark.sql") \
    .option("es.resource", "books") \
    .load()

es_df.show()
