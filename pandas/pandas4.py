import pandas as pd
s1 = pd.Series([30000,40000,35000], index = ["Anil","Kumar","Bala"])
Name = input("Enter the name: ")
New_salary = int(input("Enter the new salary: "))
s1[Name] = New_salary
print(s1)
