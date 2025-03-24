import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
def load_data(file_path):
    df = pd.read_excel(file_path)
    df['Year'] = pd.to_datetime(df['Year'], errors='coerce').dt.year
    df['WAR'] = pd.to_numeric(df['WAR'], errors='coerce')
    return df

# Extract player name from the URL
def extract_player_name(url):
    return url.split('/')[4]

# Display available players and ask for selection
def select_player(players):
    print("Available players:")
    for idx, player in enumerate(players, start=1):
        print(f"{idx}. {player}")
    
    choice = int(input("\nEnter the number corresponding to the player (or 0 to exit): "))
    
    if choice == 0:
        return None  # Exit the loop if the user chooses 0
    
    selected_player = players[choice - 1]
    return selected_player

# Plot the WAR over time for the selected player
def plot_war(player_name, df):
    player_data = df[df['Player'] == player_name]
    
    if player_data.empty:
        print(f"No data found for player: {player_name}")
        return

    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.plot(player_data['Year'], player_data['WAR'], marker='o', linestyle='-', color='b')
    plt.title(f"WAR Over Time for {player_name}")
    plt.xlabel("Year")
    plt.ylabel("WAR")
    plt.grid(True)
    plt.show()

# File path for the Excel file
file_path = r"C:\Users\dmaph\Documents\GitHub\MLB\scraped_war_data.xlsx"

# Load the data
df = load_data(file_path)

# Extract player names and add as a new column
df['Player'] = df['URL'].apply(extract_player_name)

# Get unique player names for selection
players = df['Player'].unique()

# Start an interactive loop to select players
while True:
    # Let the user select a player
    selected_player = select_player(players)
    
    if selected_player is None:
        print("Exiting the program.")
        break
    
    # Plot the WAR over time for the selected player
    plot_war(selected_player, df)
