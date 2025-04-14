import pandas as pd

df=pd.read_csv("task.csv")
no_duplicates=df.drop_duplicates(subset="uuid",keep="first")
duplicate_removes=len(df)-len(no_duplicates)
print(duplicate_removes)

incomplete_record=no_duplicates[
    no_duplicates[["firstname","surname","email"]].isnull().any(axis=1) |
    no_duplicates[["firstname","surname","email"]].eq("").any(axis=1)
]

incomplete_count=len(incomplete_record)

cleaned_records=no_duplicates.drop(incomplete_record.index)

cleaned_records.to_csv("Cleaned_Data.csv",index=False)
incomplete_record.to_csv("Incomplete_Records.csv",index=False)  

print(f"Duplicates removed : {duplicate_removes}")
print(f"Records with missing values : {incomplete_count}")