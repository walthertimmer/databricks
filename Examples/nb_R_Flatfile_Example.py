# Databricks notebook source
# MAGIC %md
# MAGIC #### R Flatfiles
# MAGIC This notebook demo's the usecase of loading a flatfile in R.

# COMMAND ----------

# MAGIC %md
# MAGIC Create a volume to dump some example files

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE VOLUME IF NOT EXISTS test.test

# COMMAND ----------

# MAGIC %md
# MAGIC CSV

# COMMAND ----------


