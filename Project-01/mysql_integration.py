# mysql_integration.py
import mysql.connector
import pandas as pd
from mysql.connector import Error

def insert_into_mysql(df):
    """Step 3: MySQL Integration - Insert cleaned data into MySQL"""
    if df is None:
        print("Error: No dataset loaded. Please load and clean the dataset first.")
        return None
    
    print("\nStarting MySQL integration process...")
    
    try:
        print("Preparing MySQL connection configuration...")
        # MySQL connection configuration
        config = {
            "host": "localhost",
            "user": "ritesh",
            "password": "4312",  # Replace with your actual password
            "database": "used_cars_db",
            "connect_timeout": 10
        }
        print(f"Connection config: host={config['host']}, user={config['user']}, database={config['database']}")
        
        print("Attempting to connect to MySQL database...")
        connection = mysql.connector.connect(**config)
        
        print("Checking connection status...")
        if connection.is_connected():
            print("Connected successfully to MySQL database!")
        else:
            print("Error: Connection established but not active.")
            return df
        
        cursor = connection.cursor()
        print("Database cursor created.")
        
        # Verify database exists
        print("Verifying database 'used_cars_db' exists...")
        cursor.execute("SHOW DATABASES LIKE 'used_cars_db'")
        if not cursor.fetchone():
            print("Error: Database 'used_cars_db' does not exist.")
            return df
        print("Database 'used_cars_db' found.")
        
        # Verify table exists
        print("Verifying table 'cars' exists...")
        cursor.execute("SHOW TABLES LIKE 'cars'")
        if not cursor.fetchone():
            print("Error: Table 'cars' does not exist in database 'used_cars_db'.")
            return df
        print("Table 'cars' found.")
        
        # Clear table to avoid duplicates
        print("Clearing 'cars' table before insertion...")
        cursor.execute("TRUNCATE TABLE cars")
        connection.commit()
        print("Table 'cars' cleared.")
        
        # Prepare SQL insert query
        print("Preparing SQL insert query...")
        insert_query = """
        INSERT INTO cars (
            make, model, year, price, mileage, body_type, cylinders,
            transmission, fuel_type, color, location, description
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        
        # Prepare data for insertion
        print("Converting DataFrame to list for insertion...")
        data = df[[
            "make", "model", "year", "price", "mileage", "body_type", "cylinders",
            "transmission", "fuel_type", "color", "location", "description"
        ]].values.tolist()
        print(f"Data prepared: {len(data)} rows to insert.")
        
        # Insert data
        print("Inserting data into 'cars' table...")
        cursor.executemany(insert_query, data)
        connection.commit()
        print(f"Successfully inserted {cursor.rowcount} rows into 'cars' table.")
        
        # Verify insertion
        print("Verifying total rows in 'cars' table...")
        cursor.execute("SELECT COUNT(*) FROM cars")
        row_count = cursor.fetchone()[0]
        print(f"Total rows in 'cars' table after insertion: {row_count}")
        
        return df
        
    except Error as e:
        print(f"MySQL Error [Code {e.errno}]: {e.msg}")
        return df
    except Exception as e:
        print(f"General Error during MySQL integration: {str(e)}")
        return df
    finally:
        if 'connection' in locals() and connection.is_connected():
            print("Closing database cursor and connection...")
            cursor.close()
            connection.close()
            print("MySQL connection closed.")
        else:
            print("No active connection to close.")