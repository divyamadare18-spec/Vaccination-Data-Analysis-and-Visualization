import pandas as pd
import os

print("Vaccination Data Analysis")
print("=========================")

dataset_path = r"D:\Vaccination_Project\Dataset"
cleaned_path = r"D:\Vaccination_Project\Cleaned_Data"

# Create Cleaned_Data folder
os.makedirs(cleaned_path, exist_ok=True)

files = [
    "coverage-data.xlsx",
    "incidence-rate-data.xlsx",
    "reported-cases-data.xlsx",
    "vaccine-introduction-data.xlsx",
    "vaccine-schedule-data.xlsx"
]

for file in files:

    path = os.path.join(dataset_path, file)

    if os.path.exists(path):

        df = pd.read_excel(path)

        print("\nFile:", file)
        print("Original Rows:", len(df))

        # Dataset-specific important columns
        if file == "coverage-data.xlsx":
            important_columns = ["CODE", "YEAR", "ANTIGEN"]

        elif file == "incidence-rate-data.xlsx":
            important_columns = ["CODE", "YEAR", "DISEASE"]

        elif file == "reported-cases-data.xlsx":
            important_columns = ["CODE", "YEAR", "DISEASE"]

        elif file == "vaccine-introduction-data.xlsx":
            important_columns = ["ISO_3_CODE", "YEAR"]

        elif file == "vaccine-schedule-data.xlsx":
            important_columns = ["ISO_3_CODE", "YEAR", "VACCINECODE"]

        # Remove rows with missing important values
        df = df.dropna(subset=important_columns)

        print("Rows after cleaning:", len(df))
        print("Duplicate Rows:", df.duplicated().sum())

        # Save cleaned file
        output_file = os.path.join(cleaned_path, "cleaned_" + file)
        df.to_excel(output_file, index=False)

        print("Saved:", output_file)

    else:
        print("\nFile not found:", file)

print("\nAll datasets cleaned and saved successfully!")