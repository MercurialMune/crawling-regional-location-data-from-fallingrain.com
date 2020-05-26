#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
from string import ascii_uppercase

county_codes = []
list_county_dict = []
url = "http://fallingrain.com/world/KE/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find('ul')
links = results.find_all('a')
for link in links:
    try:
        county_name = link.contents[0]
        county_code = link['href'].replace("/", "")[-2:]
        county_dict = {county_name:county_code}
        list_county_dict.append(county_dict)
    except:
        pass
big_county_dict = {}
for d in list_county_dict:
    big_county_dict.update(d)
all_places = {}
for x in big_county_dict:
    try:
        county_places = []
        for c in ascii_uppercase:
            try:
                url = f"http://fallingrain.com/world/KE/{big_county_dict[x]}/a/{c}/"
                page = requests.get( url )
                soup = BeautifulSoup( page.content, 'html.parser' )
                results = soup.find( 'table' )
                links = results.find_all( 'a' )
                for link in links:
                    county_places.append( link.contents[0] )
            except AttributeError:
                pass
        if len(county_places)==0:
            try:
                url = f"http://fallingrain.com/world/KE/{big_county_dict[x]}/"
                page = requests.get( url )
                soup = BeautifulSoup( page.content, 'html.parser' )
                results = soup.find_all( 'table' )[1]
                links = results.find_all( 'a' )
                for link in links:
                    county_places.append( link.contents[0] )
            except AttributeError:
                pass
        final_county_dict = {x:county_places}            
        all_places.update(final_county_dict)
    except:
        pass

import json
with open('result.json', 'w') as fp:
    json.dump(all_places, fp)
