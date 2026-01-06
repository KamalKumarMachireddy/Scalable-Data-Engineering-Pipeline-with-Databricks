# Databricks notebook source
from pyspark.sql import functions as F

# COMMAND ----------

# start date and end date
start_date = "2024-01-01"
end_date   = "2025-12-01"

# COMMAND ----------

dataframe = (spark.sql(f"""
                       SELECT explode(
                           sequence(
                               date '{start_date}', 
                               date '{end_date}', 
                               interval 1 month)
                       ) AS month_start_date
                       """)
             )

# COMMAND ----------

df = (
    dataframe
    # Surrogate key at month grain
    .withColumn("date_key", F.date_format("month_start_date", "yyyyMM").cast("int"))
    .withColumn("year", F.year("month_start_date"))
    .withColumn("month_name", F.date_format("month_start_date", "MMMM"))
    .withColumn("month_short_name", F.date_format("month_start_date", "MMM"))
    .withColumn("quarter", F.concat(F.lit("Q"), F.quarter("month_start_date")))
    .withColumn("year_quarter", F.concat(F.col("year"), F.lit("-Q"), F.quarter("month_start_date")))
)


# COMMAND ----------

display(df)

# COMMAND ----------

df.write \
    .mode("overwrite") \
    .format("delta") \
    .saveAsTable("fmcg.gold.dim_date")