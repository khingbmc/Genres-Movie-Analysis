"""Project PSIT Director and Genres Static"""
"""This program is analyse static directing but no popular"""
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


def analyse(director_name, count):
    """function analyse"""
    director, df_movie, df_credits = memory_director() #director is dataframe of dict movies
    check = {} #dictionary movie id and genres
    genres = {} #check genres of director
    
    for idx, data in df_movie.iterrows():
        check_list = [] #this list is memory name of genres
        for i in json.loads(data.genres):
            check_list.append(i['name'])
        check[data.id] = check_list #memory movie id and data is list of genres in that movies
    
    for i in director.keys(): #This loop is count num of genres is director directing
        if i == director_name:
            for j in director[i]:
                for k in check[j]:
                    count += 1 #count is num of all genres is directing
                    if k not in genres:
                        genres[k] = 1
                    else:
                        genres[k] += 1
    return genres, count
    """genres is static genres of director
    and director_name is input name director"""

def plotgraph(name, genres_sort, count):
    """function plotgraph"""
    pie_director = pygal.Bar(fill=True, interpolate='cubic', style=NeonStyle)
    genres, count = analyse(name, 0)
    pie_director.title = 'Static Genres of '+name+' directing.(%)'
    
    for i in genres:
        count += genres[i] #memory number of all genres
    
    for i in genres: #This loop is sort genres
        if genres[i] not in genres_sort:
            genres_sort[genres[i]] = [i]
        else:
            genres_sort[genres[i]].append(i)
    
    keys = sorted(check.keys())
    #keys is in genres_sort   
    for i in keys:
        for j in genres_sort[i]:
            pie_director.add(j, round(i*100/count*2, 2))
    
    pie_director.render_to_file('..\\..\\web_project\\static\\svg\\director\\%s\\director_genres.svg'%(name.replace(' ', '_')))
    #render
plotgraph(input(), {}, 0)
