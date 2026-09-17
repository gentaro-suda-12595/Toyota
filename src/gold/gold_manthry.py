from pyspark.sql import functions as F
from write_gold import write_gold

orders_df = spark.read.table("hands_on.silver.silver_orders")
items_df = spark.read.table("hands_on.silver.silver_order_items")
products_df = spark.read.table("hands_on.silver.silver_products")


inner_df = orders_df.join(items_df, on="order_id", how="inner")
left_df = inner_df.join(products_df, on="product_id", how="left")

gold_df = left_df.groupBy("order_ym","product_category_name")\
    .agg(F.sum("price").alias("revenue"),
         F.count("order_item_id").alias("order_item_count"),
         F.countDistinct("order_id").alias("unique_order_count")
    )\
    .orderBy("order_ym", "product_category_name")
    
write_gold(spark, gold_df, "gold_monthly_category_sales")
    
