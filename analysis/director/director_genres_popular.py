import pandas as pd
import json
import pygal
from pygal.style import NeonStyle

with open('..\\..\\web_project\\check.json') as genres:
    DATA = json.load(genres) #import json file

def read():
    """Read file csv"""
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


def analyse(name):
    director, df_movie, df_credits = memory_director()
    check1 = {}
    for idx, data in df_movie.iterrows():
        if data.id in director[name]:
            for i in json.loads(data.genres):
                if i['name'] in check1:
                    check1[i['name']] += data.popularity
                else:
                    check1[i['name']] = data.popularity
    return check1 #return genres and movie polarity

def plotgraph(name_director, check):
    """function plot graph"""
    popular_genres, count = analyse(name_director), 0
    chart = pygal.Bar(fill=True, interpolate='cubic', style=NeonStyle)
    chart.title = name_director+' Static Popular Genres for his Directing (%)'
    for i in popular_genres.keys():
        count += popular_genres[i]
    for i in popular_genres.keys():
        if popular_genres[i] not in check:
            check[popular_genres[i]] = [i]
        else:
            check[popular_genres[i]].append(i)
    keys = sorted(check.keys())
    for i in keys:
        for j in check[i]:
            chart.add(j, round(i/count*100, 4))
    chart.render_to_file('..\\..\\web_project\\static\\svg\\director\\%s\\popular_d.svg'%(name_director.replace(' ', '_')))
plotgraph(input(), {})
