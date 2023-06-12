import requests
from bs4 import BeautifulSoup
import random
import time

params = 'sort=recent'
headers = {'accept': '*/*', 'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build'}
pages = 501
lst = []

# for i in range(1):
#     r = requests.get(f'https://www.tradingview.com/ideas/', headers=headers, params=params)
#     r = r.text
#     with open(f'page1.html', 'w', encoding='utf8') as f:
#         f.write(r)
#     with open(f'page1.html', encoding='utf8') as f:
#         f = f.read()
#     soup = BeautifulSoup(f, 'lxml')
#     soup = soup.find_all(class_='tv-card-user-info__main-wrap js-userlink-popup')
#     for i in soup:
#         i = 'https://www.tradingview.com' + i.get('href') + '\n'
#         with open('data_en.txt', 'a', encoding='utf8') as f:
#             if i not in lst:
#                 lst.append(i)
#                 f.write(i)
#             else:
#                 continue
#     time.sleep(random.randint(1, 2))
#
# for i in range(1):
#     r = requests.get(f'https://in.tradingview.com/ideas/', headers=headers, params=params)
#     r = r.text
#     with open(f'page1.html', 'w', encoding='utf8') as f:
#         f.write(r)
#     with open(f'page1.html', encoding='utf8') as f:
#         f = f.read()
#     soup = BeautifulSoup(f, 'lxml')
#     soup = soup.find_all(class_='tv-card-user-info__main-wrap js-userlink-popup')
#     for i in soup:
#         i = 'https://www.tradingview.com' + i.get('href') + '\n'
#         with open('data_in.txt', 'a', encoding='utf8') as f:
#             if i not in lst:
#                 lst.append(i)
#                 f.write(i)
#             else:
#                 continue
# #     time.sleep(random.randint(1, 2))
# for i in range(1):
#     r = requests.get(f'https://de.tradingview.com/ideas/', headers=headers, params=params)
#     r = r.text
#     with open(f'page1.html', 'w', encoding='utf8') as f:
#         f.write(r)
#     with open(f'page1.html', encoding='utf8') as f:
#         f = f.read()
#     soup = BeautifulSoup(f, 'lxml')
#     soup = soup.find_all(class_='tv-card-user-info__main-wrap js-userlink-popup')
#     for i in soup:
#         i = 'https://www.tradingview.com' + i.get('href') + '\n'
#         with open('data_de.txt', 'a', encoding='utf8') as f:
#             if i not in lst:
#                 lst.append(i)
#                 f.write(i)
#             else:
#                 continue
#     time.sleep(random.randint(1, 2))
for i in range(1):
    r = requests.get(f'https://fr.tradingview.com/ideas/', headers=headers, params=params)
    r = r.text
    with open(f'page1.html', 'w', encoding='utf8') as f:
        f.write(r)
    with open(f'page1.html', encoding='utf8') as f:
        f = f.read()
    soup = BeautifulSoup(f, 'lxml')
    soup = soup.find_all(class_='tv-card-user-info__main-wrap js-userlink-popup')
    for i in soup:
        i = 'https://www.tradingview.com' + i.get('href') + '\n'
        with open('data_fr.txt', 'a', encoding='utf8') as f:
            if i not in lst:
                lst.append(i)
                f.write(i)
            else:
                continue
    time.sleep(random.randint(1, 2))
for i in range(1):
    r = requests.get(f'https://es.tradingview.com/ideas/', headers=headers, params=params)
    r = r.text
    with open(f'page1.html', 'w', encoding='utf8') as f:
        f.write(r)
    with open(f'page1.html', encoding='utf8') as f:
        f = f.read()
    soup = BeautifulSoup(f, 'lxml')
    soup = soup.find_all(class_='tv-card-user-info__main-wrap js-userlink-popup')
    for i in soup:
        i = 'https://www.tradingview.com' + i.get('href') + '\n'
        with open('data_es.txt', 'a', encoding='utf8') as f:
            if i not in lst:
                lst.append(i)
                f.write(i)
            else:
                continue
    time.sleep(random.randint(1, 2))
