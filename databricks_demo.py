# sample databricks utilities code
dbutils.widgets.text("param", "default", "A test parameter")
param_value = dbutils.widgets.get("param")
print(f"Received parameter: {param_value}")

# list files in a Databricks directory
files = dbutils.fs.ls("/databricks-datasets")
for f in files:
    print(f.name)

# INSECURE HARDCODED SECRET for testing policy
my_db_password = "password123"
print(f"Hardcoded password: {my_db_password}")
