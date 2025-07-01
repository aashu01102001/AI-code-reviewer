# sample databricks utilities code
dbutils.widgets.text("param", "default", "A test parameter")
param_value = dbutils.widgets.get("param")
print(f"Received parameter: {param_value}")

# list files in a Databricks directory
files = dbutils.fs.ls("/databricks-datasets")
for f in files:
    print(f.name)

# new test line for code review
print("This is a second test change for code review automation.")
