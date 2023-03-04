from pyspark.sql import types as t

# #==============================INFO_MAIN=========================#
INFO_MAIN_schema = StructType([ \
    StructField("disc_name",StringType(),True), \
    StructField("now",TimestampType(),True), \
    StructField("disc_total",IntegerType(),True), \
    StructField("disc_used", IntegerType(), True), \
    StructField("disc_free", IntegerType(), True), \
    StructField("disc_type", StringType(), True)
  ])

#==============================INFO_DIR=========================#
INFO_DIR_schema = StructType([ \
    StructField("computer_name",StringType(),True), \
    StructField("folder_name",StringType(),True), \
    StructField("folder_size",IntegerType(),True), \
    StructField("fnm_with_last_change", StringType(), True), \
    StructField("chk_from_date", TimestampType(), True), \
    StructField("now_run", TimestampType(), True)
  ])

#==============================DIR=========================#
INFO_DIR_schema = StructType([ \
    StructField("dirpath",StringType(),True), \
    StructField("filename",StringType(),True), \
    StructField("size",IntegerType(),True), \
    StructField("date_modified", TimestampType(), True), \
    StructField("date_created", TimestampType(), True)
  ])
