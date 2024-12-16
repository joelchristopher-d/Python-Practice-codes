import pandas as pd

file_path = r"D:\Rotten_Tomatoes_Movies3.xls"
data = pd.read_excel(file_path)  
print(data.head())
print(data.info())
