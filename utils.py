import re
from threading import Thread
import requests


def result_evaluate(options, text, response_string):
    n1 = response_string.count(options[0])
    n2 = response_string.count(options[1])
    n3 = response_string.count(options[2])
    n = [n1, n2, n3]

    total = n1 + n2 + n3
    print(text)
    for idx, num in enumerate(n):
        confidence = 0
        if n[idx] != 0:
            confidence = round(n[idx] / total * 1.5, 2)
        print(options[idx], " 可信度: ", confidence)


def perform_search(url, text, options):
    r = requests.get(url)
    result_evaluate(options, text, r.text)
    pass


def single_search(search_text):
    r = requests.get('https://baidu.com/s?wd=' + search_text)
    m = re.search('百度为您找到相关结果约(.+?)个', r.text)
    if m:
        print(search_text.split()[-1], m.group(1))
        return
    print(search_text.split()[-1], 0)


def remove_punctuation(line):
    rule = re.compile(r"[^a-zA-Z0-9\u4e00-\u9fa5\\.\\·\\,]")
    line = rule.sub('', line)
    return line


def get_ocr_key(filepath):
    fp = open(filepath, 'r')
    tokens = list()
    for line in fp.readlines():
        token = line.split()
        tokens.append(token)
    return tokens


def tips(options, question):
    for option in options:
        if option in question:
            print("do not choose", option)

    if '不' in question or '没有' in question:
        print('\'\'\'')
        print('tips：')
        print('选择最少的')
        print('\'\'\'')
