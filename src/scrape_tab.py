import requests
from bs4 import BeautifulSoup

url = 'https://scraping-for-beginner.herokuapp.com/udemy'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())#インデントで表示

t = soup.find_all('p', attrs={'class':'subscribers'})[0]
res = t.text

print(res.split('：')[1])

print(type(soup.select('.subscribers')[0]))

# print(r.status_code+'\n')
# print(r.headers)
# print(r.encoding+'\n')
# print(r.text+'\n')
# print(r.json())
