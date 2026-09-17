# Databricks notebook source

from pyspark.sql import functions as F
from write_silver import write_silver

df = spark.read.table("hands_on.bronze.bronze_products")

silver_df = df.drop(F.col("product_weight_g"), F.col("product_length_cm"), F.col("product_height_cm"), F.col("product_width_cm"))\
    .withColumn("product_category_name", F.when(F.col("product_category_name").isNull() | (F.col("product_category_name") == ""), "unknown").otherwise(F.col("product_category_name")))

write_silver(spark, silver_df, "silver_products")