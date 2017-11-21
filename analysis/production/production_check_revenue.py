import pandas as pd
import json
import pygal
from pygal.style import CleanStyle

with open('..\\check.json') as genres:
    DATA = json.load(genres) #import json file

def read():
    """Read file csv"""
    return pd.read_csv('..\\..\\dataset\\tmdb_5000_movies.csv')

def analyse(production, mem):
    """This function is analyse data"""
    count = 0
    df_movie = read()
    for idx, data in df_movie.iterrows():
        for i in json.loads(data.production_companies):
            if i['name'] == production:
                mem[str(data.original_title)] = int(data.revenue)-int(data.budget)
    count, memory = 0, {}
    for _ in range(3):
        for i in mem:
            if mem[i] >= count and (i not in memory):
                check = i
                count = mem[i]
        count = 0
        memory[check] = mem[check]
    with open('profit_%s.json'%production, 'w') as f:
        json.dump(memory, f)
analyse(input(), {})