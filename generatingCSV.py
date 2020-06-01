import sqlite3
import os.path
import pandas as pd

def main():
    fileName = "data/spotifyCSV.csv"
    if not(os.path.exists(fileName)):
        conn = sqlite3.connect("data/billboard-200.db", isolation_level=None,detect_types=sqlite3.PARSE_COLNAMES)
        db_df = pd.read_sql_query("SELECT * FROM acoustic_features", conn)
        db_df.to_csv('database.csv', index=False)
    else:
        print("File already exists")
        
if __name__ == '__main__':
    main()