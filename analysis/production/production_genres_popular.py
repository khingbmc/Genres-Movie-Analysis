import pandas as pd
import pygal
import json
from pygal.style import NeonStyle
from functools import reduce

def read():
    return pd.read_csv('..\\..\\dataset\\tmdb_5000_movies.csv')


def analyse(name, genres_pop):
    """function pull data and analyse"""
    df_movie = read()
    for idx, data in df_movie.iterrows():
        for i in json.loads(data.production_companies):
            if name == i['name']:
                for k in json.loads(data.genres):
                    if k['name'] in genres_pop:
                        genres_pop[k['name']] += data.popularity
                    else:
                        genres_pop[k['name']] = data.popularity #memory data popular in dictionary
    count = reduce(lambda x, y:x+y, [genres_pop[x] for x in genres_pop.keys()])
    return genres_pop, count


def plotgraph(name, mem):
    genres_pop, count = analyse(name, {})
    chart = pygal.Bar(fill=True, interpolate='cubic', style=NeonStyle)
    chart.title = name+' Static Popular Genres (%)'
    for i in genres_pop.keys():
        if genres_pop[i] not in mem:
            mem[genres_pop[i]] = [i]
        else:
            mem[genres_pop[i]].append(i)
    keys = sorted(mem.keys())
    for i in keys:
        for j in mem[i]:
            chart.add(j, round(i*100/count, 2))
    chart.render_to_file('..\\..\\web_project\\static\\svg\\production\\%s\\%s_genrespopular.svg'%(name.replace(' ', '_'), name.replace(' ', '_')))
plotgraph(input(), {})