from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
import random 

app = FastAPI()


def retrieve_data():
    URL = "https://app.studentaffairs.duke.edu/dining/menus-hours/"
    r = requests.get(URL)
    
    # with open('dump.html', 'w') as f:
    #     f.write(r.text)

    return r.content




@app.get("/")
async def root():
    soup = BeautifulSoup(retrieve_data(), 'lxml')

    # l = soup.select("td#schedule_place_data a")

    # restaurant_names = []
    # for a in l:
    #     restaurant_names.append(a.contents)

    # l = soup.find_all("td", id='schedule_time_data_day_one')

    # hours = []
    # for x in l:
    #     hours.append(x.contents)

    # print(len(restaurant_names), len(hours))

    l = soup.select("tr")

    restaurants = []
    for tr in l:
        link = tr.select('td a')
        hours = tr.select('td#schedule_time_data_day_one')
        if link and hours:
            restaurants.append((link[0].contents[0], "".join(x.strip() for x in hours[0].contents if isinstance(x, str))))
    
    print(restaurants)

    open_restaurants = [r for r in restaurants if r[1] != 'Closed']

    tup = random.choice(open_restaurants)
    

    return {"recommendation": {'restaurant': tup[0], 'todays_hours': tup[1]}}