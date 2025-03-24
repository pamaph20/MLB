import requests
from bs4 import BeautifulSoup

# Function to scrape the WAR values from the specific 'dashboard' div
def scrape_war(url):
    # Send an HTTP request to the page
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

    # Check if the request was successful
    if response.status_code == 200:
        print("Successfully retrieved the page!")
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the div with the id 'dashboard'
        dashboard_div = soup.find('div', id='dashboard')

        # Check if we found the dashboard div
        if dashboard_div:
            print("Found the dashboard div!")
            # Now find the table within that div
            dashboard_table = dashboard_div.find('table')

            if dashboard_table:
                print("Found the dashboard table!")
                # Find all the rows within the table with the class 'row-mlb-season'
                rows = dashboard_table.find_all('tr', class_='row-mlb-season')

                # If no rows are found, print a message
                if not rows:
                    print("No rows found in the dashboard table.")
                else:
                    # Loop through each row and extract the WAR column
                    for row in rows:
                        # Find the WAR data (it's in the <td> element with data-stat="WAR")
                        war_td = row.find('td', {'data-stat': 'WAR'})

                        # If we found the WAR column, extract its text (the WAR value)
                        if war_td:
                            war_value = war_td.get_text(strip=True)
                            print(f"WAR: {war_value}")
                        else:
                            print("WAR data not found for this row.")
            else:
                print("No table found within the dashboard div.")
        else:
            print("Dashboard div not found.")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

# Example URL for Stephen Strasburg
url = "https://www.fangraphs.com/players/juan-soto/20123/stats?position=OF"

# Scrape the WAR values from the page
scrape_war(url)
