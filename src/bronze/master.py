# Databricks notebook source

from bronze import csv_to_bronze

table_dict = {
    "bronze_orders": "/Volumes/hands_on/e_commerce/olist/olist_orders_dataset.csv",
    "bronze_order_items": "/Volumes/hands_on/e_commerce/olist/olist_order_items_dataset.csv",
    "bronze_products": "/Volumes/hands_on/e_commerce/olist/olist_products_dataset.csv",
    "bronze_customers": "/Volumes/hands_on/e_commerce/olist/olist_customers_dataset.csv"
}

for table_name, file_path in table_dict.items():
    csv_to_bronze(spark, table_name, file_path)