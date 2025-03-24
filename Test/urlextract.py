import pandas as pd
import re

# Function to extract URLs and associated data from an Excel file
def extract_data(file_path, url_column, il_date_column, return_date_column):
    # Load the Excel file into a DataFrame
    df = pd.read_excel(file_path)

    # Check if all required columns exist
    missing_columns = [col for col in [url_column, il_date_column, return_date_column] if col not in df.columns]
    if missing_columns:
        print(f"Missing columns in the Excel file: {missing_columns}")
        return {}

    # Extract valid URLs and associated data
    data_dict = {}
    for _, row in df.iterrows():
        url = row[url_column]
        il_date = row[il_date_column] if pd.notna(row[il_date_column]) else ""
        return_date = row[return_date_column] if pd.notna(row[return_date_column]) else ""

        # Ensure the URL is valid
        if isinstance(url, str) and re.match(r'^https?://', url):
            data_dict[url] = {
                "IL Date": il_date,
                "Return Date": return_date
            }

    return data_dict

# Example usage
file_path = 'C:/Users/dmaph/Documents/GitHub/MLB/Test/Injury Data.xlsx'
url_column = 'Player Link'
il_date_column = 'IL Date'
return_date_column = 'Return Date'

# Extract data
data_dict = extract_data(file_path, url_column, il_date_column, return_date_column)

# Print result
print(data_dict)
