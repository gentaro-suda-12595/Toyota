def write_gold(spark, gold_df, table_name):
    gold_df.write\
        .format("delta")\
        .mode("overwrite")\
        .saveAsTable(f"hands_on.gold.{table_name}")