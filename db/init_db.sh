#!/bin/bash
set -e
docker exec -i imdb_db psql -U imdb_user -d imdb < "$(dirname "$0")/create_tables.sql"