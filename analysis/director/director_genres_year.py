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


def analyse(director_name, year, mem, count):
    """function analyse"""
    director, df_movie, df_credits = memory_director()
    for idx, data in df_movie.iterrows():
        check_year = str(data.release_date)[-1:-5:-1][::-1]
        if data.id in director[director_name] and 0 <= year - int(check_year) <= 5:
            for i in json.loads(data.genres):
                if i['name'] not in mem:
                    mem[i['name']] = float(data.popularity)
                    count += float(data.popularity)
                else:
                    mem[i['name']] += float(data.popularity)
                    count += float(data.popularity)
    return mem, count

def plotgraph(name, year):
    """function plotgraph"""
    pie_director = pygal.Pie(fill=True, interpolate='cubic', style=NeonStyle)
    director, count = analyse(name, year, {}, 0)
    pie_director.title = 'Static Genres of '+name+' directing in %s-%s.'%(str(year-5), str(year))
    for i in director:
        pie_director.add(i, round(director[i]/count*100, 3))
    pie_director.render_to_file('../../web_project/static/svg/director/%s/%s_%s.svg'%(name, name.replace(' ', '_'), str(year)))
plotgraph(input(), int(input()))
