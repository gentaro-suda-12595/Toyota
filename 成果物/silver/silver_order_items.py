from pyspark.sql import functions as F
from write_silver import write_silver


df = spark.read.table("hands_on.bronze.bronze_order_items")

silver_df = df.withColumn("total_amount", F.col("price") + F.col("freight_value"))

write_silver(spark, silver_df, "silver_order_items")