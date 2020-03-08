#!/bin/python
# coding:utf-8

import requests
from bs4 import BeautifulSoup

full_url = 'http://www.mca.gov.cn/article/sj/xzqh/2020/2020/202003061536.html'
root_code = '000000'
level_arr = ['', u'省', u'市', u'区']


def load_data(url):
    '''
    发起请求，获取HTML
    '''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text


def parse_page_data(html):
    '''
    解析页面HTML内容
    '''
    html_bs = BeautifulSoup(html, features='lxml')
    if html_bs != '':
        return html_bs


def parse_tr_data(html):
    '''
    解析tr内容
    '''
    code = html.select('td')[1].text
    name = html.select('td')[2].text
    # 根据编码设定区域级别：1-省，2-市，3-区
    if code[2:6] == '0000':
        level = 1
    elif code[2:6] != '0000' and code[4:6] == '00':
        level = 2
    else:
        level = 3
    return {'code': code, 'name': name.strip(), 'level': level}


if __name__ == '__main__':
    html = load_data(full_url)
    trs = parse_page_data(html)
    masterCode = root_code
    secondaryCode = root_code
    area_json = '['
    for tr in trs.findAll('tr', attrs={'height': 19}):
        text = parse_tr_data(tr)
        code = text['code']
        level = text['level']
        if level == 1:
            parent = root_code
            masterCode = code
        elif level == 2:
            parent = masterCode
            secondaryCode = code
        else:
            parent = secondaryCode
        if code[0:3] == '6590':
            parent = '659000'

        area_json += '{'
        area_json += '"code":'+code+','
        area_json += '"name":'+text['name']+','
        area_json += '"parent":'+parent+','
        area_json += '"level":'+str(text['level'])+','
        area_json += '},'
    area_json += ']'
    print(area_json)