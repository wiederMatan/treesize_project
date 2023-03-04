# ======================================== Kafka Connections =============================================== #
brokers = "cnt7-naya-cdh63:9092"
topic_info = 'kafka-info'
topic_info_dir = 'kafka-info_d'
topic_dir = 'kafka-dir'

source_file = r"/home/naya/json_files_ts/Svetlana_k_2023_02_12_211714___dir_1.txt"
# ======================================== Kafka filters =============================================== #
filter_info = r"INFO_Main"
filter_info_dir = r"INFO_dir"
filter_dir = r"dir_"
# ================================= MongoDB Connections =============================================== #
MongoClient = 'mongodb://localhost:27017/'
db = 'treesize_db'
collection = ['Svetlana_k_info', 'Svetlana_k_info_dir', 'Svetlana_k_dir']



