import _thread
import time
import requests
from bs4 import BeautifulSoup

import dynmic_db as db


def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""


def filter_coin(coin_title):
    coin = ''
    for char in coin_title:
        if 48 <= ord(char) <= 57 or 97 <= ord(char) <= 122 or 65 <= ord(char) <= 90 or char == '$':
            coin = coin + char
    return coin


def filter_title_coin(title_coin):
    coin = ''
    if '/' in title_coin:
        coin = title_coin.split('/')
        c1 = filter_coin(coin[0])
        c2 = filter_coin(coin[1])
        if len(c1) < len(c2):
            coin = c1
        else:
            coin = c2
    elif '(' in title_coin and ')' in title_coin:
        coin = find_between(title_coin, '(', ')')
    elif '[' in title_coin and ']' in title_coin:
        coin = find_between(title_coin, '[', ']')
    else:
        coin = filter_coin(title_coin)
    print(filter_coin(coin))
    return filter_coin(coin)


# 65 - 90 + 48 - 57 (
def get_data(_from, _to):
    for num in range(_from, _to):
        try:
            url = 'https://digital-aarena.com/cat/%D8%A3%D8%AE%D8%A8%D8%A7%D8%B1/%D9%85%D8%B4%D8%A7%D8%B1%D9%8A%D8%B9-%D8%A7%D9%84%D8%B9%D9%85%D9%84%D8%A7%D8%AA-%D8%A7%D9%84%D8%B1%D9%82%D9%85%D9%8A%D9%87/page/{}/'.format(
                num)
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            for i in soup.find_all(class_='post-url post-title', href=True):
                if (
                        'معلومات عن العمله الرقميه' in i.text or 'معلومات عن' in i.text or 'ماهي العمله الرقميه‏‏' in i.text or 'ما هي' in i.text or 'ماهي العمله' in i.text or 'ماهي' in i.text) and 'HOT' not in i.text and 'ANKR' not in i.text and 'jasmy' not in i.text:
                    try:
                        my_txt = str(i.text)
                        coin_name = filter_title_coin(my_txt)
                        sub_page = requests.get(i['href'])
                        soup_sup_page = BeautifulSoup(sub_page.content, 'html.parser')
                        info = soup_sup_page.find(class_='entry-content clearfix single-post-content').text
                        info = info.split('تحتل')
                        db.update_coin_info(coin_name, info[0])
                    except Exception as e:
                        print('scrapings error : {} ,  {}'.format(e, i.text))

        except Exception as err:
            print(err)

    print("finish from {} to {}".format(_from, _to))


# _thread.start_new_thread(get_data, (300, 339))
# _thread.start_new_thread(get_data, (1, 50))#
# # done
# _thread.start_new_thread(get_data, (50, 100))#
# _thread.start_new_thread(get_data, (100, 150))#
# _thread.start_new_thread(get_data, (150, 200))#
# _thread.start_new_thread(get_data, (200, 250))#
# _thread.start_new_thread(get_data, (250, 300))#
_thread.start_new_thread(get_data, (339, 350))  #

time.sleep(60 * 60 * 24)
# AGA
# Pig
#				معلومات عن العمله الرقميه  Δ / One Pearl
# 				معلومات عن العمله الرقميه AMB / Apple
#				ما هي العملة الرقمية GENE /Genopets مشروعها و معلومات عنها
