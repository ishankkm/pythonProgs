'''
Created on Dec 21, 2017
@author: ishank

'''

# from urllib.request import Request
from urllib.request import urlopen
# from urllib.error import URLError
import json

def getMovieTitles(substr):
    
    get_url = "https://jsonmock.hackerrank.com/api/movies/search/?Title=" + substr + "&page="
          
    dump = json.loads(urlopen(get_url + "1").read().decode('utf8'))    
    movies, num_pages = dump['data'], dump['total_pages']
    
    for i in range(num_pages - 1):       
        movies += json.loads(urlopen(get_url + str(i+2)).read().decode('utf8'))['data']
    
    return sorted([mov['Title'] for mov in movies])

print(getMovieTitles("spiderman"))