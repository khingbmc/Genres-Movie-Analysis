"""Project PSIT Director and Genres Static"""
import json
import pandas as pd
import pygal
from pygal.style import NeonStyle

with open('check.json') as genres:
    DATA = json.load(genres) #import json file


def read():
    """function read file csv"""
    return pd.read_csv('..\\dataset\\tmdb_5000_movies.csv'),\
    pd.read_csv('..\\dataset\\tmdb_5000_credits.csv')


def memory_director():
    """function analyse data"""
    df_movie, df_credits = read() #read csv
    check_dict = {}
    for idx, data in df_credits.iterrows():
        for i in json.loads(data.crew):
            if i['job'] == 'Director':
                if i['name'] not in check_dict:
                    check_dict[i['name']] = [data.movie_id]
                else:
                    check_dict[i['name']].append(data.movie_id)
    return check_dict, df_movie, df_credits


def analyse(director_name, count):
    """function analyse"""
    director, df_movie, df_credits = memory_director()
    check = {} #dictionary movie id and genres
    genres = {} #check genres of director
    for idx, data in df_movie.iterrows():
        check_list = []
        for i in json.loads(data.genres):
            check_list.append(i['name'])
        check[data.id] = check_list
    for i in director.keys():
        if i == director_name:
            for j in director[i]:
                for k in check[j]:
                    count += 1
                    if k not in genres:
                        genres[k] = 1
                    else:
                        genres[k] += 1
    return genres, count
    """genres is static genres of director
    and director_name is input name director"""

def plotgraph(name):
    """function plotgraph"""
    pie_director = pygal.Pie(fill=True, interpolate='cubic', style=NeonStyle)
    genres, count = analyse(name, 0)
    pie_director.title = 'Static Genres of '+name+' directing.(%)'
    for i in genres:
        pie_director.add(i, round(genres[i]/count*100, 3))
    pie_director.render_to_file('director_genres.svg')
plotgraph(input())
