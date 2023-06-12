data_en = []
data_ar = []
data_br = []
data_cn = []
data_de = []
data_es = []
data_fr = []
data_id = []
data_il = []
data_in = []
data_it = []
data_jp = []
data_kr = []
data_my = []
data_pl = []
data_ru = []
data_se = []
data_th = []
data_tr = []
data_tw = []
data_vn = []

with open('data_en.txt', encoding='utf8') as f:
    for i in f:
        data_en.append(i)
with open('data_en_new.txt', 'w', encoding='utf8') as f:
    for i in data_en:
        f.write(i)

with open('data_ar.txt', encoding='utf8') as f:
    for i in f:
        if i not in data_en:
            data_ar.append(i)
with open('data_ar_new.txt', 'w', encoding='utf8') as f:
    for i in data_ar:
        f.write(i)

with open('data_br.txt', encoding='utf8') as f:
    for i in f:
        if i not in data_en:
            if i not in data_ar:
                data_br.append(i)
with open('data_br_new.txt', 'w', encoding='utf8') as f:
    for i in data_br:
        f.write(i)

with open('data_cn.txt', encoding='utf8') as f: # 1.change "cn" here
    for i in f:
        if i not in data_en:
            if i not in data_ar:
                if i not in data_br:
                # 2. add new UPPER here with "if i not in data_PREVIOUS:"
                    data_cn.append(i) # 3. change "cn" here + 4. MOVE RIGHT
with open('data_cn_new.txt', 'w', encoding='utf8') as f:
    for i in data_cn:
        f.write(i)

with open('data_de.txt', encoding='utf8') as f: # 1.change "cn" here
    for i in f:
        if i not in data_en:
            if i not in data_ar:
                if i not in data_br:
                    if i not in data_cn:
                    # 2. add new UPPER here with "if i not in data_PREVIOUS:"
                        data_de.append(i) # 3. change "cn" here + 4. MOVE RIGHT
with open('data_de_new.txt', 'w', encoding='utf8') as f:
    for i in data_de:
        f.write(i)

with open('data_es.txt', encoding='utf8') as f: # 1.change "cn" here
    for i in f:
        if i not in data_en:
            if i not in data_ar:
                if i not in data_br:
                    if i not in data_cn:
                        if i not in data_cn:
                        # 2. add new UPPER here with "if i not in data_PREVIOUS:"
                            data_es.append(i) # 3. change "cn" here + 4. MOVE RIGHT
with open('data_es_new.txt', 'w', encoding='utf8') as f:
    for i in data_es:
        f.write(i)

with open('data_fr.txt', encoding='utf8') as f: # 1.change "cn" here
    for i in f:
        if i not in data_en:
            if i not in data_ar:
                if i not in data_br:
                    if i not in data_cn:
                        if i not in data_cn:
                            if i not in data_es:
                            # 2. add new UPPER here with "if i not in data_PREVIOUS:"
                                data_fr.append(i) # 3. change "cn" here + 4. MOVE RIGHT
with open('data_fr_new.txt', 'w', encoding='utf8') as f:
    for i in data_fr:
        f.write(i)

with open('data_id.txt', encoding='utf8') as f: # 1.change "cn" here
    for i in f:
        if i not in data_en:
            if i not in data_ar:
                if i not in data_br:
                    if i not in data_cn:
                        if i not in data_cn:
                            if i not in data_es:
                                if i not in data_fr:
                            # 2. add new UPPER here with "if i not in data_PREVIOUS:"
                                    data_id.append(i) # 3. change "cn" here + 4. MOVE RIGHT
with open('data_id_new.txt', 'w', encoding='utf8') as f:
    for i in data_id:
        f.write(i)

with open('data_il.txt', encoding='utf8') as f: # 1.change "cn" here
    for i in f:
        if i not in data_en:
            if i not in data_ar:
                if i not in data_br:
                    if i not in data_cn:
                        if i not in data_cn:
                            if i not in data_es:
                                if i not in data_fr:
                                    if i not in data_id:
                            # 2. add new UPPER here with "if i not in data_PREVIOUS:"
                                        data_il.append(i) # 3. change "cn" here + 4. MOVE RIGHT
with open('data_il_new.txt', 'w', encoding='utf8') as f:
    for i in data_il:
        f.write(i)

with open('data_in.txt', encoding='utf8') as f: # 1.change "cn" here
    for i in f:
        if i not in data_en:
            if i not in data_ar:
                if i not in data_br:
                    if i not in data_cn:
                        if i not in data_cn:
                            if i not in data_es:
                                if i not in data_fr:
                                    if i not in data_id:
                                        if i not in data_il:
                            # 2. add new UPPER here with "if i not in data_PREVIOUS:"
                                            data_in.append(i) # 3. change "cn" here + 4. MOVE RIGHT
with open('data_in_new.txt', 'w', encoding='utf8') as f:
    for i in data_in:
        f.write(i)

