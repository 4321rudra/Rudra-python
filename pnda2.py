
import pandas as pd 

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/LXjSAttmoxJfEG6il1Bqfw/Product-sales.csv"
df = pd.read_csv(filename)
# print(df.head())
xlsx_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/n9LOuKI9SlUa1b5zkaCMeg/Product-sales.xlsx'
df2 = pd.read_excel(xlsx_path)
# print(df2.head())
x=df2[['Quantity']]
print(x)
