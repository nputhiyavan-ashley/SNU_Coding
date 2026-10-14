"""
Name: Vignesh V
ID: 23110571

Question:
 - Analyse a CSV File and output the summary of each Column details One by One

Steps:
 - Read the CSV Files
 - Iterate through each columns
 - count the Missing values 
 - calculate the valid percentage
 - Print the results in formated way
"""
import pandas as pd

def analyseCSV(fileName:str):
    fp = pd.read_csv(fileName)
    cols = fp.columns

    sol = []
    for col in cols:

        missingCount = fp[col].isnull().sum() 
        validPercent = round(((len(fp) - missingCount) / len(fp)) * 100,2)

        ans = str(f"Column Name: {col} - Missing Count: {missingCount} - Valid Percentage: {validPercent}")
        sol.append(ans)

    return sol

Ans1 = analyseCSV("input1.csv")
Ans2 = analyseCSV("input2.csv")

print("Test 1")
for ans in Ans1:
    print(ans)

print("\nTest 2")
for ans in Ans2:
    print(ans)