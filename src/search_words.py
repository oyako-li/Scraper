import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import json
# from tqdm import tqdm
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service as fs
import time


url = "https://thesaurus.weblio.jp/"
def setup_driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    chrome_service = fs.Service(executable_path='/Users/matsuzawakazuki/Code/py_code/deep/chromedriver')
    _driver = webdriver.Chrome(service=chrome_service, options=options)

    print('create chromeDriver')
    return _driver

def searchRelatedWords(_word, _driver):
    global ulr
    _results = []
    if _word == ' ':
        print('None')
        return _results, _driver
    while _word:
        try:
            _driver.get(url)
            search_box = _driver.find_element(by=By.NAME, value='query')
            search_box.send_keys(_word)
            search_box.submit()
            elems = _driver.find_elements(by=By.CLASS_NAME, value='nwntsR')

            for elem in elems[1:]:
                for item in elem.find_elements(by=By.CLASS_NAME, value='crosslink'):
                    _results.append(item.text)
            break
        except Exception as e:
            print(e)
            _driver = setup_driver()
            print("change sleep mode")
            time.sleep(15)
            print("restart")
        # raise Exception('UnknownError', e)
    print(' '.join(_results))
    return _results, _driver

if __name__ == '__main__':
    driver = setup_driver()
    print(searchRelatedWords("", driver))
# soup = BeautifulSoup(r.text, 'html.parser')
# t = soup.find_all('div')

# print(soup.find_all('div', attrs={'class':"kijiWrp"})[0].text)



# print(soup.prettify())