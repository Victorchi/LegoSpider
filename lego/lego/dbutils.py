import datetime
import hashlib
import os
import platform
import random
import re
import pymysql
import requests
from lxml import etree


def get_doc_of_response(url):
    '''
    :param url: 提供的链接url
    :return: 返回xpath可以解析的格式
    '''

    HEADERS = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "keep-alive", "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
    }
    try:
        html = requests.get(url=url, headers=HEADERS, timeout=30)
    except Exception as e:
        print(e)
        return get_doc_of_response(url)

    try:
        doc = etree.HTML(html.text)
    except ValueError:
        doc = etree.HTML(html.text.encode('utf8'))
    return doc


def get_md5(url):
    '''
    :param url:
    :return: md5加密
    '''
    issue_md5 = hashlib.md5()
    issue_md5.update(url.encode('utf8'))
    issue_md5 = issue_md5.hexdigest()
    return issue_md5


def check_year(year):
    year = re.findall('\d{4}', year)[0]
    if 1750 < int(year) < 2020:
        return year
    else:
        return ''


if __name__ == '__main__':
    pass
