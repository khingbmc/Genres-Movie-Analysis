"""Project PSIT Director and Genres Static"""
import json
import pandas as pd
import pygal
import os
from pygal.style import NeonStyle

with open('..\\..\\web_project\\check.json') as genres:
    DATA = json.load(genres) #import json file


def read():
    """function read file csv"""
    return pd.read_csv('..\\..\\dataset\\tmdb_5000_movies.csv'),\
    pd.read_csv('..\\..\\dataset\\tmdb_5000_credits.csv')


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

def plotgraph(name, check, count):
    """function plotgraph"""
    pie_director = pygal.Bar(fill=True, interpolate='cubic', style=NeonStyle)
    genres, count = analyse(name, 0)
    pie_director.title = 'Static Genres of '+name+' directing.(%)'
    for i in genres:
        count += genres[i]
    for i in genres:
        if genres[i] not in check:
            check[genres[i]] = [i]
        else:
            check[genres[i]].append(i)
    mem = sorted(check.keys())
    for i in mem:
        for j in check[i]:
            pie_director.add(j, round(i*100/count*2, 2))
    pie_director.render_to_file('..\\..\\web_project\\static\\svg\\director\\%s\\director_genres.svg'%(name.replace(' ', '_')))
plotgraph(input(), {}, 0)
