# databricks_demo.py

# This script lists files in the Databricks datasets directory and prints their sizes.
# Added: basic error handling, user input parameter for a subdirectory

dbutils.widgets.text("subdir", "", "Subdirectory within /databricks-datasets")
subdir = dbutils.widgets.get("subdir")

path = f"/databricks-datasets/{subdir}" if subdir else "/databricks-datasets"

try:
    files = dbutils.fs.ls(path)
    print(f"Files under {path}:")
    for f in files:
        print(f"{f.name} - size: {f.size}")
except Exception as e:
    print(f"Error listing files in {path}: {str(e)}")

# TODO: add filtering by file type (e.g., only .csv files)
