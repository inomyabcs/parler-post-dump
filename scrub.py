#!/usr/bin/env python

import glob
files = glob.glob('./parler.com/post/*.html')

from tqdm import tqdm
from bs4 import BeautifulSoup

data = []
for idx, file in enumerate(tqdm(files)):
	doc_data = {}
	with open(file, 'r') as html_doc:
		soup = BeautifulSoup(html_doc, 'html.parser')
		try:
			author_username = soup.find('span', {'class': 'author--username'}).text
		except AttributeError:
			author_username = ""
		try:
		      author_name = soup.find('span', {'class': 'author--name'}).text
		except AttributeError:
		      author_name = ""
		try:
		      author_profile_picture = soup.find('img', {'alt': 'Post Author Profile Pic'}).get('src', '')
		except AttributeError:
		      author_profile_picture = ""

		try:
		      post_text = soup.find('div', {'class': 'card--body'}).find('p').text
		except AttributeError:
		      post_text = ""

		try:
		      post_image = soup.find('img', {'class': "mc-image--modal--element"}).get('src', '')
		except AttributeError:
		      post_image = ""

		try:
		      post_timestamp = soup.find('span', {'class': 'post--timestamp'}).text
		except AttributeError:
		      post_timestamp = ""

		try:
		      post_impressions = soup.find('span', {'class': 'impressions--count'}).text
		except AttributeError:
		      post_impressions = ""

		data.append({
		        "author_name": author_name,
		        "author_username": author_username,
		        "author_profile_photo": author_profile_picture,
		        "post_text": post_text,
		        "post_image": post_image,
		        "post_timestamp": post_timestamp,
		        "post_impressions": post_impressions
		})

import pandas as pd

df = pd.DataFrame(data)
df.to_csv('parler.csv', encoding='utf-8')

#vals = df.groupby('author_username').apply(list).apply(lambda x: len (x)).values
