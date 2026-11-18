import os

import psycopg
from dotenv import load_dotenv


def test_conecta_a_la_base():
    # 1. Carga las variables del .env
    # 2. lee DATABASE_URL
    # 3. conectate y ejecuta SELECT 1
    # 4. comprueba con assert que la respuesta es 1

    load_dotenv()
    url = os.environ["DATABASE_URL"]
    with psycopg.connect(url) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT 1")
            fila = cur.fetchone()
            assert fila == (1,)