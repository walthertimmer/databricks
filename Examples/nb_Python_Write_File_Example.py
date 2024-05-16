# Databricks notebook source
# MAGIC %md
# MAGIC 'Write with pandas only works for workspace... not filestorage... 

# COMMAND ----------

dbutils.fs.ls('./mnt/import/headspace')

# COMMAND ----------

df = spark.sql("SELECT 1")

# COMMAND ----------

df.write.mode("overwrite").csv(path= 'dbfs:/mnt/import/headspace/test.csv')

# COMMAND ----------

df_pandas = df.toPandas()

# COMMAND ----------

csv_data = df_pandas.to_csv()

# COMMAND ----------

# MAGIC %sh pwd

# COMMAND ----------

dbutils.fs.ls('/Workspace/')

# COMMAND ----------

# MAGIC %pip install fsspec

# COMMAND ----------

# df_pandas.to_csv(/../test_pandas3.csv')
df_pandas.to_csv('/Workspace/Repos/timmer.w@menzis.nl/databricks/test_pandas4.csv')


# COMMAND ----------

dbutils.fs.put('dbfs:/mnt/import/headspace/test_pandas.csv', csv_data, overwrite=True)
