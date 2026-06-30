import pandas as pd 
d=pd.read_csv(r'C:\Users\chauh\.vscode\Rudra python\quikr_car.csv')
print(d)
data=[10,20,30,40,50]
s=pd.Series(data)
print(s[1:4])
data2={"Name":["Rudra","Anamika","Vishnu"],
       "Age":[21,20,20],
       "City":["Chandigarh","Dehradun","Delhi"]}
df=pd.DataFrame(data2)
print(df)
print(df["Name"])
print(df.iloc[2])
print(df.loc[2])
print(df[1:3])
print(df["Age"].unique())