for i in range(1):
    r = requests.get(f'https://it.tradingview.com/ideas/', headers=headers, params=params)
    r = r.text
    with open(f'page1.html', 'w', encoding='utf8') as f:
        f.write(r)
    with open(f'page1.html', encoding='utf8') as f:
        f = f.read()
    soup = BeautifulSoup(f, 'lxml')
    soup = soup.find_all(class_='tv-card-user-info__main-wrap js-userlink-popup')
    for i in soup:
        i = 'https://www.tradingview.com' + i.get('href') + '\n'
        with open('data_it.txt', 'a', encoding='utf8') as f:
            if i not in lst:
                lst.append(i)
                f.write(i)
            else:
                continue
    time.sleep(random.randint(1, 2))
for i in range(1):
    r = requests.get(f'https://pl.tradingview.com/ideas/', headers=headers, params=params)
    r = r.text
    with open(f'page1.html', 'w', encoding='utf8') as f:
        f.write(r)
    with open(f'page1.html', encoding='utf8') as f:
        f = f.read()
    soup = BeautifulSoup(f, 'lxml')
    soup = soup.find_all(class_='tv-card-user-info__main-wrap js-userlink-popup')
    for i in soup:
        i = 'https://www.tradingview.com' + i.get('href') + '\n'
        with open('data_pl.txt', 'a', encoding='utf8') as f:
            if i not in lst:
                lst.append(i)
                f.write(i)
            else:
                continue
    time.sleep(random.randint(1, 2))
for i in range(1):
    r = requests.get(f'https://se.tradingview.com/ideas/', headers=headers, params=params)
    r = r.text
    with open(f'page1.html', 'w', encoding='utf8') as f:
        f.write(r)
    with open(f'page1.html', encoding='utf8') as f:
        f = f.read()
    soup = BeautifulSoup(f, 'lxml')
    soup = soup.find_all(class_='tv-card-user-info__main-wrap js-userlink-popup')
    for i in soup:
        i = 'https://www.tradingview.com' + i.get('href') + '\n'
        with open('data_se.txt', 'a', encoding='utf8') as f:
            if i not in lst:
                lst.append(i)
                f.write(i)
            else:
                continue
    time.sleep(random.randint(1, 2))
for i in range(1):
    r = requests.get(f'https://tr.tradingview.com/ideas/', headers=headers, params=params)
    r = r.text
    with open(f'page1.html', 'w', encoding='utf8') as f:
        f.write(r)
    with open(f'page1.html', encoding='utf8') as f:
        f = f.read()
    soup = BeautifulSoup(f, 'lxml')
    soup = soup.find_all(class_='tv-card-user-info__main-wrap js-userlink-popup')
    for i in soup:
        i = 'https://www.tradingview.com' + i.get('href') + '\n'
        with open('data_tr.txt', 'a', encoding='utf8') as f:
            if i not in lst:
                lst.append(i)
                f.write(i)
            else:
                continue
    time.sleep(random.randint(1, 2))
for i in range(1):
    r = requests.get(f'https://ru.tradingview.com/ideas/', headers=headers, params=params)
    r = r.text
    with open(f'page1.html', 'w', encoding='utf8') as f:
        f.write(r)
    with open(f'page1.html', encoding='utf8') as f:
        f = f.read()
    soup = BeautifulSoup(f, 'lxml')
    soup = soup.find_all(class_='tv-card-user-info__main-wrap js-userlink-popup')
    for i in soup:
        i = 'https://www.tradingview.com' + i.get('href') + '\n'
        with open('data_ru.txt', 'a', encoding='utf8') as f:
            if i not in lst:
                lst.append(i)
                f.write(i)
            else:
                continue
    time.sleep(random.randint(1, 2))
for i in range(1):
    r = requests.get(f'https://br.tradingview.com/ideas/', headers=headers, params=params)
    r = r.text
    with open(f'page1.html', 'w', encoding='utf8') as f:
        f.write(r)
    with open(f'page1.html', encoding='utf8') as f:
        f = f.read()
    soup = BeautifulSoup(f, 'lxml')
    soup = soup.find_all(class_='tv-card-user-info__main-wrap js-userlink-popup')
    for i in soup:
        i = 'https://www.tradingview.com' + i.get('href') + '\n'
        with open('data_br.txt', 'a', encoding='utf8') as f:
            if i not in lst:
                lst.append(i)
                f.write(i)
            else:
                continue
    time.sleep(random.randint(1, 2))
