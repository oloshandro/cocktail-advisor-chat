import pandas as pd

def read_csv_file(filepath):
    try:
        df = pd.read_csv(filepath, encoding="utf-8")  # Try loading with UTF-8
        print("CSV loaded successfully!")
        return df
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
    except pd.errors.ParserError:
        print("Error: CSV parsing issue. Check delimiter or file structure.")
    except Exception as e:
        print(f"Unexpected error: {e}")