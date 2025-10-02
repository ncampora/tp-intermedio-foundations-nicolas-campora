FROM python:3.9-slim

WORKDIR /app
COPY queries.py .
RUN pip install pandas psycopg2-binary

CMD ["python", "queries.py"]