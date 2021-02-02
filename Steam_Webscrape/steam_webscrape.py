#Steam Webscrape 
#Prints Steam's current Top Sales
#By: Kai Ramirez

import requests
from bs4 import BeautifulSoup

url = 'https://store.steampowered.com/specials#p=0&tab=TopSellers'
page = requests.get(url)


soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id="TopSellersRows")

games = results.find_all('a')

for game in games:
    title = game.find(class_= "tab_item_name").text
    og_price = game.find(class_="discount_original_price").text
    new_price = game.find(class_="discount_final_price").text
    link = game.find('href')
    print(title)
    print(og_price)
    print(new_price)
    print(f"Steam Link: {link}\n")
    print()
