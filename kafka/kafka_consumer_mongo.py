from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, ArrayType
import json

# Define the schema for the message data
schema = StructType([
    StructField("field1", StringType(), True),
    StructField("field2", IntegerType(), True),
    StructField("field3", ArrayType(StringType()), True)
])

# Create a SparkSession
spark = SparkSession.builder \
    .appName("KafkaToMongoDB") \
    .config("spark.mongodb.output.uri", "mongodb://localhost/mydb.my_collection") \
    .getOrCreate()

# Create a streaming DataFrame from Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "my_topic") \
    .option("startingOffsets", "earliest") \
    .load()

# Parse the message data
parsed_df = df.select(from_json(df.value.cast("string"), schema).alias("message_data")) \
    .selectExpr("message_data.*")

# Write the data to MongoDB
query = parsed_df.writeStream \
    .outputMode("append") \
    .foreachBatch(lambda batch_df, batch_id: batch_df.write.format("mongo").mode("append").save())

# Start the query
query.start().awaitTermination()
