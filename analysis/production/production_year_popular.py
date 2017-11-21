import pandas as pd
import json
import pygal
from pygal.style import CleanStyle

with open('..\\check.json') as genres:
    DATA = json.load(genres) #import json file

def read():
    """Read file csv"""
    return pd.read_csv('..\\..\\dataset\\tmdb_5000_movies.csv')

def analyse(production, year, mem):
    """This function is analyse data"""
    count = 0
    df_movie = read()
    for idx, data in df_movie.iterrows():
        for i in json.loads(data.production_companies):
            if i['name'] == production:
                mem[str(data.original_title)] = int(data.revenue)-int(data.budget)
    print(mem)

                    

def plotgraph(production, year):
    """This function is plotgraph"""
    memory, count = analyse(production, year, {})
    bar = pygal.Bar(fill=True, interpolate='cubic', style=CleanStyle)
    bar.title = production+' genres popularity static in '+str(year-5)+'-'+str(year)
    for i in memory.keys(): 
        bar.add(i, round(memory[i]/count*100, 3))
    bar.render_to_file('..\\..\\web_project\\static\\svg\\%s\\%s_%s.svg'%(production.replace(' ', '_'), production.replace(' ', '_'), year))
plotgraph(input(), int(input()))
