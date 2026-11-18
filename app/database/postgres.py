import os

import psycopg2

from dotenv import load_dotenv

load_dotenv()


def get_connection():
    return psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"),
        database="postgres",
        user="postgres",
        password=os.getenv("POSTGRES_PASSWORD"),
        port="5432",
        sslmode="require",
    )
