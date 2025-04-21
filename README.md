# PySpark + Elasticsearch + Kibana Dockerized Project

This project demonstrates how to integrate **PySpark** with **Elasticsearch** and **Kibana** using **Docker Compose**. It provides a simple example of writing data from PySpark to Elasticsearch and reading it back for further processing.

## 📦 Project Structure

```
.
├── docker-compose.yml
├── spark
│   ├── Dockerfile
│   └── app
│       └── es_example.py
```

## 🚀 Services

- **Elasticsearch** – Stores and indexes structured data.
- **Kibana** – Visualizes data from Elasticsearch.
- **Spark** – PySpark environment for processing and interacting with Elasticsearch.

## 🐳 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/pyspark-elasticsearch-kibana.git
cd pyspark-elasticsearch-kibana
```

### 2. Start the Containers

```bash
docker-compose up --build
```

- Elasticsearch will be available at [http://localhost:9200](http://localhost:9200)
- Kibana will be available at [http://localhost:5601](http://localhost:5601)

### 3. Run the PySpark Script

Once the containers are up and running, attach to the Spark container:

```bash
docker exec -it spark bash
```

Inside the container, run the example script:

```bash
spark-submit es_example.py
```

This script:
- Creates a small sample DataFrame
- Writes it to an Elasticsearch index called `books`
- Reads it back from Elasticsearch and shows the results

## 🛠 Dependencies

The Spark container installs the following:
- Python 3 & pip
- PySpark
- `elasticsearch`, `pandas` (via pip)
- Elasticsearch Spark Connector `elasticsearch-spark-30_2.12-8.12.2.jar`

## 📈 Visualization

You can use Kibana to explore the `books` index after the script is run:

1. Go to **Kibana → Management → Stack Management → Index Patterns**
2. Create a new index pattern (e.g., `books*`)
3. Explore the data using **Discover**

## ✅ Notes

- The Elasticsearch and Kibana versions are compatible with the connector used (8.12.x).
- Security features (e.g., TLS, authentication) are disabled for simplicity in the development setup.

## 📚 Resources

- [Elasticsearch Python Client](https://elasticsearch-py.readthedocs.io/)
- [Elasticsearch Spark Connector Docs](https://www.elastic.co/guide/en/elasticsearch/hadoop/current/spark.html)
- [Kibana Guide](https://www.elastic.co/guide/en/kibana/current/index.html)
