import pandas as pd
import json
import pygal
from pygal.style import NeonStyle

with open('..\\..\\web_project\\check.json') as genres:
    DATA = json.load(genres) #import json file(json file is all name genres)

def read():
    """Read file csv and return dataframe"""
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


def analyse(name):
    """This function is analyse popular genres of director""" 
    director, df_movie, df_credits = memory_director() #variable director is name movie of director is directing
    genres_popular = {} #This variable is memory popularity of genres analytic
    
    for idx, data in df_movie.iterrows(): #This loop is in rows movie information 
        if data.id in director[name]: """data.id is name id movies and is condition is 
        check name of directing and name movies"""
            for i in json.loads(data.genres): #data.genres is genres of movie id
                if i['name'] in genres_popular:
                    genres_popular[i['name']] += data.popularity #data.popularity is num of popular in movie style
                else:
                    genres_popular[i['name']] = data.popularity
    
    return genres_popular #return genres and movie polarity

def plotgraph(name_director, popular_sort):
    """This function is plot this graph genres popular of director"""
    popular_genres, num_popular = analyse(name_director), 0
    chart = pygal.Bar(fill=True, interpolate='cubic', style=NeonStyle)
    chart.title = name_director+' Static Popular Genres for his Directing (%)'
    
    for i in popular_genres.keys(): #This loop is count all num popular
        num_popular += popular_genres[i]
    
    for i in popular_genres.keys(): #This loop is sort data because use data is sort in graph
        if popular_genres[i] not in popular_sort:
            popular_sort[popular_genres[i]] = [i]
        else:
            popular_sort[popular_genres[i]].append(i)
    
    keys = sorted(popular_sort.keys()) #keys is list memory keys in popular_sort
    
    for i in keys:
        for j in check[i]:
            chart.add(j, round(i/num_popular*100, 4)) #plot graph
    chart.render_to_file('..\\..\\web_project\\static\\svg\\director\\%s\\popular_d.svg'%(name_director.replace(' ', '_')))
    # render
plotgraph(input(), {})
