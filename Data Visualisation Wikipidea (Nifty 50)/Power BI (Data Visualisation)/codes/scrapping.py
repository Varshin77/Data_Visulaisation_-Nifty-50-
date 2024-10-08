# -*- coding: utf-8 -*-
"""Scrapping.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SKdo4vIQpyLWSHKiWWpDwctKxmEjuT_2
"""

from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/NIFTY_50'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')

table = soup.find_all('table')[8]
table

main_table = table.find_all('th')
main_table

import pandas as pd
main_table_titles = [title.text.strip() for title in main_table]
main_table_titles

df = pd.DataFrame(columns=main_table_titles)
df

column_data = table.find_all('tr')
column_data

for row in column_data[1:]:
  row_data = row.find_all('td')
  individual_row_data = [data.text.strip() for data in row_data]
  length = len(df)
  df.loc[length] = individual_row_data

df

from google.colab import files

df.to_csv('Annual Returns.csv',index=False)
files.download('Annual Returns.csv')