with open('data_it.txt', encoding='utf8') as f: # 1.change "cn" here
    for i in f:
        if i not in data_en:
            if i not in data_ar:
                if i not in data_br:
                    if i not in data_cn:
                        if i not in data_cn:
                            if i not in data_es:
                                if i not in data_fr:
                                    if i not in data_id:
                                        if i not in data_il:
                                            if i not in data_in:
                            # 2. add new UPPER here with "if i not in data_PREVIOUS:"
                                                data_it.append(i) # 3. change "cn" here + 4. MOVE RIGHT
with open('data_it_new.txt', 'w', encoding='utf8') as f:
    for i in data_it:
        f.write(i)

with open('data_jp.txt', encoding='utf8') as f: # 1.change "cn" here
    for i in f:
        if i not in data_en:
            if i not in data_ar:
                if i not in data_br:
                    if i not in data_cn:
                        if i not in data_cn:
                            if i not in data_es:
                                if i not in data_fr:
                                    if i not in data_id:
                                        if i not in data_il:
                                            if i not in data_in:
                                                if i not in data_it:
                            # 2. add new UPPER here with "if i not in data_PREVIOUS:"
                                                    data_jp.append(i) # 3. change "cn" here + 4. MOVE RIGHT
with open('data_jp_new.txt', 'w', encoding='utf8') as f:
    for i in data_jp:
        f.write(i)

with open('data_kr.txt', encoding='utf8') as f: # 1.change "cn" here
    for i in f:
        if i not in data_en:
            if i not in data_ar:
                if i not in data_br:
                    if i not in data_cn:
                        if i not in data_cn:
                            if i not in data_es:
                                if i not in data_fr:
                                    if i not in data_id:
                                        if i not in data_il:
                                            if i not in data_in:
                                                if i not in data_it:
                                                    if i not in data_jp:
                            # 2. add new UPPER here with "if i not in data_PREVIOUS:"
                                                        data_kr.append(i) # 3. change "cn" here + 4. MOVE RIGHT
with open('data_kr_new.txt', 'w', encoding='utf8') as f:
    for i in data_kr:
        f.write(i)

with open('data_my.txt', encoding='utf8') as f: # 1.change "cn" here
    for i in f:
        if i not in data_en:
            if i not in data_ar:
                if i not in data_br:
                    if i not in data_cn:
                        if i not in data_cn:
                            if i not in data_es:
                                if i not in data_fr:
                                    if i not in data_id:
                                        if i not in data_il:
                                            if i not in data_in:
                                                if i not in data_it:
                                                    if i not in data_jp:
                                                        if i not in data_kr:
                            # 2. add new UPPER here with "if i not in data_PREVIOUS:"
                                                            data_my.append(i) # 3. change "cn" here + 4. MOVE RIGHT
with open('data_my_new.txt', 'w', encoding='utf8') as f:
    for i in data_my:
        f.write(i)

with open('data_pl.txt', encoding='utf8') as f: # 1.change "cn" here
    for i in f:
        if i not in data_en:
            if i not in data_ar:
                if i not in data_br:
                    if i not in data_cn:
                        if i not in data_cn:
                            if i not in data_es:
                                if i not in data_fr:
                                    if i not in data_id:
                                        if i not in data_il:
                                            if i not in data_in:
                                                if i not in data_it:
                                                    if i not in data_jp:
                                                        if i not in data_kr:
                                                            if i not in data_my:
                            # 2. add new UPPER here with "if i not in data_PREVIOUS:"
                                                                data_pl.append(i) # 3. change "cn" here + 4. MOVE RIGHT
with open('data_pl_new.txt', 'w', encoding='utf8') as f:
    for i in data_pl:
        f.write(i)

with open('data_ru.txt', encoding='utf8') as f: # 1.change "cn" here
    for i in f:
        if i not in data_en:
            if i not in data_ar:
                if i not in data_br:
                    if i not in data_cn:
                        if i not in data_cn:
                            if i not in data_es:
                                if i not in data_fr:
                                    if i not in data_id:
                                        if i not in data_il:
                                            if i not in data_in:
                                                if i not in data_it:
                                                    if i not in data_jp:
                                                        if i not in data_kr:
                                                            if i not in data_my:
                                                                if i not in data_pl:
                            # 2. add new UPPER here with "if i not in data_PREVIOUS:"
                                                                    data_ru.append(i) # 3. change "cn" here + 4.
with open('data_ru_new.txt', 'w', encoding='utf8') as f:
    for i in data_ru:
        f.write(i)

with open('data_se.txt', encoding='utf8') as f: # 1.change "cn" here
    for i in f:
        if i not in data_en:
            if i not in data_ar:
                if i not in data_br:
                    if i not in data_cn:
                        if i not in data_cn:
                            if i not in data_es:
                                if i not in data_fr:
                                    if i not in data_id:
                                        if i not in data_il:
                                            if i not in data_in:
                                                if i not in data_it:
                                                    if i not in data_jp:
                                                        if i not in data_kr:
                                                            if i not in data_my:
                                                                if i not in data_pl:
                                                                    if i not in data_ru:
                            # 2. add new UPPER here with "if i not in data_PREVIOUS:"
                                                                        data_se.append(i)
