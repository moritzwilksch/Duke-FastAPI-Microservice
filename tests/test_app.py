import pytest
import requests

from src.app import scrape_restaurants_and_hours

def test_website_online():
    URL = "https://app.studentaffairs.duke.edu/dining/menus-hours/"
    r = requests.get(URL)

    assert r.ok

def test_html_selectors_working():
    with open("tests/test_dump.html") as f:
        html = f.read()


    result = scrape_restaurants_and_hours(html)
    # print(result)

    assert len(result) > 0
    