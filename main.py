import utils_fs as ut
import src as c
import re
from os import walk
import schema_ut as sc

from pyspark.sql import SparkSession
import pyspark.sql.functions as f
from pyspark.sql import types as t
from pyspark.sql.functions import *

from kafka import KafkaProducer
from kafka import from kafka import KafkaProducer

######### get all
#
# json files from folder #########

json_files = ut.get_all_files(c.source_file)

list_file_info = []
info_file_dir = []
list_file_dir = []

for file_name in json_files:
    if re.search(ut.filter_info, file_name):
        list_file_info.append(file_name)
    elif re.search(ut.filter_info_dir, file_name):
        info_file_dir.append(file_name)
    elif re.search(ut.filter_dir, file_name):
        list_file_dir.append(file_name)

######### create a Kafka instance for producer #########

producer = KafkaProducer(
    bootstrap_servers=src.brokers,
    client_id='producer',
    acks=1,
    compression_type=None,
    retries=3)

ut.send_file_topic(list_file_info)
ut.send_file_topic(info_file_dir)
ut.send_file_topic(list_file_dir)


spark = SparkSession.builder.appName("tz_app") .getOrCreate()

stream.foreachRDD(process_message)

ssc.start()
ssc.awaitTermination()






