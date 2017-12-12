import pandas as pd
import json
import pygal
from pygal.style import NeonStyle

with open('..\\..\\web_project\\check.json') as genres:
    DATA = json.load(genres) #import json file and it is data of all genres and id

def read():
    """Read file csv"""
    return pd.read_csv('..\\..\\dataset\\tmdb_5000_movies.csv') #read file csv and return dataframe

def analyse(mem_d, mem_m): #mem_m is marvel revenue , mem_d is DC revenue
    """This is function analyse"""
<<<<<<< HEAD
    count_num = 0 #count_num is check round in loop
=======
    count_num = 0
>>>>>>> 6510efb639140a28012f5144f55e1c6f54a11dd0
    df_movies = read()
    marvel, dc = {}, {} #memory revenue in year
    
    for idx, data in df_movies.iterrows():
        check_year = str(data.release_date)[-1:-5:-1][::-1] #mem year is round
        check = json.loads(data.production_companies) #data production 
        for i in check: #this loop is check DC and Marvel revenue and memory
            production = i['name']
            if production == 'Marvel Studios':
                if check_year == '2016':
                    if count_num == 0:
<<<<<<< HEAD
                        marvel[check_year] = 1831022890 #data is wrong because true revenue is 1831022890 not 2734327385
                    else:
                        continue
                else:
                    
                    if check_year not in marvel:
                        marvel[check_year] = float(data.revenue)
                    else:
                        marvel[check_year] += float(data.revenue)
            
=======
                        marvel[check_year] = 1831022890
                        count_num = 1
                    else:
                        continue
                else:
                    if check_year not in marvel:
                        marvel[check_year] = float(data.revenue)-float(data.budget)
                    else:
                        marvel[check_year] += (float(data.revenue)-float(data.budget))
                count_m += 1
>>>>>>> 6510efb639140a28012f5144f55e1c6f54a11dd0
            elif production == 'DC Comics':
                if check_year not in dc:
                    dc[check_year] = float(data.revenue)
                else:
                    dc[check_year] += float(data.revenue)
<<<<<<< HEAD
    
=======
                count_d += 1
>>>>>>> 6510efb639140a28012f5144f55e1c6f54a11dd0
    dot_m = pygal.Line(x_label_rotation=30, style=NeonStyle)
    dot_m.title = 'Marvel and DC Profit'
    dot_m.x_labels = map(str, range(2008, 2017))
    print(dc, marvel) #print dict

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
    dot_m.add('DC', mem_d) #add in graph
    dot_m.render_to_file('..\\..\\web_project\\static\\svg\\production\\DC_Marvel\\check_benefit.svg')
    #render
analyse([], [])
