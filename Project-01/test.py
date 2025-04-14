# with open("uae_used_cars_10k.csv","r+") as file:
#     content = file.read()
#     print(content)
import mysql.connector
import pandas as pd

df = pd.read_csv("uae_used_cars_10k.csv")
print(df)
dupli=df.drop_duplicates(inplace=True)
print(dupli)
ddd=df.fillna({

    'Price':df['Price'].median(),
    'Mileage':df['Mileage'].median(),
    'Fuel':'Unknown',
    'Transmission':'Unknown',
    'Year': df['Year'].mode()[0]},
    inplace=True
)
print(ddd)
# Normalize data types
df['Price']=pd.to_numeric(df['Price'])
df['Mileage']=pd.to_numeric(df['Mileage'])
df['Year']=pd.to_numeric(df['Year'])
print(df)
# rename column names
df.rename(columns={
    'Year':'Manufacture_Year',
    'Description':'About',
    'Mileage':'Mileage',
    'Location':'Location',
    'Fuel Type':'Fuel_Type'
},inplace=True)


dff=df[(df['Mileage']==0) & (df['Manufacture_Year']>2025)]
# Filter out unrealistic entries
print(dff)
 # Drop rows with any remaining NaNs
df.dropna(inplace=True)
# print(df.info())

conn = mysql.connector.connect(
    host="localhost",         # or your database IP address
    user="ritesh",     # MySQL username
    password="4312", # MySQL password
    database="used_cars_db"  # Optional: If you want to connect to a specific database
)


cursor=conn.cursor()

insert_query="""
INSERT INTO cars (Make, Model, Manufacture_year, Price, Mileage, Fuel_type, Transmission,Color,Location,About)
VALUES (%s, %s, %s, %s, %s, %s, %s,%s,%s,%s)
"""
data_to_insert=[
    (
        row['Make'],
        row['Model'],
        int(row['Manufacture_Year']),
        float(row['Price']),
        int(row['Mileage']),
        row['Fuel_Type'],
        row['Transmission'],
        row['Color'],
        row['Location'],
        row['About']
    )
    for _,row in df.iterrows()
]
cursor.executemany(insert_query,data_to_insert)
cursor.close()
conn.commit()