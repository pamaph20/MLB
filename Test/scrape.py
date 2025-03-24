import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# Function to extract URLs and associated data from the Excel file
def extract_data(file_path, url_column, il_date_column, return_date_column):
    df = pd.read_excel(file_path)

    missing_columns = [col for col in [url_column, il_date_column, return_date_column] if col not in df.columns]
    if missing_columns:
        print(f"Missing columns in the Excel file: {missing_columns}")
        return {}

    data_dict = {}
    for _, row in df.iterrows():
        url = row[url_column]
        il_date = row[il_date_column] if pd.notna(row[il_date_column]) else ""
        return_date = row[return_date_column] if pd.notna(row[return_date_column]) else ""

        if isinstance(url, str) and re.match(r'^https?://', url):
            data_dict[url] = {
                "IL Date": il_date,
                "Return Date": return_date
            }
    print(len(data_dict))
    return data_dict


# Function to scrape WAR data for multiple URLs
def scrape_war_for_multiple_urls(data_dict):
    result = []  # List to hold results for saving to Excel
    for url, info in data_dict.items():
        try:
            # Send an HTTP request to the page
            response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

            # Check if the request was successful
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')

                # Find the div with the id 'dashboard'
                dashboard_div = soup.find('div', id='dashboard')

                # Check if we found the dashboard div
                if dashboard_div:
                    # Find the table within that div
                    dashboard_table = dashboard_div.find('table')

                    if dashboard_table:
                        # Find all the rows within the table with the class 'row-mlb-season'
                        rows = dashboard_table.find_all('tr', class_='row-mlb-season')
                        print("Found Table with URL : " + url)
                        # Loop through each row and extract the WAR column
                        for row in rows:
                            # Find the season year
                            season_td = row.find('td', {'data-stat': 'Season'})
                            if season_td:
                                season = season_td.get_text(strip=True)
                                
                                # Find the WAR data
                                war_td = row.find('td', {'data-stat': 'WAR'})
                                if war_td:
                                    print("Found War")
                                    war_value = war_td.get_text(strip=True)
                                    # Append the URL, season, and WAR value to the result list
                                    result.append([url, season, war_value])
                                    
            else:
                continue

        except requests.exceptions.RequestException as e:
            continue

    return result


# Define file path and column names
file_path = 'C:/Users/dmaph/Documents/GitHub/MLB/Test/Injury Data.xlsx'
url_column = 'Player Link'
il_date_column = 'IL Date'
return_date_column = 'Return Date'

# Extract URLs and associated data
data_dict = extract_data(file_path, url_column, il_date_column, return_date_column)

# Scrape WAR data for each URL and get the result
war_data = scrape_war_for_multiple_urls(data_dict)

# Convert the result into a DataFrame
df = pd.DataFrame(war_data, columns=['URL', 'Year', 'WAR'])

# Save the data to an Excel file
output_file = 'scraped_war_data.xlsx'
df.to_excel(output_file, index=False)

print(f"Data saved to {output_file}")
