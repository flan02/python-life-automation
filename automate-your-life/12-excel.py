# Let's automate Excel with Python! -> Read excel, Filter fields, save excel
# We'll use two libraries: 1. pandas: for data manipulation | 2. openpyxl: for styling and formatting, adding formulas, create graphs
import pandas as pd
import openpyxl

# Read the Excel file
df = pd.read_excel("./files/PRODUCTOS.xlsx")  # virtual table (in memory)

# Filter the DataFrame to only include products with a price greater than > 300
df_filtered = df[df["PRECIO"] >= 300]

# Sort articles
df_sorted = df_filtered.sort_values(by="PRECIO", ascending=True)

# Save the filtered and sorted DataFrame to a new Excel file
file_output = "./files/PRODUCTOS_FILTRADOS.xlsx"

df_sorted.to_excel(file_output, index=False)  # - Remove index column in the output file
