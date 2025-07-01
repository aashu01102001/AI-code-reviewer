# sample databricks utilities code
# added another test line
dbutils.widgets.text("param", "default", "A test parameter")
param_value = dbutils.widgets.get("param")
print(f"Received parameter: {param_value}")

# list files in a Databricks directory
files = dbutils.fs.ls("/databricks-datasets")
for f in files:
    print(f.name)

print("✅ Another test change for PR review")
