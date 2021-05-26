from flask import request, Flask
import os
import requests
key=os.environ.get('API_KEY')
def search_park_news():
    r = requests.get(f"http://api.mediastack.com/v1/news?countries=us&keywords=theme park&sources=dailynews&access_key={key}")
    return r.json()