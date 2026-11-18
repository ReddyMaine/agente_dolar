from pathlib import Path
import sys

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

sys.path.append(str(BASE_DIR))

from database.postgres import get_connection
from utils.detector import has_real_site
from utils.score import calculate_score


def normalize(value):

    if pd.isna(value):
        return None

    value = str(value).strip()

    if value.lower() == "nan":
        return None

    return value


excel_path = (
    BASE_DIR
    / "uploads"
    / "Bing_Maps_Scraper_105__20261106133348.xlsx"
)

df = pd.read_excel(excel_path)

conn = get_connection()

cur = conn.cursor()

inserted = 0
duplicates = 0

for _, row in df.iterrows():

    company_name = normalize(row["Name"])
    phone = normalize(row["Phone"])
    website = normalize(row["Website"])
    category = normalize(row["Category"])
    address = normalize(row["Address"])

    instagram = normalize(row["Instagram"])
    facebook = normalize(row["Facebook"])
    emails = normalize(row["Emails"])

    has_site = has_real_site(website)

    score = calculate_score(
        has_site=has_site,
        phone=phone,
        category=category,
        instagram=instagram,
        email=emails,
    )

    try:

        cur.execute(
            """
            INSERT INTO leads
            (
                company_name,
                phone,
                website,
                category,
                city,
                score,
                has_site,
                instagram,
                facebook,
                emails
            )
            VALUES
            (
                %s,%s,%s,%s,%s,
                %s,%s,%s,%s,%s
            )

            ON CONFLICT(phone)
            DO NOTHING
            """,
            (
                company_name,
                phone,
                website,
                category,
                address,
                score,
                has_site,
                instagram,
                facebook,
                emails,
            ),
        )

        if cur.rowcount:
            inserted += 1
        else:
            duplicates += 1

    except Exception as e:

        print()
        print(f"ERRO AO INSERIR: {company_name}")
        print(str(e))
        print()

conn.commit()

cur.close()
conn.close()

print()
print("================================")
print("IMPORTAÇÃO FINALIZADA")
print("================================")
print(f"Inseridos: {inserted}")
print(f"Duplicados: {duplicates}")