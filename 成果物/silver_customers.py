from pyspark.sql import functions as F
df_bronze_customers = spark.read.table("hands_on.bronze.bronze_customers")

df_silver_customers = df_bronze_customers\
    .withColumn("customer_state",F.upper(F.col("customer_state")))\
    .withColumn("customer_city",F.upper(F.col("customer_city")))


df_silver_customers.write\
    .format("delta")\
    .mode("overwrite")\
    .saveAsTable("hands_on.silver.silver_customers")