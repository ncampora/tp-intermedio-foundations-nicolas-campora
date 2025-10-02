import pandas as pd
import psycopg2

DATA_PATH="data/imdb_top_1000.csv"

# Leer CS
df = pd.read_csv(DATA_PATH)

# Limpiar y transformar
df = df.rename (columns={
    "Series_Title": "title",
    "Released_Year": "year",
    "Genre": "genre",
    "Director": "director",
    "Runtime": "runtime",
    "IMDB_Rating": "rating",
    "No_of_Votes": "votes"
})

# Convertir runtime a entero
def parse_runtime(runtime_str):
    try:
        return int(runtime_str.split()[0])
    except:
        return None

# onectar a PostgreSQL
conn = psycopg2.connect(
    host="db",
    database="imdb",
    user="imdb_user",
    password="imdb_pass"
)
cur = conn.cursor()

for _, row in df.iterrows():
    cur.execute("""
        INSERT INTO movies (title, year, genre, director, runtime, rating, votes)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        row['title'],
        row['year'],
        row['genre'],
        row['director'],
        parse_runtime(row['runtime']),
        row['rating'],
        row['votes']
    ))

conn.commit()
cur.close()
conn.close()