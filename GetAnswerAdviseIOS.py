import wda
import io
import urllib.parse
import requests
import timeit
import base64
from PIL import Image
from utils import perform_search, remove_punctuation, get_ocr_key
from threading import Thread

c = wda.Client()
# OCR API - baidu
keys = get_ocr_key('config/OCR_KEY')
api_key = keys[0]
api_secret = keys[1]
token = keys[2]

while True:
    start = timeit.default_timer()
    c.screenshot('1.png')
    im = Image.open("./1.png")
    print(im.size)
    out = im.resize((1080, 1920))
    print(out.size)
    # parameter4 1100 for zhishichaoren 1200 for baiwanyingxiong
    region = out.crop((75, 315, 1167, 1200))  # iPhone 7P
    imgByteArr = io.BytesIO()
    region.save(imgByteArr, format='PNG')
    image_data = imgByteArr.getvalue()
    base64_data = base64.b64encode(image_data)
    r = requests.post('https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic',
                      params={'access_token': token}, data={'image': base64_data})
    question = ''
    pure_question = ''
    res_num = r.json()['words_result_num']
    question_num = res_num - 3
    word_res = r.json()['words_result']
    for idx in range(len(word_res)):
        if idx >= question_num - 1:
            question += " " + word_res[idx]['words']
            continue
        question += word_res[idx]['words']
        pure_question += word_res[idx]['words']

    print(question)
    question = urllib.parse.quote(question)
    option1 = remove_punctuation(word_res[-1]['words'])
    option2 = remove_punctuation(word_res[-2]['words'])
    option3 = remove_punctuation(word_res[-3]['words'])
    options = [option1, option2, option3]

    Thread(perform_search('https://baidu.com/s?wd=' + question + '&rn=50', "question with options res:", options))
    Thread(perform_search('https://baidu.com/s?wd=' + pure_question + '&rn=50', "pure question res:", options))

    end = timeit.default_timer()
    print("time elapsed", end - start, "seconds")

    next = input("按键继续，或q键退出:")

    if next == 'q':
        break

    print('----------------------')
