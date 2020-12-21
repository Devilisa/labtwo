"""import csv
with open('steam.csv') as f:
    reader = csv.reader(f)
    k = 0
    f2 = open('result.txt', 'w')
    for i in reader:
        print(i)
        print(i[6].split(';'))
        print(i[8].split(';'))
        print(i[9].split(';'))
        print(i[9].split(';') in ['Action', 'RPG'])
        print(type(i))
        f2.write(i[1])
        f2.write('\n')
        k += 1
        if k == 3:
            break
    p = ' lcnjk  cdnk'
    p.strip(' ')
    print(p)
f2.close()
(re.search(r'[0123456789]', question1) or re.search(r'[0123456789]', question2) or
            re.search(r'[0123456789]', question3) and ((question1 != '' and not re.search(r',', question1)) or
                                                       (question2 != '' and not re.search(r',', question2))
                                                       or (question3 != '' and not re.search(r',', question3))))
"""
y = {'categories': 'categories_response', 'genres': 'genres_response', 'platforms': 'platforms_response'}
not_empty_responses = []
for key in y:
    print(key)
print(not_empty_responses[0][1])
print(y[not_empty_responses[1][0]])
