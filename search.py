from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote
import re


def search_by_name(name: str):
    url = "https://baike.baidu.com/search?word=" + quote(name)
    # print(url)
    html = urlopen(url)
    bsobj = BeautifulSoup(html.read(), "html.parser")
    result_by_name_raw = bsobj.find_all('dd')[0:9]
    result = []
    for i in range(0, 9):
        result_per = []
        m_name = result_by_name_raw[i].find('a', class_='result-title').get_text()
        if i == 0:
            m_name = m_name[:-5]
        else:
            m_name = m_name[:-6]
        result_per.append(m_name)
        m_url_raw = result_by_name_raw[i].find('a').get('href')
        if m_url_raw[0:4] == "http":
            m_url = m_url_raw
        else:
            m_url = "http://baike.baidu.com" + m_url_raw
        result_per.append(m_url)
        m_date = result_by_name_raw[i].find('span', class_='result-date').get_text()
        result_per.append(m_date)
        result.append(result_per)
    return result


def search_by_url(url: str):
    html = urlopen(url)
    bsobj = BeautifulSoup(html.read(), "html.parser")
    text = bsobj.find("div", {"class": "lemma-summary"})
    text = text.get_text()[1:]
    re_rule = re.compile(r'[\[](.*?)[]]', re.S)
    for item in re.findall(re_rule, text):
        text = text.replace(("[" + item + "] \n"), "")
    image_url = search_by_url_image(url)
    if len(image_url) != 0:
        text += "简介图片链接：" + image_url
    text=text.strip('\n')
    return text


def search_by_url_image(url: str):
    html = urlopen(url)
    bsobj = BeautifulSoup(html.read(), "html.parser")
    result_image_raw = bsobj.find_all('div', {"class": "summary-pic"})
    if len(result_image_raw) == 0:
        return ""
    else:
        result_image = result_image_raw[0].find('img').get('src')
        return result_image


if __name__ == "__main__":
    # search_by_name("CTF")
    print(search_by_url_image("https://baike.baidu.com/item/ctf/9548546"))
