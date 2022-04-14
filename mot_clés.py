import csv
from bs4 import BeautifulSoup
import requests
import time
import re


basic_url = 'https://www.amazon.fr'

#look for word
def get_url(search_term):
    template = 's?k={}&__mk_fr_FR=ÅMÅŽÕÑ&ref=nb_sb_noss'
    search_term = search_term.replace(' ', '+')
    return template.format(search_term)


def get_links_write_text():
    element = soup.find_all('div', role="treeitem")
    with open('url_text', 'r+') as file:
        for line in element:
            file.write(str(line).replace('</div>','\n'))
        
        for line in file.readlines():
            return_ = re.findall(r'(/gp/.\w.\w*\w.\b\w*.\w*\b)', str(line))
            for i in return_:
                file.write(i + '\n')

url = requests.get(basic_url + '/gp/bestsellers/boost')

soup = BeautifulSoup(url.text, 'lxml')

print(soup)