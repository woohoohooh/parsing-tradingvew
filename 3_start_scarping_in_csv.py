from bs4 import BeautifulSoup
import csv
prefix = 'vn' # МЕНЯТЬ ТОЛЬКО ТУТ ПРЕФИКС
count = 1
for i in range(10000):
    with open(f'data_{prefix}/page{count}.html', encoding='utf8') as f:
        a = f.read()

    soup = BeautifulSoup(a, 'lxml')

    try:
        rr = soup.find(rel='canonical').get('href')
    except:
        rr = soup.find(rel='link-locale').get('href')

    q1 = a.find('"signature":')
    q2 = a[q1:]
    q3 = q2.find('},')
    new = q2[14:q3-4]

    soup = BeautifulSoup(a, 'lxml')
    hey = soup.find_all(
        class_='tv-profile__title-info-item tv-profile__title-info-item--link tv-profile__title-info-item--social-link apply-overflow-tooltip')

    youtube = ''
    twitter = ''
    for i in hey:
        if 'youtube' in i.get('href'):
            youtube = i.get('href')
    for i in hey:
        if 'twitter' in i.get('href'):
            twitter = i.get('href')
    try:
        heya = soup.find(class_='tv-profile__title-info-item tv-profile__title-info-item--link apply-overflow-tooltip').get(
        'href')
    except:
        heya = ''
    with open(f'main_{prefix}.csv', 'a', encoding='utf8', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow([rr, heya, youtube, twitter, new])
    count += 1
print('FINISH')