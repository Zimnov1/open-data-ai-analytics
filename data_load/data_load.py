import pandas as pd
import os
from sqlalchemy import create_engine

def load_data(path):
    df = pd.read_excel(path, engine='xlrd')
    return df

def save_to_db(df, table_name):
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        raise ValueError("DATABASE_URL variable is not set")
    
    engine = create_engine(db_url)
    
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"Data imported to table: {table_name}")

if __name__ == "__main__":
    os.makedirs("artifacts/data_load", exist_ok=True)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "..", "data", "dohodi_vsi.xls")
    
    try:
        df = load_data(file_path)
        
        df.to_csv("artifacts/data_load/dataset.csv", index=False)
        
        save_to_db(df, "incomes")
        
        with open("artifacts/data_load/run.log", "w") as f:
            f.write("Data loaded and imported to DB successfully.\nRows: {}\nColumns: {}".format(df.shape[0], df.shape[1]))
        print("Data loaded successfully.")
        
    except FileNotFoundError:
        error_msg = f"ERROR: File not found at {file_path}"
        with open("artifacts/data_load/run.log", "w") as f:
            f.write(error_msg + "\n")
        print(error_msg)
    except Exception as e:
        error_msg = f"ERROR: {str(e)}"
        with open("artifacts/data_load/run.log", "w") as f:
            f.write(error_msg + "\n")
        print(error_msg)