for i in range(1):
    r = requests.get(f'https://id.tradingview.com/ideas/', headers=headers, params=params)
    r = r.text
    with open(f'page1.html', 'w', encoding='utf8') as f:
        f.write(r)
    with open(f'page1.html', encoding='utf8') as f:
        f = f.read()
    soup = BeautifulSoup(f, 'lxml')
    soup = soup.find_all(class_='tv-card-user-info__main-wrap js-userlink-popup')
    for i in soup:
        i = 'https://www.tradingview.com' + i.get('href') + '\n'
        with open('data_id.txt', 'a', encoding='utf8') as f:
            if i not in lst:
                lst.append(i)
                f.write(i)
            else:
                continue
    time.sleep(random.randint(1, 2))
for i in range(1):
    r = requests.get(f'https://my.tradingview.com/ideas/', headers=headers, params=params)
    r = r.text
    with open(f'page1.html', 'w', encoding='utf8') as f:
        f.write(r)
    with open(f'page1.html', encoding='utf8') as f:
        f = f.read()
    soup = BeautifulSoup(f, 'lxml')
    soup = soup.find_all(class_='tv-card-user-info__main-wrap js-userlink-popup')
    for i in soup:
        i = 'https://www.tradingview.com' + i.get('href') + '\n'
        with open('data_my.txt', 'a', encoding='utf8') as f:
            if i not in lst:
                lst.append(i)
                f.write(i)
            else:
                continue
    time.sleep(random.randint(1, 2))
for i in range(1):
    r = requests.get(f'https://th.tradingview.com/ideas/', headers=headers, params=params)
    r = r.text
    with open(f'page1.html', 'w', encoding='utf8') as f:
        f.write(r)
    with open(f'page1.html', encoding='utf8') as f:
        f = f.read()
    soup = BeautifulSoup(f, 'lxml')
    soup = soup.find_all(class_='tv-card-user-info__main-wrap js-userlink-popup')
    for i in soup:
        i = 'https://www.tradingview.com' + i.get('href') + '\n'
        with open('data_th.txt', 'a', encoding='utf8') as f:
            if i not in lst:
                lst.append(i)
                f.write(i)
            else:
                continue
    time.sleep(random.randint(1, 2))
for i in range(1):
    r = requests.get(f'https://vn.tradingview.com/ideas/', headers=headers, params=params)
    r = r.text
    with open(f'page1.html', 'w', encoding='utf8') as f:
        f.write(r)
    with open(f'page1.html', encoding='utf8') as f:
        f = f.read()
    soup = BeautifulSoup(f, 'lxml')
    soup = soup.find_all(class_='tv-card-user-info__main-wrap js-userlink-popup')
    for i in soup:
        i = 'https://www.tradingview.com' + i.get('href') + '\n'
        with open('data_vn.txt', 'a', encoding='utf8') as f:
            if i not in lst:
                lst.append(i)
                f.write(i)
            else:
                continue
    time.sleep(random.randint(1, 2))
for i in range(1):
    r = requests.get(f'https://jp.tradingview.com/ideas/', headers=headers, params=params)
    r = r.text
    with open(f'page1.html', 'w', encoding='utf8') as f:
        f.write(r)
    with open(f'page1.html', encoding='utf8') as f:
        f = f.read()
    soup = BeautifulSoup(f, 'lxml')
    soup = soup.find_all(class_='tv-card-user-info__main-wrap js-userlink-popup')
    for i in soup:
        i = 'https://www.tradingview.com' + i.get('href') + '\n'
        with open('data_jp.txt', 'a', encoding='utf8') as f:
            if i not in lst:
                lst.append(i)
                f.write(i)
            else:
                continue
    time.sleep(random.randint(1, 2))
for i in range(1):
    r = requests.get(f'https://kr.tradingview.com/ideas/', headers=headers, params=params)
    r = r.text
    with open(f'page1.html', 'w', encoding='utf8') as f:
        f.write(r)
    with open(f'page1.html', encoding='utf8') as f:
        f = f.read()
    soup = BeautifulSoup(f, 'lxml')
    soup = soup.find_all(class_='tv-card-user-info__main-wrap js-userlink-popup')
    for i in soup:
        i = 'https://www.tradingview.com' + i.get('href') + '\n'
        with open('data_kr.txt', 'a', encoding='utf8') as f:
            if i not in lst:
                lst.append(i)
                f.write(i)
            else:
                continue
    time.sleep(random.randint(1, 2))
