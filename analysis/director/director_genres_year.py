"""Project PSIT Director and Genres Static"""
"""This program is analyse static of director is directing in start year to year+9"""
import json
import pandas as pd
import pygal
import os
from pygal.style import NeonStyle

with open('..\\..\\web_project\\check.json') as genres:
    DATA = json.load(genres) #import json file(json file is all name genres)


def read():
    """function read file csv"""
    return pd.read_csv('..\\..\\dataset\\tmdb_5000_movies.csv'),\
    pd.read_csv('..\\..\\dataset\\tmdb_5000_credits.csv')
    #first it is a all dataframe information and second is detail in production 

def memory_director():
    """This function is memory movie of director is directing"""
    df_movie, df_credits = read() #read csv
    director_movie = {} #This dict is memory name director and his directing movie
    
    for idx, data in df_credits.iterrows(): #idx is index of rows and data is data in rows
        for i in json.loads(data.crew): #data.crew is detail duty
            if i['job'] == 'Director':
                if i['name'] not in check_dict:
                    director_movie[i['name']] = [data.movie_id]
                else:
                    director_movie[i['name']].append(data.movie_id)
        '''This loop is check if i keys job is equal director memory movies name and 
        name director in dict(director_movie)'''
    
    return director_movie, df_movie, df_credits #return dataframe and dict(memory director and movies)


def analyse(director_name, year, mem, count_genres):
    """function analyse"""
    director, df_movie, df_credits = memory_director() #director is memory name director and movie
    
    for idx, data in df_movie.iterrows():
        check_year = str(data.release_date)[-1:-5:-1][::-1] #check_year is year of film
        if data.id in director[director_name] and 0 <= int(check_year)-year <= 9: #director_name is name of director analyse
            
            for i in json.loads(data.genres): #This loop is memory number of genres is director directing
                if i['name'] not in mem:
                    mem[i['name']] = 1
                    count_genres += 1 #count_genres is num of all genres
                else:
                    mem[i['name']] += 1
                    count_genres += 1 #mem is memory num of genres is director is directing
    
    return mem, count_genres #return memory num of genres and number of all genres

def plotgraph(name, year):
    """function plotgraph"""
    pie_director = pygal.Bar(fill=True, interpolate='cubic', style=NeonStyle)
    director, count = analyse(name, year, {}, 0) #name is name director year is start year
    pie_director.title = 'Static Genres of '+name+' directing in %s-%s.'%(str(year), str(year+9))
    director_sort = {} #dict sort num of popular director directing genres
    for i in director:
        if director[i] not in director_sort:
            director_sort[director[i]] = [i]
        else:
            director_sort[director[i]].append(i)
    keys = sorted(check.keys()) #keys of dict director sort
    
    for j in keys:
        for i in director_sort[j]:
            pie_director.add(i, round(j/count*100, 3))
    pie_director.render_to_file('..\\..\\web_project\\static\\svg\\director\\%s\\%s_%s.svg'%(name.replace(' ', '_'), name.replace(' ', '_'), str(year)))
    # render
plotgraph(input(), int(input()))
