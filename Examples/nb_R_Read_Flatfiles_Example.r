# Databricks notebook source
# MAGIC %md
# MAGIC ### Read flatfiles with R

# COMMAND ----------

# MAGIC %md
# MAGIC #### CSV

# COMMAND ----------


# Define the file path of the CSV file within the Databricks volume
csv_file_path <- "/Volumes/uc_concurrentie/test/test_files/r_dummy_file.csv" 

# Read the CSV file into a data frame
data <- read.csv(csv_file_path)

# Display the first few rows of the data frame
head(data)

# COMMAND ----------

# MAGIC %md
# MAGIC #### JSON

# COMMAND ----------


# Define the file path of the JSON file within the Databricks volume
json_file_path <- "/Volumes/uc_concurrentie/test/test_files/r_dummy_file.json" 

# Read the JSON file into a data frame
data <- jsonlite::fromJSON(json_file_path)

# Display the first few rows of the data frame
head(data)

# COMMAND ----------

# MAGIC %md
# MAGIC ####TXT

# COMMAND ----------

# Define the file path of the text file within the Databricks volume
txt_file_path <- "/Volumes/uc_concurrentie/test/test_files/r_dummy.txt"

# Read the text file into a data frame
data <- read.delim(txt_file_path)

# Display the first few rows of the data frame
head(data)

# COMMAND ----------

# MAGIC %md
# MAGIC
