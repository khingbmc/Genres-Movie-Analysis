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


def analyse(year):
    """This function is analyse data"""
    #1916-2015
    df_1, df_2 = read()
    df_1.set_index('id', inplace=True) #set index
    df_2.set_index('movie_id', inplace=True)
    check, popularity, count = {}, 0, 0
    for idx, data in df_1.iterrows():
        count += 1
        if str(data.release_date)[len(str(data.release_date))-4:] == year:
           check_genres = json.loads(data.genres)
           for i in check_genres:
            if i['name'] not in check:
                check[i['name']] = float(data.popularity)
            else:
                check[i['name']] += float(data.popularity)
    count1 = 1
    for i in check.keys():
        count1 += 1
        check[i] = check[i]/count*100
    return check, count1


def plotgraph(year, check):
    """This function is Plot graph"""
    memory, count1 = analyse(year)
    plot_bar, check1 = pygal.Bar(fill=True, interpolate='cubic', style=NeonStyle), 0
    plot_bar.title = 'Genres Satic in '+year
    for i in memory:
        check += memory[i]*count1
    check_mem = [memory[x] for x in memory.keys()]
    check_mem = sorted(check_mem)
    for j in check_mem:
        for i in memory:
            if memory[i] == j:
                plot_bar.add(i, round(memory[i]*count1/check*100, 3))
    plot_bar.render_to_file('../../web_project/static/svg/year/%s.svg'%(str(year)))
plotgraph(input(), 0)
