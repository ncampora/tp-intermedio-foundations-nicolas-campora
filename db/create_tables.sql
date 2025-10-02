CREATE TABLE IF NOT EXISTS movies (
    movie_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    year INT,
    genre VARCHAR(100),
    director VARCHAR(255),
    runtime_minutes INT,
    rating NUMERIC(3, 1),
    votes INT
)