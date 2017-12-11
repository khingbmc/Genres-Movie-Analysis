import pandas as pd
import json
import pygal
from pygal.style import NeonStyle

with open('..\\..\\web_project\\check.json') as genres:
    DATA = json.load(genres) #import json file

def read():
    """Read file csv"""
    return pd.read_csv('..\\..\\dataset\\tmdb_5000_movies.csv')

def analyse(count_d, count_m, mem_d, mem_m):
    """This is function analyse"""
    df_movies = read()
    marvel, dc = {}, {}
    for idx, data in df_movies.iterrows():
        check_year = str(data.release_date)[-1:-5:-1][::-1]
        check = json.loads(data.production_companies)
        for i in check:
            production = i['name']
            if production == 'Marvel Studios':
                if check_year not in marvel:
                    marvel[check_year] = float(data.revenue)-float(data.budget)
                else:
                    marvel[check_year] += (float(data.revenue)-float(data.budget))
                count_m += 1
            elif production == 'DC Comics':
                if check_year not in dc:
                    dc[check_year] = float(data.revenue)-float(data.budget)
                else:
                    dc[check_year] += (float(data.revenue)-float(data.budget))
                count_d += 1
    dot_m = pygal.Line(x_label_rotation=30, style=NeonStyle)
    dot_m.title = 'Marvel and DC Profit'
    dot_m.x_labels = map(str, range(2008, 2017))
    print(dc, marvel)
    for i in range(2008, 2017):
        if str(i) in marvel:
            mem_m.append(marvel[str(i)])
        else:
            mem_m.append(None)
        if str(i) in dc:
            mem_d.append(dc[str(i)])
        else:
            mem_d.append(None)
    dot_m.add('Marvel', mem_m)
    dot_m.add('DC', mem_d)
    dot_m.render_to_file('..\\..\\web_project\\static\\svg\\production\\DC_Marvel\\check_benefit.svg')
analyse(0, 0, [], [])
