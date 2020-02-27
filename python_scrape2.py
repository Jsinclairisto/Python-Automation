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
	calender_url = "https://dining.humboldt.edu/j-menu"
	response = urllib.request.urlopen(calender_url)
	html = response.read()
	soup = BeautifulSoup(html, "html.parser")

	#soup.prettify()
	#thefood = soup.find_all("div", {"class": "food-menu-dropdown"})
	
	listings = []
	for menu in soup.find_all("div", {"class": "field-content"}): 
		weekday = menu.find('p').text.strip()
		print(weekday + '\n')
			
		for item in soup.find_all("div", {"class": "food-menu-dropdown"}):
			
			type_meal = item.find_all('h2')


		for thing in type_meal:
			thingy = thing.getText()
			print(thingy + '\n')
			food_item = item.find_all('p')
			for item in food_item:
				food_product_item = item.getText()
				print(food_product_item)
				

			

if __name__ == '__main__':
	get_event_info()