for i in range(1):
    r = requests.get(f'https://cn.tradingview.com/ideas/', headers=headers, params=params)
    r = r.text
    with open(f'page1.html', 'w', encoding='utf8') as f:
        f.write(r)
    with open(f'page1.html', encoding='utf8') as f:
        f = f.read()
    soup = BeautifulSoup(f, 'lxml')
    soup = soup.find_all(class_='tv-card-user-info__main-wrap js-userlink-popup')
    for i in soup:
        i = 'https://www.tradingview.com' + i.get('href') + '\n'
        with open('data_cn.txt', 'a', encoding='utf8') as f:
            if i not in lst:
                lst.append(i)
                f.write(i)
            else:
                continue
    time.sleep(random.randint(1, 2))
for i in range(1):
    r = requests.get(f'https://tw.tradingview.com/ideas/', headers=headers, params=params)
    r = r.text
    with open(f'page1.html', 'w', encoding='utf8') as f:
        f.write(r)
    with open(f'page1.html', encoding='utf8') as f:
        f = f.read()
    soup = BeautifulSoup(f, 'lxml')
    soup = soup.find_all(class_='tv-card-user-info__main-wrap js-userlink-popup')
    for i in soup:
        i = 'https://www.tradingview.com' + i.get('href') + '\n'
        with open('data_tw.txt', 'a', encoding='utf8') as f:
            if i not in lst:
                lst.append(i)
                f.write(i)
            else:
                continue
    time.sleep(random.randint(1, 2))
for i in range(1):
    r = requests.get(f'https://ar.tradingview.com/ideas/', headers=headers, params=params)
    r = r.text
    with open(f'page1.html', 'w', encoding='utf8') as f:
        f.write(r)
    with open(f'page1.html', encoding='utf8') as f:
        f = f.read()
    soup = BeautifulSoup(f, 'lxml')
    soup = soup.find_all(class_='tv-card-user-info__main-wrap js-userlink-popup')
    for i in soup:
        i = 'https://www.tradingview.com' + i.get('href') + '\n'
        with open('data_ar.txt', 'a', encoding='utf8') as f:
            if i not in lst:
                lst.append(i)
                f.write(i)
            else:
                continue
    time.sleep(random.randint(1, 2))
for i in range(1):
    r = requests.get(f'https://il.tradingview.com/ideas/', headers=headers, params=params)
    r = r.text
    with open(f'page1.html', 'w', encoding='utf8') as f:
        f.write(r)
    with open(f'page1.html', encoding='utf8') as f:
        f = f.read()
    soup = BeautifulSoup(f, 'lxml')
    soup = soup.find_all(class_='tv-card-user-info__main-wrap js-userlink-popup')
    for i in soup:
        i = 'https://www.tradingview.com' + i.get('href') + '\n'
        with open('data_il.txt', 'a', encoding='utf8') as f:
            if i not in lst:
                lst.append(i)
                f.write(i)
            else:
                continue
    time.sleep(random.randint(1, 2))

count = 2

# ================================================================================================================

for i in range(count, pages):
    r = requests.get(f'https://www.tradingview.com/ideas/page-{count}/', headers=headers, params=params)
    r = r.text
    with open(f'page{count}.html', 'w', encoding='utf8') as f:
        f.write(r)
    with open(f'page{count}.html', encoding='utf8') as f:
        f = f.read()
    soup = BeautifulSoup(f, 'lxml')
    soup = soup.find_all(class_='tv-card-user-info__main-wrap js-userlink-popup')
    for i in soup:
        i = 'https://www.tradingview.com' + i.get('href') + '\n'
        with open('data_en.txt', 'a', encoding='utf8') as f:
            if i not in lst:
                lst.append(i)
                f.write(i)
            else:
                continue
    count += 1
    time.sleep(random.randint(1, 2))
