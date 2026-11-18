from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

excel_path = BASE_DIR / "uploads" / "Bing_Maps_Scraper_29__20261106000235.xlsx"

print(excel_path)

df = pd.read_excel(excel_path)

print(df.columns.tolist())