with open('data_se_new.txt', 'w', encoding='utf8') as f:
    for i in data_se:
        f.write(i)

with open('data_th.txt', encoding='utf8') as f: # 1.change "cn" here
    for i in f:
        if i not in data_en:
            if i not in data_ar:
                if i not in data_br:
                    if i not in data_cn:
                        if i not in data_cn:
                            if i not in data_es:
                                if i not in data_fr:
                                    if i not in data_id:
                                        if i not in data_il:
                                            if i not in data_in:
                                                if i not in data_it:
                                                    if i not in data_jp:
                                                        if i not in data_kr:
                                                            if i not in data_my:
                                                                if i not in data_pl:
                                                                    if i not in data_ru:
                                                                        if i not in data_se:
                            # 2. add new UPPER here with "if i not in data_PREVIOUS:"
                                                                            data_th.append(i)
with open('data_th_new.txt', 'w', encoding='utf8') as f:
    for i in data_th:
        f.write(i)

with open('data_tr.txt', encoding='utf8') as f: # 1.change "cn" here
    for i in f:
        if i not in data_en:
            if i not in data_ar:
                if i not in data_br:
                    if i not in data_cn:
                        if i not in data_cn:
                            if i not in data_es:
                                if i not in data_fr:
                                    if i not in data_id:
                                        if i not in data_il:
                                            if i not in data_in:
                                                if i not in data_it:
                                                    if i not in data_jp:
                                                        if i not in data_kr:
                                                            if i not in data_my:
                                                                if i not in data_pl:
                                                                    if i not in data_ru:
                                                                        if i not in data_se:
                                                                            if i not in data_th:
                            # 2. add new UPPER here with "if i not in data_PREVIOUS:"
                                                                                data_tr.append(i)
with open('data_tr_new.txt', 'w', encoding='utf8') as f:
    for i in data_tr:
        f.write(i)

with open('data_tw.txt', encoding='utf8') as f: # 1.change "cn" here
    for i in f:
        if i not in data_en:
            if i not in data_ar:
                if i not in data_br:
                    if i not in data_cn:
                        if i not in data_cn:
                            if i not in data_es:
                                if i not in data_fr:
                                    if i not in data_id:
                                        if i not in data_il:
                                            if i not in data_in:
                                                if i not in data_it:
                                                    if i not in data_jp:
                                                        if i not in data_kr:
                                                            if i not in data_my:
                                                                if i not in data_pl:
                                                                    if i not in data_ru:
                                                                        if i not in data_se:
                                                                            if i not in data_th:
                                                                                if i not in data_tr:
                            # 2. add new UPPER here with "if i not in data_PREVIOUS:"
                                                                                    data_tw.append(i)
with open('data_tw_new.txt', 'w', encoding='utf8') as f:
    for i in data_tw:
        f.write(i)

count_full_vn = 0

with open('data_vn.txt', encoding='utf8') as f: # 1.change "cn" here
    for i in f:
        count_full_vn += 1
        if i not in data_en:
            if i not in data_ar:
                if i not in data_br:
                    if i not in data_cn:
                        if i not in data_cn:
                            if i not in data_es:
                                if i not in data_fr:
                                    if i not in data_id:
                                        if i not in data_il:
                                            if i not in data_in:
                                                if i not in data_it:
                                                    if i not in data_jp:
                                                        if i not in data_kr:
                                                            if i not in data_my:
                                                                if i not in data_pl:
                                                                    if i not in data_ru:
                                                                        if i not in data_se:
                                                                            if i not in data_th:
                                                                                if i not in data_tr:
                                                                                    if i not in data_tw:
                            # 2. add new UPPER here with "if i not in data_PREVIOUS:"
                                                                                        data_vn.append(i)
with open('data_vn_new.txt', 'w', encoding='utf8') as f:
    for i in data_vn:
        f.write(i)

print('data_en:', len(data_en))
print('data_ar:', len(data_ar))
print('data_br:', len(data_br))
print('data_cn:', len(data_cn))
print('data_de:', len(data_de))
print('data_es:', len(data_es))
print('data_fr:', len(data_fr))
print('data_id:', len(data_id))
print('data_il:', len(data_il))
print('data_in:', len(data_in))
print('data_it:', len(data_it))
print('data_jp:', len(data_jp))
print('data_kr:', len(data_kr))
print('data_my:', len(data_my))
print('data_pl:', len(data_pl))
print('data_ru:', len(data_ru))
print('data_se:', len(data_se))
print('data_th:', len(data_th))
print('data_tr:', len(data_tr))
print('data_tw:', len(data_tw))
print('data_vn:', len(data_vn))
print('count_full_vn:', count_full_vn)