print(f'Регион us завершен!')
count = 1
for i in range(count, pages):
    r = requests.get(f'https://in.tradingview.com/ideas/page-{count}/', headers=headers, params=params)
    r = r.text
    with open(f'page{count}.html', 'w', encoding='utf8') as f:
        f.write(r)
    with open(f'page{count}.html', encoding='utf8') as f:
        f = f.read()
    soup = BeautifulSoup(f, 'lxml')
    soup = soup.find_all(class_='tv-card-user-info__main-wrap js-userlink-popup')
    for i in soup:
        i = 'https://www.tradingview.com' + i.get('href') + '\n'
        with open('data_in.txt', 'a', encoding='utf8') as f:
            if i not in lst:
                lst.append(i)
                f.write(i)
            else:
                continue
    count += 1
    time.sleep(random.randint(1, 2))
print(f'Регион in завершен!')
count = 1
for i in range(count, pages):
    r = requests.get(f'https://de.tradingview.com/ideas/page-{count}/', headers=headers, params=params)
    r = r.text
    with open(f'page{count}.html', 'w', encoding='utf8') as f:
        f.write(r)
    with open(f'page{count}.html', encoding='utf8') as f:
        f = f.read()
    soup = BeautifulSoup(f, 'lxml')
    soup = soup.find_all(class_='tv-card-user-info__main-wrap js-userlink-popup')
    for i in soup:
        i = 'https://www.tradingview.com' + i.get('href') + '\n'
        with open('data_de.txt', 'a', encoding='utf8') as f:
            if i not in lst:
                lst.append(i)
                f.write(i)
            else:
                continue
    count += 1
    time.sleep(random.randint(1, 2))
print(f'Регион de завершен!')
count = 1
for i in range(count, pages):
    r = requests.get(f'https://fr.tradingview.com/ideas/page-{count}/', headers=headers, params=params)
    r = r.text
    with open(f'page{count}.html', 'w', encoding='utf8') as f:
        f.write(r)
    with open(f'page{count}.html', encoding='utf8') as f:
        f = f.read()
    soup = BeautifulSoup(f, 'lxml')
    soup = soup.find_all(class_='tv-card-user-info__main-wrap js-userlink-popup')
    for i in soup:
        i = 'https://www.tradingview.com' + i.get('href') + '\n'
        with open('data_fr.txt', 'a', encoding='utf8') as f:
            if i not in lst:
                lst.append(i)
                f.write(i)
            else:
                continue
    count += 1
    time.sleep(random.randint(1, 2))
print(f'Регион fr завершен!')
count = 1
for i in range(count, pages):
    r = requests.get(f'https://es.tradingview.com/ideas/page-{count}/', headers=headers, params=params)
    r = r.text
    with open(f'page{count}.html', 'w', encoding='utf8') as f:
        f.write(r)
    with open(f'page{count}.html', encoding='utf8') as f:
        f = f.read()
    soup = BeautifulSoup(f, 'lxml')
    soup = soup.find_all(class_='tv-card-user-info__main-wrap js-userlink-popup')
    for i in soup:
        i = 'https://www.tradingview.com' + i.get('href') + '\n'
        with open('data_es.txt', 'a', encoding='utf8') as f:
            if i not in lst:
                lst.append(i)
                f.write(i)
            else:
                continue
    count += 1
    time.sleep(random.randint(1, 2))
print(f'Регион es завершен!')
count = 1
for i in range(count, pages):
    r = requests.get(f'https://it.tradingview.com/ideas/page-{count}/', headers=headers, params=params)
    r = r.text
    with open(f'page{count}.html', 'w', encoding='utf8') as f:
        f.write(r)
    with open(f'page{count}.html', encoding='utf8') as f:
        f = f.read()
    soup = BeautifulSoup(f, 'lxml')
    soup = soup.find_all(class_='tv-card-user-info__main-wrap js-userlink-popup')
    for i in soup:
        i = 'https://www.tradingview.com' + i.get('href') + '\n'
        with open('data_it.txt', 'a', encoding='utf8') as f:
            if i not in lst:
                lst.append(i)
                f.write(i)
            else:
                continue
    count += 1
    time.sleep(random.randint(1, 2))
