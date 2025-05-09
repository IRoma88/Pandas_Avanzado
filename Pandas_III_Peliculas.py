# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

"""En este proyecto vamos a trabajar con otro de los datasets más usados para aprender, contiene datos de las 1000 películas mejor valoradas segun IMDB.

La siguiente url contienen el csv para crear el dataframe : https://raw.githubusercontent.com/thechaudharysab/imdb-data-pandas-visualization/master/data/imdb_1000.csv

Puedes usar la url directamente para crear el dataframe.
"""

movies = pd.read_csv('https://raw.githubusercontent.com/thechaudharysab/imdb-data-pandas-visualization/master/data/imdb_1000.csv')

"""Comprueba las 5 primeras filas para confirmar que el moviesframe se ha creado correctamente."""

movies.head()

"""#Ejercicio 1

Almacena en la variable solucion_1 el número de filas y en la variable solucion_1b el número de columnas.
"""

solucion_1=movies.shape[0]

solucion_1b=movies.shape[1]

print(solucion_1, solucion_1b)

"""#Ejercicio 2

Almacena en la variable solucion_2 las 10 primeras filas del dataframe ordenado según la duración de las películas de más corta a más larga.
"""

solucion_2=movies.sort_values('duration').head(10)

solucion_2

"""#Ejercicio 3

Comprueba cuantos valores faltan en cada columna
"""

movies.isnull().sum()

"""Almacena en la variable solucion_3 las filas donde faltan valores.

"""

solucion_3=movies[movies['content_rating'].isnull()]

solucion_3

"""#Ejercicio 4

Compara la media de estrellas en las películas que duran dos horas o más frente a las que duran menos de dos horas.

Almacena en la variable solucion_4 la media de estrellas mayor, redondeada a dos decimales.
"""

print('Avg. star rating for movies 2 hours or longer: ', movies[movies['duration'] >= 120]['star_rating'].mean(),
 '\nAvg. star rating for movies shorter than 2 hours: ', movies[movies['duration'] < 120]['star_rating'].mean())

solucion_4=round(movies[movies['duration'] >= 120]['star_rating'].mean(),2)

solucion_4

"""#Ejercicio 5

Calcula la duración media para cada género. Almacena como cadena de  texto en la variable solucion_5 el género con la media de duración más baja.
"""

movies[['duration','genre']].groupby('genre').mean()

"""Escribe tu respuesta en la variable solucion_5.

Tu respuesta deberá ser un string con el nombre del género.
"""

solucion_5='History'

"""# Ejercicio 6

Almacena en la variable solucion_6 el dataframe resultante de buscar la pelicula con mayor puntuación de estrellas para cada género.
"""

solucion_6=movies.sort_values('star_rating', ascending=False).groupby('genre')[['title','star_rating']].first()

solucion_6

"""#Ejercicio 7

Comprueba si existen películas con el mismo título. Y de ser así ¿Alguna está duplicada por error? Responde esta pregunta con un booleano en la variable solucion_7
"""

result = movies[movies['title'].isin(movies[movies.duplicated(['title'])]['title'])]
result.sort_values('title')

solucion_7=False

"""#Ejercicio 8

Crea un diccionario 'actor_dict' cuya clave sea el nombre de los actores y su valor el número de películas del dataframe donde aparece. Ordenalo de mayor a menor según el número de películas en las que aparece el actor/actriz.

**Pista: ten en cuenta que antes de crear el diccionario deberas tratar los datos de la columna 'actor_list'**
"""

def repp(string):
    return string.replace("[","").replace("]","").replace("u'","").replace("',",",")[:-1]
#Apply that function to every entry
movies_series = movies['actors_list'].apply(repp)

#Declare a list to store the split values
actors_list = []
for movie_actors in movies_series:
    actors_list.append([e.strip() for e in movie_actors.split(',')])

#Declare a dictionary and see if the actor name key exist and then count accordingly.
actor_dict = {}
for actor in actors_list:
    for a in actor:
        if a in actor_dict:
            actor_dict[a] +=1
        else:
            actor_dict[a] = 1

actor_dict = sorted(actor_dict.items(), key=lambda x: x[1],reverse=True)

actor_dict


print(hashlib.sha256(str(solucion_5).encode()).hexdigest())
print(hashlib.sha256(str(solucion_6).encode()).hexdigest())
print(hashlib.sha256(str(solucion_7).encode()).hexdigest())
