# Databricks notebook source
# MAGIC %sql
# MAGIC
# MAGIC create catalog if not exists fmcg;
# MAGIC use catalog fmcg;

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC CREATE SCHEMA IF NOT EXISTS fmcg.gold;
# MAGIC CREATE SCHEMA IF NOT EXISTS fmcg.silver;
# MAGIC CREATE SCHEMA IF NOT EXISTS fmcg.bronze;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT count(*) FROM fmcg.gold.fact_orders;