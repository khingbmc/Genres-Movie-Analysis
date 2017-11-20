import pandas as pd
import json
import pygal
from pygal.style import NeonStyle

with open('..\\check.json') as genres:
    DATA = json.load(genres) #import json file

def read():
    """Read file csv"""
    return pd.read_csv('..\\..\\dataset\\tmdb_5000_movies.csv')

def analyse(production, year, mem):
    """This function is analyse data"""
    df_movie = read()
    for idx, data in df_movie.iterrows():
        check_year = str(data.release_date)[-1:-5:-1][::-1]
        for i in json.loads(data.production_companies):
            if i['name'] == production and year == int(check_year):
                for i in json.loads(data.genres):
                    if i['name'] not in mem:
                        mem[i['name']] = float(data.popularity)
                    else:
                        mem[i['name']] += float(data.popularity)
    return mem
                    

def plotgraph(production, year):
    """This function is plotgraph"""
    memory = analyse(production, year, {})
    pie = pygal.Pie()
    pie.title = production+' genres popularity static in '+year
    for i in memory.keys():
        pie.add(i, round(memory[i], 3))
    pie.render_to_file('static/svg/%s_%s.svg'%(production, year))
plotgraph(input(), int(input()))
