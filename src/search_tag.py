from bs4 import BeautifulSoup
import requests, lxml

headers = {
    'User-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582'
}

params = {
  'q': 'minecraft',
  'gl': 'us',
  'hl': 'en',
}

html = requests.get('https://www.google.com/search', headers=headers, params=params)
soup = BeautifulSoup(html.text, 'lxml')

for result in soup.select('.tF2Cxc'):
  title = result.select_one('.DKV0Md').text
  link = result.select_one('.yuRUbf a')['href']
  print(title, link, sep='\n')