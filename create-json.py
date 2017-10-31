import pandas as pd
import json as j
df = pd.read_csv('dataset\\tmdb_5000_movies.csv')
check = {}
for i in df['genres']:
    i = j.loads(i)
    for k in i:
        if k['id'] not in check:
            check[k['id']] = k['name']
with open('check.json', 'w') as f:
    j.dump(check, f)