print(f'Регион it завершен!')
count = 1
for i in range(count, pages):
    r = requests.get(f'https://pl.tradingview.com/ideas/page-{count}/', headers=headers, params=params)
    r = r.text
    with open(f'page{count}.html', 'w', encoding='utf8') as f:
        f.write(r)
    with open(f'page{count}.html', encoding='utf8') as f:
        f = f.read()
    soup = BeautifulSoup(f, 'lxml')
    soup = soup.find_all(class_='tv-card-user-info__main-wrap js-userlink-popup')
    for i in soup:
        i = 'https://www.tradingview.com' + i.get('href') + '\n'
        with open('data_pl.txt', 'a', encoding='utf8') as f:
            if i not in lst:
                lst.append(i)
                f.write(i)
            else:
                continue
    count += 1
    time.sleep(random.randint(1, 2))
print(f'Регион pl завершен!')
count = 1
for i in range(count, pages):
    r = requests.get(f'https://se.tradingview.com/ideas/page-{count}/', headers=headers, params=params)
    r = r.text
    with open(f'page{count}.html', 'w', encoding='utf8') as f:
        f.write(r)
    with open(f'page{count}.html', encoding='utf8') as f:
        f = f.read()
    soup = BeautifulSoup(f, 'lxml')
    soup = soup.find_all(class_='tv-card-user-info__main-wrap js-userlink-popup')
    for i in soup:
        i = 'https://www.tradingview.com' + i.get('href') + '\n'
        with open('data_se.txt', 'a', encoding='utf8') as f:
            if i not in lst:
                lst.append(i)
                f.write(i)
            else:
                continue
    count += 1
    time.sleep(random.randint(1, 2))
print(f'Регион se завершен!')
count = 1
for i in range(count, pages):
    r = requests.get(f'https://tr.tradingview.com/ideas/page-{count}/', headers=headers, params=params)
    r = r.text
    with open(f'page{count}.html', 'w', encoding='utf8') as f:
        f.write(r)
    with open(f'page{count}.html', encoding='utf8') as f:
        f = f.read()
    soup = BeautifulSoup(f, 'lxml')
    soup = soup.find_all(class_='tv-card-user-info__main-wrap js-userlink-popup')
    for i in soup:
        i = 'https://www.tradingview.com' + i.get('href') + '\n'
        with open('data_tr.txt', 'a', encoding='utf8') as f:
            if i not in lst:
                lst.append(i)
                f.write(i)
            else:
                continue
    count += 1
    time.sleep(random.randint(1, 2))
print(f'Регион tr завершен!')
count = 1
for i in range(count, pages):
    r = requests.get(f'https://ru.tradingview.com/ideas/page-{count}/', headers=headers, params=params)
    r = r.text
    with open(f'page{count}.html', 'w', encoding='utf8') as f:
        f.write(r)
    with open(f'page{count}.html', encoding='utf8') as f:
        f = f.read()
    soup = BeautifulSoup(f, 'lxml')
    soup = soup.find_all(class_='tv-card-user-info__main-wrap js-userlink-popup')
    for i in soup:
        i = 'https://www.tradingview.com' + i.get('href') + '\n'
        with open('data_ru.txt', 'a', encoding='utf8') as f:
            if i not in lst:
                lst.append(i)
                f.write(i)
            else:
                continue
    count += 1
    time.sleep(random.randint(1, 2))
print(f'Регион ru завершен!')
count = 1
for i in range(count, pages):
    r = requests.get(f'https://br.tradingview.com/ideas/page-{count}/', headers=headers, params=params)
    r = r.text
    with open(f'page{count}.html', 'w', encoding='utf8') as f:
        f.write(r)
    with open(f'page{count}.html', encoding='utf8') as f:
        f = f.read()
    soup = BeautifulSoup(f, 'lxml')
    soup = soup.find_all(class_='tv-card-user-info__main-wrap js-userlink-popup')
    for i in soup:
        i = 'https://www.tradingview.com' + i.get('href') + '\n'
        with open('data_br.txt', 'a', encoding='utf8') as f:
            if i not in lst:
                lst.append(i)
                f.write(i)
            else:
                continue
    count += 1
    time.sleep(random.randint(1, 2))
