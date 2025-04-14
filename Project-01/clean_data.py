# clean_data.py
import pandas as pd

def clean_data(df):
    """Step 2: Data Cleaning & Sanitization"""
    if df is None:
        print("Error: No dataset loaded. Please load the dataset first (Option 1).")
        return None
    
    try:
        print("\nStarting data cleaning process...")
        
        # Step 1: Remove duplicate entries
        initial_rows = df.shape[0]
        df = df.drop_duplicates()
        duplicates_removed = initial_rows - df.shape[0]
        print(f"Removed {duplicates_removed} duplicate rows.")
        
        # Step 2: Handle missing values
        # Fill missing strings with 'Unknown', numeric with median
        for col in df.columns:
            if df[col].dtype == "object":
                df[col] = df[col].fillna("Unknown")
            else:
                df[col] = df[col].fillna(df[col].median())
        
        # Step 3: Normalize data formats
        df["Year"] = df["Year"].astype(int)
        df["Price"] = pd.to_numeric(df["Price"], errors="coerce").fillna(df["Price"].median())
        df["Mileage"] = pd.to_numeric(df["Mileage"], errors="coerce").fillna(df["Mileage"].median())
        df["Cylinders"] = df["Cylinders"].astype(int, errors="ignore")
        
        # Step 4: Filter outliers
        initial_rows = df.shape[0]
        df = df[
            (df["Year"] <= 2025) & 
            (df["Year"] >= 1980) &  # Assume no cars older than 1980
            (df["Price"] > 0) & 
            (df["Mileage"] > 0)
        ]
        outliers_removed = initial_rows - df.shape[0]
        print(f"Removed {outliers_removed} rows with unrealistic values (Year > 2025, Year < 1980, Price <= 0, or Mileage <= 0).")
        
        # Step 5: Standardize column names
        df.columns = df.columns.str.lower().str.replace(" ", "_")
        print("Standardized column names to lowercase with underscores.")
        
        # Display cleaned dataset info
        print("\nCleaning complete! Dataset summary:")
        print(f"Dataset shape: {df.shape}")
        print("\nFirst 5 rows of cleaned dataset:")
        print(df.head())
        print("\nMissing values per column:")
        print(df.isnull().sum())
        
        return df
        
    except Exception as e:
        print(f"An error occurred during cleaning: {e}")
        return None