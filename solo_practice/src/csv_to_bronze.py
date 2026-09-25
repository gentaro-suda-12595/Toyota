bronze_df = spark.read\
    .format("csv")\
    .option("header", "true")\
    .option("inferSchema", "true")\
    .load("/Volumes/solo_practice/data/customer/customer_data.csv")

bronze_df.write\
    .format("delta")\
    .mode("overwrite")\
    .saveAsTable("solo_practice.bronze.bronze_employee")