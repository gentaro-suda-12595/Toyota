# Databricks notebook source

from pyspark.sql.functions import col, to_timestamp, date_format
from write_silver import write_silver

df_orders = spark.read.table("hands_on.bronze.bronze_orders")

df_silver_orders = df_orders \
  .withColumn("order_purchase_timestamp", to_timestamp(col("order_purchase_timestamp"))) \
  .withColumn("order_date", date_format(col("order_purchase_timestamp"), "yyyy-MM-dd")) \
  .withColumn("order_ym", date_format(col("order_purchase_timestamp"), "yyyy-MM")) \
  .filter(~col("order_status").isin("canceled", "unavailable"))

write_silver(spark, df_silver_orders, "silver_orders")



  
