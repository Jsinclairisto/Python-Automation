import urllib
from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import datetime
import os
from os.path import isfile, join
import csv
import shutil
import sqlite3
import requests
import pandas as pd


# humboldt_site = pd.read_html('https://www.humboldt.edu/events/featured#/?i=6')


def get_event_info():
	
	calender_page = requests.get("https://dining.humboldt.edu/j-menu").text
	soup = BeautifulSoup(calender_page, 'html.parser')
	#soup.prettify()

	

	#thefood = soup.find_all("div", {"class": "food-menu-dropdown"}, "div", {"class": "field-content"})
	
	#print(menudivs.find_all('p'))

	button = soup.find_all("a", {"class": "btn btn-dropdown collapsed"})

	print(button)

	listings = []
	for rows in soup.find_all("a", {"class": "btn btn-dropdown collapsed"}):
		# date = rows.find("span", class_="date-display-single").p.get_text()

		# print(date)
	

	# for food_items in menudivs:

	# table = soup.find('tbody')
	# rows = table.find_all('tr')

# 	# TODO: Print events in rows


if __name__ == '__main__':
    get_event_info()
    db_thingy()
