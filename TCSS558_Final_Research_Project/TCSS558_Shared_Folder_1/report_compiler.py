import pandas as pd
import re

# List of report files to compile
files = [
    "A1_simulation_report.txt",
    "A2_simulation_report.txt",
    "B1_simulation_report.txt",
    "B2_simulation_report.txt",
    "C1_simulation_report.txt",
    "C2_simulation_report.txt"
]

# Dictionary to hold data for each file
data = {}

for file in files:
    with open(file, "r") as f:
        # Read lines and remove any trailing newline characters
        lines = f.read().splitlines()
    
    # Check if there are at least 8 lines
    if len(lines) >= 8:
        # Extract the first number from line 8 using regex
        match = re.search(r"[-+]?[0-9]*\.?[0-9]+", lines[7])
        if match:
            lines[7] = match.group(0)  # Replace line 8 with the extracted number

    # Use a shorter column name (e.g., "A1" instead of "A1_simulation_report.txt")
    col_name = file.split("_")[0]
    data[col_name] = lines

# Create a DataFrame where each column corresponds to one report file
df = pd.DataFrame(data)

# Save the compiled DataFrame to a CSV file
df.to_csv("compiled_reports.csv", index=False)

print("CSV file 'compiled_reports.csv' has been created.")

