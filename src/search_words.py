import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import json
from tqdm import tqdm
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service as fs
import time

url = "https://thesaurus.weblio.jp/"
# path = "/User/matsuzawakazuki/Code/py_code/deep/"
def setup_driver():
    # global path
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    chrome_service = fs.Service(executable_path='.\\chromedriver.exe')
    _driver = webdriver.Chrome(service=chrome_service, options=options)

    print('create chromeDriver')
    return _driver

def searchRelatedWords(_word, _driver):
    # global ulr
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
            # print(e)
            _driver = setup_driver()
            print("change sleep mode")
            time.sleep(5)
            print("restart")
        # raise Exception('UnknownError', e)
    print(' '.join(_results))
    return _results, _driver

def offload(_filename):
    # global path
    _path = f'.\\data\\{_filename}.json'
    jsonfile = open(_path, encoding='utf-8')
    return json.load(jsonfile)

# 関連語を辞書オブジェクトに追加
def related_words(_data):

    _driver = setup_driver()
    for key in tqdm(_data):
        _labels = _data[key]['labels']
        _results = []
        _words = _labels.split(' ')
        _words = list(dict.fromkeys(_words))
        for word in _words:
            while word:
                try:
                    _result, _driver = searchRelatedWords(word, _driver)
                    _result = ' '.join(_result)
                    _results.append(_result)
                    break
                except ValueError as e:
                    # print(e)
                    _driver = setup_driver()
                    print("change sleep mode")
                    time.sleep(10)
                    print("restart")

        _labels = _words + _results
        _labels = list(dict.fromkeys(_labels))
        _labels = ' '.join(_labels)
        _data[key]['labels'] = _labels
    
    return _data

# jsonファイル化
def upload(_filename, _submit_dict):
  _jsonfile = f".\\data\\{_filename}.json"
  _json_dic = _submit_dict
  _jsonfile_open = open(_jsonfile,"w",encoding="utf-8")
  json.dump(_json_dic , _jsonfile_open , ensure_ascii=False , indent=4)
  _jsonfile_open.close()

def resize_data(_data:dict)->list:
    _results = []
    for key in _data:
        _labels = _data[key]['labels']
        _words = _labels.split(' ')
        _results += _words
    
    _results = list(dict.fromkeys(_results))
    return _results

def append_related(_words:list)->dict:
    _driver = setup_driver()
    _result = {}
    for word in tqdm(_words):
        while word:
            try:
                _related, _driver = searchRelatedWords(word, _driver)
                _result[word] = _related
                break
            except ValueError as e:
                # print(e)
                _driver = setup_driver()
                print("change sleep mode")
                time.sleep(10)
                print("restart")
    
    return _result

def re_labeling(_data:dict, _words_dict:dict)->dict:
    print('start re_labeling')
    for key in tqdm(_data):
        _labels = _data[key]['labels']
        _results = []
        _words = _labels.split(' ')
        _words = list(dict.fromkeys(_words))
        for word in _words:
            for item in _words_dict:
                if word == item:
                    _results +=_words_dict[item]

        _labels = _words + _results
        _labels = list(dict.fromkeys(_labels))
        _labels = ' '.join(_labels)
        _data[key]['labels'] = _labels
    
    return _data

def scraper(i):
    name = f'Labels{i}'
    data = offload(name)
    print(f'start_scraper{name}')
    re_data = related_words(data)
    re_name = f'Labels{i}_thesaurus'
    upload(re_name, re_data)

def scraper2(i):
    name = f'Labels{i}'
    data = offload(name)
    print(f'start_scraper{name}')
    _search_words = resize_data(data)
    _related_words = append_related(_search_words)
    re_data = re_labeling(data, _related_words)
    re_name = f'Labels{i}_thesaurus'
    upload(re_name, re_data)


if __name__ == '__main__':
    driver = setup_driver()
    # print(searchRelatedWords("男性", driver))
    for x in [20,30]:
        scraper2(x)
# soup = BeautifulSoup(r.text, 'html.parser')
# t = soup.find_all('div')

# print(soup.find_all('div', attrs={'class':"kijiWrp"})[0].text)



# print(soup.prettify())