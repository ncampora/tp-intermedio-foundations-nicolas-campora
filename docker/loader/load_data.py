import pandas as pd
import psycopg2
import os

DATA_PATH = os.getenv("DATA_PATH", "/data/imdb_top_1000.csv")

# Leer CSV
df = pd.read_csv(DATA_PATH)

# Renombrar columnas para que coincidan con la tabla
df = df.rename(columns={
    "Series_Title": "title",
    "Released_Year": "year",
    "Genre": "genre",
    "Director": "director",
    "Runtime": "runtime_minutes",
    "IMDB_Rating": "rating",
    "No_of_Votes": "votes"
})

# Convertir runtime "142 min" → 142
def parse_runtime(runtime_str):
    try:
        return int(str(runtime_str).split()[0])
    except:
        return None

df["runtime_minutes"] = df["runtime_minutes"].apply(parse_runtime)

# Conectar a PostgreSQL
conn = psycopg2.connect(
    host="db",
    database="imdb",
    user="imdb_user",
    password="imdb_pass"
)
cur = conn.cursor()

# Limpiar la tabla antes de insertar
cur.execute("TRUNCATE TABLE movies RESTART IDENTITY;")
print("Tabla 'movies' limpiada antes de la carga.")

# Insertar registros
for idx, row in df.iterrows():
    # limpiar año: si está vacío o no es numérico, lo pasamos a None
    year_val = row['year']
    try:
        year = int(year_val)
    except:
        year = None

    cur.execute("""
        INSERT INTO movies (title, year, genre, director, runtime_minutes, rating, votes)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        row['title'],
        year,
        row['genre'],
        row['director'],
        row['runtime_minutes'],
        row['rating'],
        row['votes']
    ))

conn.commit()
cur.close()
conn.close()