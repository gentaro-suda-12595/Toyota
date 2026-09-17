from pyspark.sql import functions as F
from write_silver import write_silver

df_bronze_customers = spark.read.table("hands_on.bronze.bronze_customers")

df_silver_customers = df_bronze_customers\
    .withColumn("customer_state",F.upper(F.col("customer_state")))\
    .withColumn("customer_city",F.upper(F.col("customer_city")))

write_silver(spark ,df_silver_customers, "silver_customers")