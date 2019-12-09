                        # Guide To Web Scraping(Python3
# To web scrape we will use the beautifulSoup4 module
from bs4 import BeautifulSoup as bs

# Here we'll import requests so we can make url requests
import requests

# Here we'll use json to store our scraped data
import json

# Import of csv
import csv

# Here we'll grab the source code for the website we want to scrape
source = requests.get('https://www.burcheburger.com/menus/#burgers').text

soup = bs(source,'lxml')

menu_items = {}
for element in soup.find_all('p',class_='menu-item__heading'):

    '''I included a try block of code here because the website wasn't
    evenly formatted and some of the nodes didn't contain text'''
    try:
        #  This is the menu item name
        item = element.text

        #  This is the menu item description
        item_desc = element.next_sibling.next_sibling.text

        #  This is the menu item price
        item_price = element.next_sibling.next_sibling.next_sibling.next_sibling.text

        #  This is each menu item's data that I was going to use to build a blueprint for the class Food order
        menu_items[item] = {'Name':item, 'Description': item_desc, 'Price':item_price, 'Type': None}
    except:
        continue

'''This was just to display a readable format of each menu item I had scraped'''
# for key, value in menu_items.items():
#     print ("\nItem: " + key)
#     print ("Item Description: " + value['item_desc'])
#     print ("Item Price: " + value['item_price'])

'''This was the beginning of me categorizing the menu items'''
# burgers = []
# for item in menu_items:
#     if 'burger' in item:
#         burgers.append([item,menu_items[item]])
#     elif 'Burger' in item:
#         burgers.append([item,menu_items[item]])

'''This was another display block of code to see each burger item'''
# for burger in burgers:
#     print("\n")
#     print ("Item: " + burger[0])
#     print ("Item Description: " + burger[1]['item_desc'])
#     print ("Item Price: " + burger[1]['item_price'])

'''This was the code I had written to export the entire menu to a csv file'''
# with open('order_database.csv','w') as csv_file:
#     fieldnames = ['Name','Description','Price','Type']
#     csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#
#     csv_writer.writeheader()
#     for item in menu_items:
#         csv_writer.writerow(menu_items[item])
