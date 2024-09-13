import pandas as pd
import sqlite3

def save_into_db(DEBUG:bool =False) -> None:
    df = pd.read_csv("data\data.csv")

    if DEBUG:
        print(df.head())
        print(df.keys())

    

    conn = sqlite3.connect('data\data.db')


    df.to_sql('dsa', conn, if_exists='replace', index=False)

    conn.close()

if __name__ == '__main__':
    save_into_db(DEBUG=True)