# Databricks notebook source
%pip install Faker

# COMMAND ----------
import pandas as pd
import random
from faker import Faker
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# 乱数シードの固定
Faker.seed(42)
random.seed(42)

fake = Faker('en_US')
num_records = 10000

departments = ['Engineering', 'Sales', 'HR', 'Marketing', 'Finance']
regions = ['Japan', 'US', 'EMEA', 'APAC']

def generate_mock_data(n):
    data = []
    for i in range(1, n + 1):
        data.append({
            "emp_id": f"EMP{i:05d}",
            "name": fake.name(),
            "department": random.choice(departments),
            "region": random.choice(regions),
            "salary": random.randint(40000, 150000),
            "ssn": fake.ssn()
        })
    return data

pdf = pd.DataFrame(generate_mock_data(num_records))

schema = StructType([
    StructField("emp_id", StringType(), False),
    StructField("name", StringType(), True),
    StructField("department", StringType(), True),
    StructField("region", StringType(), True),
    StructField("salary", IntegerType(), True),
    StructField("ssn", StringType(), True)
])

df = spark.createDataFrame(pdf, schema=schema)

# 保存先のVolumeパスを定義
# ※ <ボリューム名> の部分は事前に作成したVolume名（例: raw_data など）に書き換えてください
volume_path = "/Volumes/solo_practice/data/customer/hr_employees_initial"

# 単一のCSVファイルとしてVolumeに書き込み
df.coalesce(1).write \
  .format("csv") \
  .option("header", "true") \
  .mode("overwrite") \
  .save(volume_path)

print(f"CSVデータのエクスポートが完了しました: {volume_path}")