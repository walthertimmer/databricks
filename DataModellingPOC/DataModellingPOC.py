# Databricks notebook source
# MAGIC %md
# MAGIC ## Data Modelling POC.
# MAGIC
# MAGIC How do seperate data modelling tools look at tables and relations inside Databricks?
# MAGIC
# MAGIC https://medium.com/@kamaljp/untangling-databases-data-modeling-with-dbeaver-b2e53ca06ca9
# MAGIC
# MAGIC Due note:
# MAGIC Table constraints are only supported in Unity Catalog

# COMMAND ----------

catalog_name = "uc_sandbox"
schema_name = "data_modelling_poc"

# COMMAND ----------

display(spark.sql(f"CREATE SCHEMA IF NOT EXISTS {catalog_name}.{schema_name};"))

# COMMAND ----------

# Create the country table with dummy records
spark.sql(f"""
CREATE TABLE IF NOT EXISTS {catalog_name}.{schema_name}.country (
    country_key INT PRIMARY KEY,
    name STRING,
    region STRING
) USING DELTA;
""")

# Insert dummy records into the country table
spark.sql(f"""
INSERT INTO {catalog_name}.{schema_name}.country VALUES
(1, 'United States', 'North America'),
(2, 'Canada', 'North America'),
(3, 'Brazil', 'South America'),
(4, 'United Kingdom', 'Europe'),
(5, 'Germany', 'Europe'),
(6, 'China', 'Asia'),
(7, 'India', 'Asia'),
(8, 'Australia', 'Oceania'),
(9, 'South Africa', 'Africa'),
(10, 'Egypt', 'Africa');
""")

# Display the newly inserted records
display(spark.sql(f"SELECT * FROM {catalog_name}.{schema_name}.country"))

# COMMAND ----------

spark.sql(f"""
CREATE TABLE IF NOT EXISTS {catalog_name}.{schema_name}.economy (
    economy_key INT PRIMARY KEY,
    country_key INT,
    gdp DECIMAL(10,2),
    FOREIGN KEY (country_key) REFERENCES {catalog_name}.{schema_name}.country(country_key)
) USING DELTA;
""")
