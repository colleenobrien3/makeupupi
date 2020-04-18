
import json
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

from datetime import datetime

import urllib
from bs4 import BeautifulSoup


quote_page = 'https://www.crueltyfreekitty.com/list-of-cruelty-free-brands/'
page = urllib.request.urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')
name_box = soup.find_all('td')

whole = []

for i in name_box:
    whole.append(''.join(i.get_text().strip()))

# print(whole)

# newObj = []
# newerObj = []

# for i in range(50):
#     for j in range(8):
#         newObj.append(whole.pop(0))
#     newerObj.append(newObj)
#     newObj = []

# f = open('dataFile.py', 'w')
# f.write(str(newerObj))
# f.close()


data = []
for i in whole:
    if i != '' and i != 'Amazon' and i != 'UltaAmazon' and i != 'SephoraAmazon' and i != 'Sephora' and i != 'SephoraUltaAmazon' and i != 'SephoraUlta' and i != 'Ulta' and i != 'SephoraPetit Vour' and i != 'AmazonPetit Vour':
        data.append({
            "model": "cruelty_free_companies.Company",
            "pk": whole.index(i),
            "fields": {
                'name': i
            }
        })

# print(data)


with open('cruelty_free_companies/fixtures/companies.json', 'w') as outfile:
    json.dump(data, outfile)
