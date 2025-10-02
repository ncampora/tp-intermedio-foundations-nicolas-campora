# ncampora-tp-intermedio-foundations-nicolas-campora

TP Final de la sección Foundations del Módulo 1 de la Diplomatura en Cloud Data Engineering del ITBA

---

## Resolución de los ejercicios

### Ejercicio 1: Elección de dataset y preguntas

Se eligió el dataset [IMDb Top 1000 Movies and TV Shows](https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows).  
La explicación del dataset y las preguntas de negocio se encuentran en [`docs/dataset.md`](docs/dataset.md).

---

### Ejercicio 2: Crear container de la DB

Se utilizó [`docker/docker-compose.yml`](docker/docker-compose.yml) para crear un contenedor de PostgreSQL 12.7 expuesto en el puerto estándar 5432.

---

### Ejercicio 3: Script para creación de tablas

Se creó [`db/create_tables.sql`](db/create_tables.sql) con la definición de la tabla `movies`, y [`db/init_db.sh`](db/init_db.sh) para ejecutar este script dentro del contenedor.

---

### Ejercicio 4: Popular la base de datos

Se implementó [`docker/loader/load_data.py`](docker/loader/load_data.py) para cargar el dataset en PostgreSQL, y [`docker/loader/Dockerfile`](docker/loader/Dockerfile) para construir la imagen que lo corre.

---

### Ejercicio 5: Consultas a la base de datos

Se desarrolló [`docker/queries/queries.py`](docker/queries/queries.py) con 5 consultas SQL de análisis de negocio, y [`docker/queries/Dockerfile`](docker/queries/Dockerfile) para construir la imagen que lo corre.

---

### Ejercicio 6: Documentación y ejecución end-to-end

Se creó el script [`run_all.sh`](run_all.sh) que automatiza todo el proceso en conjunto con la documentación el proyecto.

---

## Estructura del proyecto

```plaintext
imdb-project/
├── data/
│   └── imdb_top_1000.csv
├── db/
│   ├── create_tables.sql
│   └── init_db.sh
├── docker/
│   ├── loader/
│   │   ├── Dockerfile
│   │   └── load_data.py
│   ├── queries/
│   │   ├── Dockerfile
│   │   └── queries.py
│   └── docker-compose.yml
├── docs/
│   └── dataset.md
├── run_all.sh
└── README.md
```

## Ejecución end-to-end

### Construcción de las imágenes de load y queries

Tener instalado **Docker** y **Docker Compose**.

```bash
docker build -t imdb_loader ./docker/loader
docker build -t imdb_queries ./docker/queries
```

---

### Ejecución del pipeline completo

```bash
./run_all.sh
```

El script `run_all.sh` levanta el contenedor de PostgreSQL, crea la tabla, carga el dataset y ejecuta las consultas, mostrando los resultados en consola.

---

### Ejemplo de salida

```text
>>> Top 10 directores con mejor rating
             director  avg_rating
0      Frank Darabont        8.95
1      Irvin Kershner        8.70
2      Lana Wachowski        8.70
...

>>> Películas por año
   year  cantidad
0  1920         1
1  1921         1
...
```
