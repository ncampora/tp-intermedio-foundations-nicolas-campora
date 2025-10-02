FROM python:3.9-slim

WORKDIR /app
COPY load_data.py .
RUN pip install pandas psycopg2-binary
CMD ["python", "load_data.py"]