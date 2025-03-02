import pandas as pd
import matplotlib.pyplot as plt

# Creating sample IPL data
data = {
    'season': [2023]*15,
    'team1': ['MI', 'CSK', 'RCB', 'KKR', 'SRH', 'PBKS', 'GT', 'DC', 'LSG', 'RR', 'KKR', 'SRH', 'PBKS', 'GT', 'MI'],
    'team2': ['CSK', 'RCB', 'KKR', 'SRH', 'PBKS', 'GT', 'DC', 'LSG', 'RR', 'MI', 'CSK', 'RCB', 'KKR', 'SRH', 'PBKS'],
    'winner': ['MI', 'CSK', 'RCB', 'KKR', 'SRH', 'PBKS', 'GT', 'DC', 'RR', 'MI', 'KKR', 'SRH', 'PBKS', 'GT', 'CSK'],
    'city': ['Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad', 'Mohali', 'Ahmedabad', 'Delhi', 'Lucknow', 'Jaipur', 'Kolkata', 'Hyderabad', 'Mohali', 'Ahmedabad', 'Mumbai'],
    'player_of_match': ['Rohit Sharma', 'MS Dhoni', 'Virat Kohli', 'Andre Russell', 'Kane Williamson', 'Shikhar Dhawan',
                        'Hardik Pandya', 'David Warner', 'Sanju Samson', 'Jasprit Bumrah', 'Rishabh Pant', 'Faf du Plessis',
                        'Liam Livingstone', 'Shubman Gill', 'Suryakumar Yadav'],
    'runs_scored': [180, 190, 200, 210, 175, 185, 195, 160, 170, 200, 180, 190, 210, 200, 195]
}

# Creating a DataFrame
ipl_df = pd.DataFrame(data)

# Basic Data Exploration
team_wins = ipl_df['winner'].value_counts()
player_of_match_counts = ipl_df['player_of_match'].value_counts()
average_runs_per_match = ipl_df['runs_scored'].mean()

# Bar Chart for Wins by Team
plt.figure(figsize=(8, 5))
team_wins.plot(kind='bar', color='blue', alpha=0.7)
plt.xlabel("Team")
plt.ylabel("Number of Wins")
plt.title("Number of Wins by Team")
plt.xticks(rotation=45)
plt.savefig("team_wins_chart.png")
plt.close()

# Histogram of Runs Scored
plt.figure(figsize=(8, 5))
plt.hist(ipl_df['runs_scored'], bins=5, color='green', alpha=0.7)
plt.xlabel("Runs Scored")
plt.ylabel("Frequency")
plt.title("Distribution of Runs Scored per Match")
plt.savefig("runs_distribution_chart.png")
plt.close()

# Save DataFrame to CSV
ipl_df.to_csv("ipl_analysis.csv", index=False)
