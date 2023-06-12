import requests
prefix = 'vn' # МЕНЯТЬ ТОЛЬКО ТУТ ПРЕФИКС
headers = {'accept': '*/*', 'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build'}
count = 1

with open(f'data_{prefix}_new.txt', encoding='utf8') as f:
    for i in f:
        i = i.replace('\n', '')
        r = requests.get(i, headers=headers)
        r = r.text
        with open(f'data_{prefix}/page{count}.html', 'w', encoding='utf8') as f:
            f.write(r)
        count += 1