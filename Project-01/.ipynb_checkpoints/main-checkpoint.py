import pandas as pd
import numpy as np
import mysql.connector
import os
from mysql.connector import Error
from clean_data import clean_data
from mysql_integration import insert_into_mysql  # Import the renamed function# Global variable to store DataFrame
df = None

def load_dataset():
    """Step 1: Dataset Acquisition - Load the CSV file"""
    global df
    csv_path = "uae_used_cars_10k.csv"
    
    try:
        # Check if file exists
        if not os.path.exists(csv_path):
            print(f"Error: File '{csv_path}' not found. Please ensure it's in the 'data/' folder.")
            return
        
        # Read CSV into DataFrame
        df = pd.read_csv(csv_path)
        print("Dataset loaded successfully!")
        print("\nFirst 5 rows of the dataset:")
        print(df.head())
        print(f"\nDataset shape: {df.shape}")
        
    except FileNotFoundError:
        print(f"Error: File '{csv_path}' not found.")
    except pd.errors.EmptyDataError:
        print("Error: The CSV file is empty or corrupted.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def display_menu():
    """Display the menu options"""
    print("\n=== UAE Used Cars Analysis Menu ===")
    print("1. Load Dataset")
    print("2. Clean Data")
    print("3. Insert Data into MySQL")
    print("4. Perform Analysis")
    print("5. Display Results")
    print("6. Exit")
    return input("Enter your choice (1-6): ")

def main():
    global df  # Declare df as global to allow modification
    while True:
        choice = display_menu()
        
        if choice == "1":
            load_dataset()
        elif choice == "2":
            df = clean_data(df)  # Now df is properly handled
        elif choice == "3":
            df = insert_into_mysql(df)
        elif choice == "4":
            print("Analytical Computation - Not implemented yet.")
        elif choice == "5":
            print("Console Output - Not implemented yet.")
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()