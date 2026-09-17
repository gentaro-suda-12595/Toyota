from pyspark.sql import functions as F


df = spark.read.table("hands_on.bronze.bronze_order_items")

silver_df = df.withColumn("total_amount", F.col("price") + F.col("freight_value"))

silver_df.write\
    .format("delta")\
    .mode("overwrite")\
    .saveAsTable("hands_on.silver.silver_order_items")