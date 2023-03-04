import re
import utils_fs as ut
import src as c
from os import walk
import schema_ut as sc

from pyspark.sql import SparkSession
import pyspark.sql.functions as f
from pyspark.sql import types as t
from pyspark.sql.functions import *

from kafka import KafkaProducer
from kafka import KafkaProducer



def get_all_files(source_file):
    json_files = source_file
    filenames = next(walk(source_file), (None, None, []))[2]
    return filenames


def send_file_topic(source_file, topic_dest):
    with open(source_file, 'r') as f:
        while True:
            lines = f.readlines()  # returns list of strings
            if not lines:
                time.sleep(1)
                f.seek(f.tell())
            else:
                producer.send(topic=topic_dest, value=json.dumps(lines).encode('utf-8'))
                producer.flush()
                sleep(3)

def ReadStream(brokers, topic):
    socketDF = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", brokers) \
        .option("Subscribe", topic)\
        .load()\
        .selectEx pr("CAST(key AS STRING)","CAST(value AS STRING)")

def process_message(rdd, schema, host, collection_name):
    message_data = rdd.map(lambda x: x[1])
    message_data = message_data.map(lambda x: json.loads(x))

    df = spark.createDataFrame(message_data, schema=INFO_DIR_schema)
    df.write.format("com.mongodb.spark.sql.DefaultSource")
    .mode("append")
    .option("uri","mongodb://localhost:27017")
    .option("database","treesize_db")
    .option("collection","Svetlana_k_dir")
    .save()