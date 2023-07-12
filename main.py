import csv

import requests
from bs4 import BeautifulSoup
import json

import selentiumParser


def writeFile(data):
    with open('../Pyton/data.csv', 'w', encoding='UTF8') as file:
        fileWriter = csv.writer(file, delimiter=';')
        for name in data.keys():
            fileWriter.writerow([name, data[name]])



cookies_normal = {
    '_tuid': '7cd58bedf0a0b3c33ab16684863305fbaac77164',
    '_ym_uid': '1638897945923956217',
    '_ym_d': '1688055547',
    '_space': 'srt_cl',
    'digi_uc': 'W10=',
    'ab_test': '90x10v4%3A1%7Creindexer%3A2%7Cdynamic_yield%3A3%7Cwelcome_mechanics%3A4%7Cdummy%3A10',
    'ab_test_analytics': '90x10v4%3A1%7Creindexer%3A2%7Cdynamic_yield%3A3%7Cwelcome_mechanics%3A4%7Cdummy%3A10',
    'ab_test_segment': '93',
    '_ym_isad': '2',
    'AMP_TOKEN': '%24NOT_FOUND',
    '_gid': 'GA1.2.633692097.1689161685',
    '_ga': 'GA1.2.1289353934.1685205387',
    '_ga_DDRSRL2E1B': 'GS1.1.1689164546.9.0.1689164546.60.0.0',
}

headers = {
    'authority': 'rpc.citilink.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/grpc-web+proto',
    # 'cookie': '_tuid=7cd58bedf0a0b3c33ab16684863305fbaac77164; _ym_uid=1638897945923956217; _ym_d=1688055547; _space=srt_cl; digi_uc=W10=; ab_test=90x10v4%3A1%7Creindexer%3A2%7Cdynamic_yield%3A3%7Cwelcome_mechanics%3A4%7Cdummy%3A10; ab_test_analytics=90x10v4%3A1%7Creindexer%3A2%7Cdynamic_yield%3A3%7Cwelcome_mechanics%3A4%7Cdummy%3A10; ab_test_segment=93; _ym_isad=2; AMP_TOKEN=%24NOT_FOUND; _gid=GA1.2.633692097.1689161685; _ga=GA1.2.1289353934.1685205387; _ga_DDRSRL2E1B=GS1.1.1689164546.9.0.1689164546.60.0.0',
    'origin': 'https://www.citilink.ru',
    'referer': 'https://www.citilink.ru/catalog/noutbuki/',
    'sec-ch-ua': '"Opera GX";v="99", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 OPR/99.0.0.0 (Edition Yx GX)',
    'x-citilink-anon-id': '7cd58bedf0a0b3c33ab16684863305fbaac77164',
    'x-citilink-city-id': 'srt_cl',
    'x-grpc-web': '1',
}



mapp = {}
tmp_p = ''


for i in range(1, 100):
    print('page = ' + str(i))
    if i % 10 == 0:
        try:
            response = requests.get(
                f'https://www.citilink.ru/catalog/noutbuki/?p={i}',
                cookies=selentiumParser.getCookie(),
                headers=headers
            )
        except Exception:
            print('')
    response = requests.get(
        f'https://www.citilink.ru/catalog/noutbuki/?p={i}',
        cookies=cookies_normal,
        headers=headers
    )
    soup = BeautifulSoup(response.text, 'lxml')


    rr = soup.find_all('div', {"class":"product_data__gtm-js product_data__pageevents-js ProductCardHorizontal js--ProductCardInListing js--ProductCardInWishlist"})

    if tmp_p == rr:
        break

    if i == 1:
        tmp_p = rr


    for r in rr:
        jss = json.loads(r.attrs['data-params'])
        ##print(jss['shortName'] + " " + str(jss['price']))
        mapp[jss['shortName']] = jss['price']

##print(mapp)

writeFile(mapp)
