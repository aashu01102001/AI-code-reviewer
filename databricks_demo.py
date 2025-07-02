# databricks_demo.py

# added test change for PR 3
dbutils.widgets.text("param", "default", "Parameter for code review testing")
param_value = dbutils.widgets.get("param")
print(f"Received parameter: {param_value}")

# list files in a Databricks directory with policy check
files = dbutils.fs.ls("/databricks-datasets")
for f in files:
    if "policy" in f.name.lower():
        print(f"Policy file detected: {f.name}")
    else:
        print(f.name)
