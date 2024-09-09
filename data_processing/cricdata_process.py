import csv
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate

def extract_matches_from_file(filename):
    matches = []
    seen_matches = set()  # Store seen match numbers to avoid duplicates
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        for row in reader:
            match_no = row[0]
            if match_no not in seen_matches:
                teams = row[1].split(' vs ')
                matches.append((match_no, teams[0], teams[1]))
                seen_matches.add(match_no)
    return matches

def extract_match_data(filename, match_no):
    df = pd.read_csv(filename)
    match_df = df[df['Match_no'] == match_no]
    return match_df

def serve_batsman_data_analysis(filename, match_number):
    while True:
        match_df = extract_match_data(filename, match_number)
        print('\t*** CRICKET DATA ANALYSIS SYSTEM ***')
        print('*'*50)
        print('\n\t\t1. Show Batsmen and runs')
        print('\n\t\t2. Show Batsmen and strike rate')
        print('\n\t\t3. Show Batsmen score card')
        print('\n\t\t4. Exit to main menu\n\n')
        choice=int(input('Select your choice [1-3] : '))
        if choice==1:
            print('\nBatsmen and runs:\n\n')
            runs_columns = ['Match_no', 'Match_Between', 'Team_Innings', 'Batsman_Name', 'Batting_Position', 'Runs']
            match_df = match_df[runs_columns]
            print(tabulate(match_df,showindex=False,headers=runs_columns,tablefmt='pretty'))
        elif choice==2:
            print('\nBatsmen and strike rate:\n\n')
            strike_rate_columns = ['Match_no', 'Match_Between', 'Team_Innings', 'Batsman_Name', 'Batting_Position', 'Strike_Rate']
            match_df = match_df[strike_rate_columns]
            print(tabulate(match_df,showindex=False,headers=strike_rate_columns,tablefmt='pretty'))
        elif choice==3:
            print('\nBatsmen score card:\n\n')
            scorecard_columns = ['Match_no', 'Match_Between', 'Team_Innings', 'Batsman_Name', 'Batting_Position', 'Dismissal', 'Runs', 'Balls', '4s', '6s', 'Strike_Rate']
            match_df = match_df[scorecard_columns]
            print(tabulate(match_df,showindex=False,headers=scorecard_columns,tablefmt='pretty'))
        elif choice==4:
            print('Exit to main menu...')
            break

def serve_bowler_data_analysis(filename, match_number):
    while True:
        match_df = extract_match_data(filename, match_number)
        print('\t*** CRICKET DATA ANALYSIS SYSTEM ***')
        print('*'*50)
        print('\n\t\t1. Show Bowlers, Runs and wickets')
        print('\n\t\t2. Show Bowlers, Maidens and economy')
        print('\n\t\t3. Show Bowlers score card')
        print('\n\t\t4. Exit to main menu\n\n')
        choice=int(input('Select your choice [1-3] : '))
        if choice==1:
            print('\nBowlers and wickets:\n\n')
            wickets_columns = ['Match_no', 'Match_Between', 'Bowling_Team', 'Bowler_Name', 'Overs', 'Runs', 'Wickets']
            match_df = match_df[wickets_columns]
            print(tabulate(match_df,showindex=False,headers=wickets_columns,tablefmt='pretty'))
        elif choice==2:
            print('\nBowlers and economy:\n\n')
            wickets_columns = ['Match_no', 'Match_Between', 'Bowling_Team', 'Bowler_Name', 'Overs', 'Maidens', 'Economy']
            match_df = match_df[wickets_columns]
            print(tabulate(match_df,showindex=False,headers=wickets_columns,tablefmt='pretty'))
        elif choice==3:
            print('\nBowlers score card:\n\n')
            scorecard_columns = ['Match_no', 'Match_Between', 'Bowling_team', 'Bowler_Name', 'Overs', 'Maidens', 'Runs', 'Wickets', 'Economy']
            print(tabulate(match_df,showindex=False,headers=scorecard_columns,tablefmt='pretty'))
        elif choice==4:
            print('Exit to main menu...')
            break

def serve_batting_data_visualization(filename, match_number):
    while True:
        match_df = extract_match_data(filename, match_number)
        print('\t*** CRICKET DATA VISUALIZATION ***')
        print('*'*50)
        print('\n\t\t1. Plot Line Chart (Name and runs)')
        print('\n\t\t2. Plot Line Chart (Name and strike rate)')
        print('\n\t\t3. Exit to the main menu\n\n')
        choice=int(input('Select your choice [1-3] : '))
        if choice==1:
            plt.figure(figsize=(12, 6))
            plt.plot(match_df['Batsman_Name'], match_df['Runs'], marker='o', linestyle='-', color='green')
            plt.title(f"Batsmen Runs for Match {match_number}")
            plt.xlabel('Batsman')
            plt.ylabel('Runs')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            #plt.show()
            plt.savefig('batsmen_run.png')
        elif choice==2:
            plt.figure(figsize=(12, 6))
            plt.plot(match_df['Batsman_Name'], match_df['Strike_Rate'], marker='o', linestyle='-', color='green')
            plt.title(f"Batsmen Strike Rate for Match {match_number}")
            plt.xlabel('Batsman')
            plt.ylabel('Strike_Rate')
            plt.grid(True)
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            #plt.show()
            plt.savefig('batsmen_strike_rate.png')
        elif choice==3:
            print('Exiting to the main menu...')
            break

def get_match_number(filename):
    print('\t Choose a match from world cup 2023')
    matches = extract_matches_from_file(filename)
    for match in matches:
        print(f"\t\tMatch {match[0]}: {match[1]} vs {match[2]}")
    match_number=int(input(f'\nSelect a match [1-{len(matches)}] : '))
    return match_number

def serve_cricket_data_processing():
    batting_summary_file = '/mnt/f/worldcup_2023_cricket_data/batting_summary.csv'
    bowling_summary_file = '/mnt/f/worldcup_2023_cricket_data/bowling_summary.csv'
    while True:
        print('\t\t *** Cricket Data Analysis *** ')
        print('\n\t\t\t1. Batsman Data Analysis')
        print('\n\t\t\t2. Bowler Data Analysis')
        print('\n\t\t\t3. Batsman Data Visualization')
        print('\n\t\t\t4. Bowler Data Visualization')
        print('\n\t\t\t5. Exit the program\n')
        main_choice=int(input('Select your choice [1-3] : '))
        if main_choice == 1:
            filename = batting_summary_file
            match_number = get_match_number(filename)
            serve_batsman_data_analysis(filename, match_number)
        elif main_choice == 2:
            filename = bowling_summary_file
            match_number = get_match_number(filename)
            serve_bowler_data_analysis(filename, match_number)
        elif main_choice == 3:
            filename = batting_summary_file
            match_number = get_match_number(filename)
            serve_batting_data_visualization(filename, match_number)
        elif main_choice == 4:
            filename = bowling_summary_file
            match_number = get_match_number(filename)
            serve_bowling_data_visualization(filename, match_number)
        elif main_choice == 5:
            print('Exiting the program. Have a nice day...')
            break
        else:
            print('Invalid choice')


if __name__ == "__main__":
  serve_cricket_data_processing()
