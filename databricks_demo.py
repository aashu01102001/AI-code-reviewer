# sample databricks utilities code
dbutils.widgets.text("param", "default", "A test parameter")
param_value = dbutils.widgets.get("param")
print(f"Received parameter: {param_value}")

# list files in a Databricks directory
files = dbutils.fs.ls("/databricks-datasets")
for f in files:
    print(f.name)

# NEW CHANGE FOR TEST
print("✅ This is a new test line for PR review by the AI reviewer.")
