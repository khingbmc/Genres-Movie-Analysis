import pandas as pd
import json
import numpy as np
"""Project PSIT"""
with open('check.json') as genres:
    DATA = json.load(genres) #import json file


def read():
    """Read file csv"""
    return pd.read_csv('dataset\\tmdb_5000_movies.csv'),\
    pd.read_csv('dataset\\tmdb_5000_credits.csv')


def analyse():
    """function analyse"""
    memory = {}
    df_1, df_2 = read()
    df_id = df_1.id #id movie
    df_1.set_index('id', inplace=True) #set index
    df_2.set_index('movie_id', inplace=True)
    df_production = df_1.production_companies #dataframe production
    for i in df_id:
        for j in json.loads(df_production[i]):
            if j['name'] not in memory:
                memory[j['name']] = {}
    for idx, data in df_1.iterrows():#select row
        for i in json.loads(data.production_companies):
            genres = {}
            for j in json.loads(data.genres):
                genres[j['id']] = 1
            for j in genres.keys():
                if j not in memory[i['name']]:
                    memory[i['name']][j] = 1
                else:
                    memory[i['name']][j] += 1
    print(memory)
analyse()