print(f'Регион br завершен!')
count = 1
for i in range(count, pages):
    r = requests.get(f'https://id.tradingview.com/ideas/page-{count}/', headers=headers, params=params)
    r = r.text
    with open(f'page{count}.html', 'w', encoding='utf8') as f:
        f.write(r)
    with open(f'page{count}.html', encoding='utf8') as f:
        f = f.read()
    soup = BeautifulSoup(f, 'lxml')
    soup = soup.find_all(class_='tv-card-user-info__main-wrap js-userlink-popup')
    for i in soup:
        i = 'https://www.tradingview.com' + i.get('href') + '\n'
        with open('data_id.txt', 'a', encoding='utf8') as f:
            if i not in lst:
                lst.append(i)
                f.write(i)
            else:
                continue
    count += 1
    time.sleep(random.randint(1, 2))
print(f'Регион id завершен!')
count = 1
for i in range(count, pages):
    r = requests.get(f'https://my.tradingview.com/ideas/page-{count}/', headers=headers, params=params)
    r = r.text
    with open(f'page{count}.html', 'w', encoding='utf8') as f:
        f.write(r)
    with open(f'page{count}.html', encoding='utf8') as f:
        f = f.read()
    soup = BeautifulSoup(f, 'lxml')
    soup = soup.find_all(class_='tv-card-user-info__main-wrap js-userlink-popup')
    for i in soup:
        i = 'https://www.tradingview.com' + i.get('href') + '\n'
        with open('data_my.txt', 'a', encoding='utf8') as f:
            if i not in lst:
                lst.append(i)
                f.write(i)
            else:
                continue
    count += 1
    time.sleep(random.randint(1, 2))
print(f'Регион my завершен!')
count = 1
for i in range(count, pages):
    r = requests.get(f'https://th.tradingview.com/ideas/page-{count}/', headers=headers, params=params)
    r = r.text
    with open(f'page{count}.html', 'w', encoding='utf8') as f:
        f.write(r)
    with open(f'page{count}.html', encoding='utf8') as f:
        f = f.read()
    soup = BeautifulSoup(f, 'lxml')
    soup = soup.find_all(class_='tv-card-user-info__main-wrap js-userlink-popup')
    for i in soup:
        i = 'https://www.tradingview.com' + i.get('href') + '\n'
        with open('data_th.txt', 'a', encoding='utf8') as f:
            if i not in lst:
                lst.append(i)
                f.write(i)
            else:
                continue
    count += 1
    time.sleep(random.randint(1, 2))
print(f'Регион th завершен!')
count = 1
for i in range(count, pages):
    r = requests.get(f'https://vn.tradingview.com/ideas/page-{count}/', headers=headers, params=params)
    r = r.text
    with open(f'page{count}.html', 'w', encoding='utf8') as f:
        f.write(r)
    with open(f'page{count}.html', encoding='utf8') as f:
        f = f.read()
    soup = BeautifulSoup(f, 'lxml')
    soup = soup.find_all(class_='tv-card-user-info__main-wrap js-userlink-popup')
    for i in soup:
        i = 'https://www.tradingview.com' + i.get('href') + '\n'
        with open('data_vn.txt', 'a', encoding='utf8') as f:
            if i not in lst:
                lst.append(i)
                f.write(i)
            else:
                continue
    count += 1
    time.sleep(random.randint(1, 2))
print(f'Регион vn завершен!')
count = 1
for i in range(count, pages):
    r = requests.get(f'https://jp.tradingview.com/ideas/page-{count}/', headers=headers, params=params)
    r = r.text
    with open(f'page{count}.html', 'w', encoding='utf8') as f:
        f.write(r)
    with open(f'page{count}.html', encoding='utf8') as f:
        f = f.read()
    soup = BeautifulSoup(f, 'lxml')
    soup = soup.find_all(class_='tv-card-user-info__main-wrap js-userlink-popup')
    for i in soup:
        i = 'https://www.tradingview.com' + i.get('href') + '\n'
        with open('data_jp.txt', 'a', encoding='utf8') as f:
            if i not in lst:
                lst.append(i)
                f.write(i)
            else:
                continue
    count += 1
    time.sleep(random.randint(1, 2))
