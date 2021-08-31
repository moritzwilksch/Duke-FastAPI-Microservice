from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
import random 

app = FastAPI()


def retrieve_data():
    """Make HTTP request and return its contents"""

    URL = "https://app.studentaffairs.duke.edu/dining/menus-hours/"
    r = requests.get(URL)
    
    # with open('dump.html', 'w') as f:
    #     f.write(r.text)

    return r.content


def scrape_restaurants_and_hours(data):
    """Extract list of (rest_name, hours) tuples from html page"""
    
    soup = BeautifulSoup(data, 'lxml')

    l = soup.select("tr")

    restaurants = []
    for tr in l:
        link = tr.select('td a')
        hours = tr.select('td#schedule_time_data_day_one')
        if link and hours:
            restaurants.append((link[0].contents[0], "".join(x.strip() for x in hours[0].contents if isinstance(x, str))))
    
    return restaurants


@app.get("/")
async def root():
    data = retrieve_data()
    restaurants = scrape_restaurants_and_hours(data)

    open_restaurants = [r for r in restaurants if r[1] != 'Closed']

    tup = random.choice(open_restaurants)
    

    return {"recommendation": {'restaurant': tup[0], 'todays_hours': tup[1]}}


@app.get("/all-restaurants")
async def root():
    data = retrieve_data()
    restaurants = scrape_restaurants_and_hours(data)

    return {"recommendation": {'all_restaurants': restaurants}}


@app.get("/open-restaurants")
async def root():
    data = retrieve_data()
    restaurants = scrape_restaurants_and_hours(data)

    open_restaurants = [r for r in restaurants if r[1] != 'Closed']
    return {"recommendation": {'open_restaurants': open_restaurants}}


@app.get("/status")
def status():
    return {'msg': "I'm alive!!"}