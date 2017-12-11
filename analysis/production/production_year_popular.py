import pandas as pd
import json
import pygal
from pygal.style import NeonStyle

with open('..\\..\\web_project\\check.json') as genres:
    DATA = json.load(genres) #import json file

def read():
    """Read file csv"""
    return pd.read_csv('..\\..\\dataset\\tmdb_5000_movies.csv')

def analyse(production, year, mem):
    """This function is analyse data"""
    count = 0
    df_movie = read()
    for idx, data in df_movie.iterrows():
        check_year = str(data.release_date)[-1:-5:-1][::-1]
        for i in json.loads(data.production_companies):
            if i['name'] == production and 0 <= int(check_year)-year <= 5:
                for i in json.loads(data.genres):
                    if i['name'] not in mem.keys():
                        mem[i['name']] = float(data.popularity)
                        count += float(data.popularity)
                    else:
                        mem[i['name']] += float(data.popularity)
                        count += float(data.popularity)
                    
    return mem, count

def plotgraph(production, year, check):
    """This function is plotgraph"""
    memory, count = analyse(production, year, {})
    bar = pygal.Bar(fill=True, interpolate='cubic', style=NeonStyle)
    bar.title = production+' genres popularity static in '+str(year)+'-'+str(year+5)
    check_mem = [memory[x] for x in memory.keys()]
    check_mem = sorted(check_mem)
    for i in memory.keys():
        if memory[i] not in check:
            check[memory[i]] = [i]
        else:
            check[memory[i]].append(i)
    keys = sorted(check.keys())
    for i in keys:
        for j in check[i]:
            bar.add(j, round(i/count*100, 3))
    bar.render_to_file('..\..\web_project\static\svg\production\%s\%s_%s.svg'%(production.replace(' ', '_'), production.replace(' ', '_'), year))
plotgraph(input(), int(input()), {})
