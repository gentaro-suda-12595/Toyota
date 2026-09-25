from pyspark.sql import functions as F

df = spark.read.table("solo_practice.bronze.bronze_employee")

silver_df = df.withColumn("salary", F.col("salary").cast("int"))

silver_df.write\
    .format("delta")\
    .mode("append")\
    .option("delta.enableChangeDataFeed", "true")\
    .option("margeSchema", "true")\
    .saveAsTable("solo_practice.silver.silver_employee")
