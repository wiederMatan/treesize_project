from kafka import KafkaProducer
from time import sleep
import json


# -----------------------Topics/Brokers-----------------------
usage_tracker = 'kafka-tst-03'
brokers = ['cnt7-naya-cdh63:9092']
source_file = r"/home/naya/json_files_ts/"

# ----------loop json files
from os import walk
filenames = next(walk(source_file), (None, None, []))[2]
print(filenames)





# source_file = r"/home/naya/json_files_ts/Svetlana_k_2023_02_12_211714___dir_1.txt"

# producer = KafkaProducer(
#     bootstrap_servers=brokers,
#     client_id='producer',
#     acks=1,
#     compression_type=None,
#     retries=3)
#
# with open(source_file, 'r') as f:
#     while True:
#         lines = f.readlines()  # returns list of strings
#         if not lines:
#             sleep(1)
#             f.seek(f.tell())
#         else:
#             # print(lines)
#             producer.send(topic=usage_tracker, value=json.dumps(lines).encode('utf-8'))
#             producer.flush()
#             sleep(3)

