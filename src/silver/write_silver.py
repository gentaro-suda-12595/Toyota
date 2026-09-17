# Databricks notebook source

def write_silver(spark, silver_df, table_name):
    silver_df.write\
    .format("delta")\
    .mode("overwrite")\
    .saveAsTable(f"hands_on.silver.{table_name}")
