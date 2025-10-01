CREATE TABLE movies (
    movie_id SERIAL PRIMARY EY,
    title VARCHAR(255) NOT NULL,
    year INT,
    genre VARCHAR(100),
    director VARCHAR(255)
    runtime_minutes INT,
    rating NUMERIC(3, 1),
    votes INT
)