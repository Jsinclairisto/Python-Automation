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



# humboldt_site = pd.read_html('https://www.humboldt.edu/events/featured#/?i=6')


def get_event_info():
	
	calender_page = requests.get("https://www.humboldt.edu/events/featured#/?i=6").text

	soup = BeautifulSoup(calender_page, 'html.parser')

	soup.prettify()

	
	
	# table = soup.find('tbody')
	# rows = table.find_all('tr')

	

# 	# TODO: Print events in rows
	


def db_thingy():
    return "this is db_thingy"

if __name__ == '__main__':
    get_event_info()
    db_thingy()
