from pyspark.sql.functions import col, to_timestamp, date_format

# 1. Bronzeテーブルの読み込み
df_orders = spark.read.table("hands_on.bronze.bronze_orders")

# 2. Silver層への変換・加工
df_silver_orders = df_orders \
  .withColumn("order_purchase_timestamp", to_timestamp(col("order_purchase_timestamp"))) \
  .withColumn("order_date", date_format(col("order_purchase_timestamp"), "yyyy-MM-dd")) \
  .withColumn("order_ym", date_format(col("order_purchase_timestamp"), "yyyy-MM")) \
  .filter(~col("order_status").isin("canceled", "unavailable"))

# 3. 確認表示
df_silver_orders.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("hands_on.silver.silver_orders")


  
