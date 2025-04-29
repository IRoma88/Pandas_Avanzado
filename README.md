# Proyecto: Análisis de Datos de Películas (IMDB)

## Descripción
En este proyecto, se trabajará con un conjunto de datos que contiene información sobre las 1000 películas mejor valoradas según IMDB. A través de diversos ejercicios, exploraremos el dataset utilizando la librería `pandas` en Python y realizaremos algunos análisis para obtener estadísticas y patrones relevantes.

Los datos incluyen varias características como la duración de las películas, su calificación, los actores, y mucho más.

## Dataset

El dataset utilizado en este proyecto está disponible en formato CSV y contiene la siguiente información:

- **title**: Título de la película.
- **content_rating**: Clasificación por edades de la película.
- **duration**: Duración de la película en minutos.
- **genre**: Género de la película.
- **star_rating**: Puntuación de estrellas de la película.
- **actors_list**: Lista de actores que aparecen en la película.

Puedes acceder al dataset desde este [enlace](https://raw.githubusercontent.com/thechaudharysab/imdb-data-pandas-visualization/master/data/imdb_1000.csv).

## Requisitos

Para ejecutar este proyecto, necesitarás las siguientes librerías de Python:

- **pandas**: Para manipulación y análisis de datos.
- **numpy**: Para operaciones numéricas.

Instala las dependencias usando el siguiente comando:

pip install -r requirements.txt

markdown
Copiar
Editar

## Ejercicios Realizados

1. **Dimensiones del Dataset**:
   - Se almacenó el número de filas y columnas del dataframe en las variables `solucion_1` y `solucion_1b` respectivamente.

2. **Ordenar por Duración**:
   - Se almacenaron las 10 primeras películas ordenadas por duración, desde las más cortas a las más largas.

3. **Valores Faltantes**:
   - Se comprobó si existen valores faltantes en las columnas del dataset y se almacenaron las filas con valores faltantes en la columna 'content_rating' en `solucion_3`.

4. **Comparación de Estrellas por Duración**:
   - Se comparó la media de las puntuaciones de estrellas entre las películas de más de dos horas de duración y las que duran menos de dos horas, y se almacenó la media mayor en `solucion_4`.

5. **Duración Promedio por Género**:
   - Se calculó la duración media para cada género y se almacenó el género con la menor duración promedio en la variable `solucion_5`.

6. **Película con Mayor Puntuación por Género**:
   - Se almacenó el dataframe con la película de mayor puntuación por cada género en `solucion_6`.

7. **Películas con Títulos Duplicados**:
   - Se comprobó si existen títulos duplicados en el dataset, y se almacenó el resultado en `solucion_7` (booleano).

8. **Número de Películas por Actor**:
   - Se creó un diccionario que cuenta cuántas películas tiene cada actor en el dataset, y se ordenó de mayor a menor.

## Archivos del Proyecto

El proyecto contiene los siguientes archivos:

- `imdb_1000.csv`: El archivo con los datos de las películas.
- `titanic_movies_analysis.py`: El archivo con el código de Python para los ejercicios mencionados.
- `requirements.txt`: El archivo que contiene las dependencias necesarias.
- `.gitignore`: El archivo para ignorar archivos no deseados en el control de versiones.

## Cómo ejecutar el proyecto

1. Clona este repositorio a tu máquina local:

   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   ````
2. Navega al directorio del proyecto:

````bash
Copiar
Editar
cd tu_repositorio
````
3. Instala las dependencias necesarias:

````bash
Copiar
Editar
pip install -r requirements.txt
````
3. Ejecuta el script para realizar los análisis:

````bash
Copiar
Editar
python titanic_movies_analysis.py
````
## Contribución
Si deseas contribuir a este proyecto, por favor realiza un fork del repositorio, crea una nueva rama y envía un pull request con tus cambios.

## Licencia
Este proyecto está bajo la Licencia MIT - consulta el archivo LICENSE para más detalles.
