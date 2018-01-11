import re

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


def remove_punctuation(line):
    rule = re.compile(r"[^a-zA-Z0-9\u4e00-\u9fa5]")
    line = rule.sub('', line)
    return line


def get_ocr_key(filepath):
    fp = open(filepath, 'r')
    tokens = list()
    for line in fp.readlines():
        token = line.split()
        tokens.append(token)
    return tokens
