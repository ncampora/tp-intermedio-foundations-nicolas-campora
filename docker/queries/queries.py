import psycopg2
import pandas as pd

conn = psycopg2.connect(
    host="db",
    database="imdb",
    user="imdb_user",
    password="imdb_pass"
)

queries = {
    "Top 10 irecctores con mejor rating": """
        SELECT director, ROUND (AVG(rating), 2) AS avg_rating
        FROM movies
        WHERE rating IS NOT NULL
        GROUP BY director
        ORDER BY avg_rating DESC
        LIMIT 10;
    """,
    "Peliculas por año": """
        SELECT year, COUNT(*) AS cantidad
        FROM movies
        WHERE year IS NOT NULL
        GROUP BY year
        ORDER BY year;
    """,
    "Mejores géneros por rating": """
        SELECT genre, ROUND(AVG(rating), 2) AS avg_rating
        FROM movies
        WHERE rating IS NOT NULL
        GROUP BY genre
        ORDER BY avg_rating DESC
    """,
    "Duración promedio por género": """
        SELECT genre, ROUND(AVG(runtime_minutes),0) AS avg_duration
        FROM movies
        WHERE runtime_minutes IS NOT NULL
        GROUP BY genre
        ORDER BY avg_duration DESC;
    """,
    "Top 10 películas con más votos": """
        SELECT title, vote, rating
        FROM movies
        WHERE votes IS NOT NULL
        ORDER BY botes DESC
        LIMIT 10;
    """
}

for name, q in queries.items():
    print(f"\n>>> {name}")
    df = pd.read_sql(q, conn)
    print(df)

conn.close()