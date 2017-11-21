import pandas as pd
import json
import pygal
from pygal.style import NeonStyle

with open('check.json') as genres:
    DATA = json.load(genres) #import json file

def read():
    """Read file csv"""
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

def plotgraph(name_director):
    """function plot graph"""
    popular_genres, count = sorted(analyse(name_director)), 0
    chart = pygal.Bar(fill=True, interpolate='cubic', style=NeonStyle)
    chart.title = name_director+' Static Popular Genres for his Directing (%)'
    for i in popular_genres.keys():
        count += popular_genres[i]
    chart.x_labels = map(str, popular_genres.keys())
    chart.add('popularity', [round(popular_genres[x]/count*100, 4) for x in popular_genres.keys()])
    chart.render_to_file('../web_project/static/svg/popular_d.svg')
