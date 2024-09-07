import pandas as pd
from tabulate import tabulate
while True:
    print('\t\t *** Cricket Data Analysis Project *** ')
    print('\n\t\t\t1. Data Analysis')
    print('\n\t\t\t2. Data Visualization')
    print('\n\t\t\t3. Exit\n')
    choice=int(input('Select your choice [1-3] : '))
    if choice==1:
        while True:
            print('\t*** CRICKET DATA ANALYSIS SYSTEM')
            print('*'*50)
            print('\n\t\t1. Show Batsmen data')
            print('\n\t\t2. Show Bowler data')
            print('\n\t\t3. Exit to main menu\n\n')
            choice=int(input('Select your choice [1-3] : '))
            if choice==1:
                print('\nBatsmen Data:\n\n')
                df=pd.read_csv('/mnt/f/worldcup_2023_cricket_data/batting_summary.csv')
                print(tabulate(df,showindex=False,headers=['Match No', 'Match Between', 'Team', 'Batsman', 'Batsman Position', 'Dismissal', 'Runs', 'Balls', '4s', '6s', 'Strike Rate'],tablefmt='pretty'))
            elif choice==2:
                print('\nBowler Data:\n\n')
            elif choice==3:
                print('Exit to main menu...')
                break
    elif choice==2:
        while True:
            print('\t*** CRICKET DATA VISUALIZATION')
            print('*'*50)
            print('\n\t\t1. Plot Line Chart (Name and runs)')
            print('\n\t\t2. Plot Line Chart (Name and wickets)')
            print('\n\t\t3. Exit the Program\n\n')
            choice=int(input('Select your choice [1-3] : '))
    elif choice==3:
        print('Exit from menu...')
        break
    else:
        print('Invalid choice')
