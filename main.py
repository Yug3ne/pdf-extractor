import pandas as pd
import tabula

# Extract tables from the PDF
tables = tabula.read_pdf("bills.pdf", pages="all", multiple_tables=True)

# Combine all DataFrames into one (if tables is not empty)
if tables:
    df = pd.concat(tables, ignore_index=True)
    df.to_csv('bills.csv', index=False)
else:
    print("No tables found in the PDF.")
