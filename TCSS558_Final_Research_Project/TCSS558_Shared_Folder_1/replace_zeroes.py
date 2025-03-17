# List of files to modify
files = ["A1.txt", "A2.txt", "B1.txt", "B2.txt", "C1.txt", "C2.txt"]

for file in files:
    # Open each file in write mode to overwrite its contents with "0"
    with open(file, "w") as f:
        f.write("0")

print("All files have been updated to contain '0'.")
