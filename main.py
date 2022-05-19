import requests
from bs4 import BeautifulSoup

url = "https://www.washingtonpost.com/technology/2020/09/25/privacy-check-blacklight"

#make request 
result = requests.get(url)
data = BeautifulSoup(result.text,'html.parser')

#getting required data
title = data.find('h1').text
content = data.find('div', class_="grid-body").text[38:-62].split('.')

#print results
print(title)

for lines in content:
    print(lines)




