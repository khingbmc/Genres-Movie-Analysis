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
    check_y = {}
    for idx, data in df_movie.iterrows():
        check_year = str(data.release_date)[-1:-5:-1][::-1]
        if data.id in director[director_name] and int(check_year)-year<= 9:
            if check_year not in mem:
                mem[check_year] = {}
            for i in json.loads(data.genres):
                if i['name'] not in mem[check_year].keys():
                    mem[check_year][i['name']] = 1
                else:
                    mem[check_year][i['name']] += 1
                count += 1
    for i in mem:
        for j in DATA:
            if DATA[j] not in mem[i]:
                mem[i][DATA[j]] = 0 
    return mem, count

def plotgraph(name, year, check, genres):
    """function plotgraph"""
    line_director = pygal.Line(fill=True, style=NeonStyle)
    director, count = analyse(name, year, {}, 0)
    line_director.title = 'Static Genres of '+name+' directing in %s-%s.'%(str(year), str(year+9))
    line_director.x_labels = map(str, range(year, year+10))
    for i in range(year, year+10):
        if str(i) not in director:
            director[str(i)] = {}
            for j in DATA:
                director[str(i)][DATA[j]] = 0
    keys = sorted([int(x) for x in director.keys()])
    for i in keys:
        for j in director[str(i)]:
            if j not in check:
                check[j] = [director[str(i)][j]]
            else:
                check[j].append(director[str(i)][j])
    for i in check:
        if i == genres:
            line_director.add(i, check[i])
    line_director.render_to_file('..\\..\\web_project\\static\\svg\\director\\%s\\test%s_%s.svg'%(name.replace(' ', '_'), name.replace(' ', '_'), str(year)))

plotgraph(input(), int(input()), {}, input())
