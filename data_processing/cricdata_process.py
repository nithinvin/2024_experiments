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

def serve_data_analysis_menu(filename, match_number):
    while True:
        match_df = extract_match_data(filename, match_number)
        print('\t*** CRICKET DATA ANALYSIS SYSTEM ***')
        print('*'*50)
        print('\n\t\t1. Show Batsmen and runs')
        print('\n\t\t2. Show Batsmen and strike rate')
        print('\n\t\t3. Exit to main menu\n\n')
        choice=int(input('Select your choice [1-3] : '))
        if choice==1:
            print('\nBatsmen and runs:\n\n')
            runs_columns = ['Match_no', 'Match_Between', 'Team_Innings', 'Batsman_Name', 'Batting_Position', 'Runs']
            match_df = match_df[runs_columns]
            print(tabulate(match_df,showindex=False,headers=runs_columns,tablefmt='pretty'))
            #print(tabulate(match_df,showindex=False,headers=['Match No', 'Match Between', 'Team', 'Batsman', 'Batsman Position', 'Dismissal', 'Runs', 'Balls', '4s', '6s', 'Strike Rate'],tablefmt='pretty'))
        elif choice==2:
            print('\nBatsmen and strike rate:\n\n')
            runs_columns = ['Match_no', 'Match_Between', 'Team_Innings', 'Batsman_Name', 'Batting_Position', 'Strike_Rate']
            match_df = match_df[runs_columns]
            print(tabulate(match_df,showindex=False,headers=runs_columns,tablefmt='pretty'))
            #df=pd.read_csv('/mnt/f/worldcup_2023_cricket_data/bowling_summary.csv')
            #print(tabulate(df,showindex=False,headers=['Match No', 'Match Between', 'Bowling team', 'Bowler name', 'Overs', 'Maidens', 'Runs', 'Wickets', 'Economy'],tablefmt='pretty'))
        elif choice==3:
            print('Exit to main menu...')
            break

def serve_data_visualization_menu(filename, match_number):
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
            plt.title(f"Batsmen Runs for Match {match_number}")
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
    filename = '/mnt/f/worldcup_2023_cricket_data/batting_summary.csv'
    while True:
        print('\t\t *** Cricket Data Analysis *** ')
        print('\n\t\t\t1. Data Analysis')
        print('\n\t\t\t2. Data Visualization')
        print('\n\t\t\t3. Exit the program\n')
        main_choice=int(input('Select your choice [1-3] : '))
        if main_choice == 1:
            match_number = get_match_number(filename)
            serve_data_analysis_menu(filename, match_number)
        elif main_choice == 2:
            match_number = get_match_number(filename)
            serve_data_visualization_menu(filename, match_number)
        elif main_choice == 3:
            print('Exiting from the main menu...')
            break
        else:
            print('Invalid choice')


if __name__ == "__main__":
  serve_cricket_data_processing()
