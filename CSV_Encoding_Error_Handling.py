import pandas as pd

# Attempting to read the CSV file with a different encoding.
# 'ISO-8859-1' or 'latin1' are used for CSV files with encoding issues.
# The file path where ChatGPT stores the data to be
csv_file_path = '/mnt/data/How physics flew the philosophers\' nest extracted_theories.csv'



# Read the CSV file into a pandas DataFrame

try:
    df_extracted = pd.read_csv(csv_file_path)
except:
    pass
try:
    df_extracted = pd.read_csv(csv_file_path, encoding='ISO-8859-1')
except Exception as e:
    error_message = str(e)

error_message if 'error_message' in locals() else df_extracted.head()
