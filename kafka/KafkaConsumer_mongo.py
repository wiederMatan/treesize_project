from kafka import KafkaConsumer
from pymongo import MongoClient
import json


# ------------config KafkaConsumer-------------
usage_tracker = 'kafka-tst-03'
brokers = ['cnt7-naya-cdh63:9092']


# -------------config MongoDB-------------
client = MongoClient('mongodb://localhost:27017/')
db = client['treesize_db']
collection = db['Svetlana_k_dir']

# -------------create kafka session-------------
consumer = KafkaConsumer(usage_tracker,
                         bootstrap_servers=brokers,
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))

# -------------Send data from Kafka to MongoDB-------------
for message in consumer:
    message_data = message.value[0]
    message_data = json.loads(message_data)

    if isinstance(message_data, list):
        collection.insert_many(message_data)
    else:
        collection.insert_one(message_data)
    print(message_data)







