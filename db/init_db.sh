#!/bin/bash
set -e
docker exec -i imdb_db psql -U imdb_user -d imdb < create_tables.sql