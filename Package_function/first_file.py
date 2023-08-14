import pandas as pd
from openpyxl import load_workbook

# Загрузка данных из файла Excel
excel_file = "Kidwill.xlsx"
df = pd.read_excel(excel_file)

# Создание нового файла CSV
csv_file = "Kidwill_data.csv"
df.to_csv(csv_file, index=False)

