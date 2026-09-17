# Databricks notebook source

def csv_to_bronze(spark, table_name, file_path):
    df = spark.read\
         .format("csv")\
         .option("header", "true")\
         .option("inferSchema", "true")\
         .load(file_path)
    
    df.write\
        .format("delta")\
        .mode("overwrite")\
        .saveAsTable(f"hands_on.bronze.{table_name}")
    


   