print(f'Регион jp завершен!')
count = 1
for i in range(count, pages):
    r = requests.get(f'https://kr.tradingview.com/ideas/page-{count}/', headers=headers, params=params)
    r = r.text
    with open(f'page{count}.html', 'w', encoding='utf8') as f:
        f.write(r)
    with open(f'page{count}.html', encoding='utf8') as f:
        f = f.read()
    soup = BeautifulSoup(f, 'lxml')
    soup = soup.find_all(class_='tv-card-user-info__main-wrap js-userlink-popup')
    for i in soup:
        i = 'https://www.tradingview.com' + i.get('href') + '\n'
        with open('data_kr.txt', 'a', encoding='utf8') as f:
            if i not in lst:
                lst.append(i)
                f.write(i)
            else:
                continue
    count += 1
    time.sleep(random.randint(1, 2))
print(f'Регион kr завершен!')
count = 1
for i in range(count, pages):
    r = requests.get(f'https://cn.tradingview.com/ideas/page-{count}/', headers=headers, params=params)
    r = r.text
    with open(f'page{count}.html', 'w', encoding='utf8') as f:
        f.write(r)
    with open(f'page{count}.html', encoding='utf8') as f:
        f = f.read()
    soup = BeautifulSoup(f, 'lxml')
    soup = soup.find_all(class_='tv-card-user-info__main-wrap js-userlink-popup')
    for i in soup:
        i = 'https://www.tradingview.com' + i.get('href') + '\n'
        with open('data_cn.txt', 'a', encoding='utf8') as f:
            if i not in lst:
                lst.append(i)
                f.write(i)
            else:
                continue
    count += 1
    time.sleep(random.randint(1, 2))
print(f'Регион cn завершен!')
count = 1
for i in range(count, pages):
    r = requests.get(f'https://tw.tradingview.com/ideas/page-{count}/', headers=headers, params=params)
    r = r.text
    with open(f'page{count}.html', 'w', encoding='utf8') as f:
        f.write(r)
    with open(f'page{count}.html', encoding='utf8') as f:
        f = f.read()
    soup = BeautifulSoup(f, 'lxml')
    soup = soup.find_all(class_='tv-card-user-info__main-wrap js-userlink-popup')
    for i in soup:
        i = 'https://www.tradingview.com' + i.get('href') + '\n'
        with open('data_tw.txt', 'a', encoding='utf8') as f:
            if i not in lst:
                lst.append(i)
                f.write(i)
            else:
                continue
    count += 1
    time.sleep(random.randint(1, 2))
print(f'Регион tw завершен!')
count = 1
for i in range(count, pages):
    r = requests.get(f'https://ar.tradingview.com/ideas/page-{count}/', headers=headers, params=params)
    r = r.text
    with open(f'page{count}.html', 'w', encoding='utf8') as f:
        f.write(r)
    with open(f'page{count}.html', encoding='utf8') as f:
        f = f.read()
    soup = BeautifulSoup(f, 'lxml')
    soup = soup.find_all(class_='tv-card-user-info__main-wrap js-userlink-popup')
    for i in soup:
        i = 'https://www.tradingview.com' + i.get('href') + '\n'
        with open('data_ar.txt', 'a', encoding='utf8') as f:
            if i not in lst:
                lst.append(i)
                f.write(i)
            else:
                continue
    count += 1
    time.sleep(random.randint(1, 2))
print(f'Регион ar завершен!')
count = 1
for i in range(count, pages):
    r = requests.get(f'https://il.tradingview.com/ideas/page-{count}/', headers=headers, params=params)
    r = r.text
    with open(f'page{count}.html', 'w', encoding='utf8') as f:
        f.write(r)
    with open(f'page{count}.html', encoding='utf8') as f:
        f = f.read()
    soup = BeautifulSoup(f, 'lxml')
    soup = soup.find_all(class_='tv-card-user-info__main-wrap js-userlink-popup')
    for i in soup:
        i = 'https://www.tradingview.com' + i.get('href') + '\n'
        with open('data_il.txt', 'a', encoding='utf8') as f:
            if i not in lst:
                lst.append(i)
                f.write(i)
            else:
                continue
    count += 1
    time.sleep(random.randint(1, 2))
print(f'ВСе регионы завершены!')
