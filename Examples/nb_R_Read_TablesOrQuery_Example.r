# Databricks notebook source
# MAGIC %md
# MAGIC ####Read from table

# COMMAND ----------


# Install and load required packages
# install.packages("sparklyr")
library(sparklyr)

# Connect to Spark session
sc <- spark_connect(method = "databricks")

# Change the schema being used
tbl_change_db(sc, "uc_concurrentie.test")

name <- "city_price_data"

# Read the "trips" table into a Spark DataFrame
trips_df <- spark_read_table(sc, name = name)

# Preview the first few rows of the DataFrame
head(trips_df)

# COMMAND ----------

# MAGIC %md
# MAGIC ####Read with query

# COMMAND ----------


sc <- spark_connect(method = "databricks")

catalog <- "uc_concurrentie"
schema <- "test"
table_name <- "city_price_data"
query <- paste("SELECT * FROM ", catalog, ".", schema, ".", table_name)

collect(sdf_sql(sc, query))
