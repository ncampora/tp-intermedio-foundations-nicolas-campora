#!/bin/bash
set -e

echo "Levantando PostgreSQL"
docker-compose -f docker/docker-compose.yml up -d

echo "Esperando 5s"
sleep 5

echo "Creando tablas"
./db/init_db.sh

echo "Cargando dataset"
docker run --rm --network docker_default -v "$(pwd)/data:/data" imdb_loader

echo "Ejecutando consultas"
docker run --rm --network docker_default imdb_queries

echo "Proceso end2end completado"