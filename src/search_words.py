import requests
from bs4 import BeautifulSoup
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options


url = "https://thesaurus.weblio.jp/"
driver = webdriver.Chrome('/Users/matsuzawakazuki/Code/py_code/deep/chromedriver')
# # r = requests.get(url, data={'query': "至高"})
driver.get(url)
search_box = driver.find_element_by_class_name('formBoxITxt')

def searchRelatedWords(word):
    search_box.send_keys(word)
    search_box.submit()
    results = []
    try:
        elems = driver.find_elements_by_class_name('nwntsR')
        for elem in elems[1:]:
            for item in elem.find_elements_by_class_name('crosslink'):
                # print(item.text)
                results.append(item.text)
    except IndexError as e:
        print(e)
    return results

print(searchRelatedWords("検索"))
# soup = BeautifulSoup(r.text, 'html.parser')
# t = soup.find_all('div')

# print(soup.find_all('div', attrs={'class':"kijiWrp"})[0].text)



# print(soup.prettify())