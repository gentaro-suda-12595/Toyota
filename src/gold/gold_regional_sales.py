from pyspark.sql import functions as F
from write_gold import write_gold
df_silver_orders = spark.read.table("hands_on.silver.silver_orders")
df_silver_customers = spark.read.table("hands_on.silver.silver_customers")
df_silver_items = spark.read.table("hands_on.silver.silver_order_items")

df_orders_customers = df_silver_orders\
.join(df_silver_customers, "customer_id", how="inner")\
.join(df_silver_items, "order_id", how="inner")

df_regional_sales = df_orders_customers\
.groupBy("customer_state")\
.agg(F.sum("total_amount").alias("total_sales"),
F.countDistinct("customer_unique_id").alias("total_customers"),
(F.sum("total_amount") / F.countDistinct("customer_unique_id")).alias("customer_avg_sales")     
     )

write_gold(spark,df_regional_sales,"gold_regional_sales")

