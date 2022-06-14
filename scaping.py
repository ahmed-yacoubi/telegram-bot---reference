import _thread
import time
import requests
from bs4 import BeautifulSoup
import db as database


# 65 - 90 + 48 - 57 (
def get_data(_from, _to):
    for num in range(_from, _to + 1):
        print(num)
        url = 'https://digital-aarena.com/cat/%D8%A3%D8%AE%D8%A8%D8%A7%D8%B1/%D9%85%D8%B4%D8%A7%D8%B1%D9%8A%D8%B9-%D8%A7%D9%84%D8%B9%D9%85%D9%84%D8%A7%D8%AA-%D8%A7%D9%84%D8%B1%D9%82%D9%85%D9%8A%D9%87/page/{}/'.format(
            num)
        print(url)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        for i in soup.find_all(class_='post-url post-title', href=True):
            if 'معلومات عن العمله الرقميه' in i.text or 'معلومات عن' in i.text \
                    or 'ماهي العمله الرقميه‏‏' in i.text or 'ما هي' in i.text \
                    or 'ماهي العمله' in i.text or 'ماهي' in i.text:
                try:
                    my_txt = str(i.text)
                    sub_page = requests.get(i['href'])
                    soup_sup_page = BeautifulSoup(sub_page.content, 'html.parser')
                    info = str(soup_sup_page.find(class_='entry-content clearfix single-post-content').text)
                    database.insert_coin(my_txt, info)
                except:
                    print('error')
    print("finish from {} to {}".format(_from, _to))


# 65 - 90 + 48 - 57

_thread.start_new_thread(get_data, (296, 301))#done
_thread.start_new_thread(get_data, (302, 307))#
_thread.start_new_thread(get_data, (308, 312))# done
_thread.start_new_thread(get_data, (313, 318))#
_thread.start_new_thread(get_data, (319, 324))#
_thread.start_new_thread(get_data, (325, 330))#
_thread.start_new_thread(get_data, (331, 336))#
get_data (337, 341)# done
get_data (342, 345)
# 296
