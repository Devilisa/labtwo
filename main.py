import csv
import re


def check_format(fmt, responses):
    return all(r == '' or fmt.search(r) for r in responses.values())


def check(x: list, y):
    flag = False
    not_empty_responses = []
    name = x[1]
    string_steam = {'categories': x[8].split(';'), 'genres': x[9].split(';'), 'platforms': x[6].split(';')}
    for key, value in y.items():
        if value != '':
            not_empty_responses.append([key, value])
    if len(not_empty_responses) == 3:
        for g in not_empty_responses[1][1]:
            if g[0] == ' ':
                g.strip(' ')
            for c in not_empty_responses[0][1]:
                if c[0] == ' ':
                    c.strip(' ')
                for p in not_empty_responses[2][1]:
                    if p[0] == ' ':
                        p.strip(' ')
                    if (g in string_steam[not_empty_responses[1][0]] and c in string_steam[not_empty_responses[2][0]]
                            and p in string_steam[not_empty_responses[0][0]]):
                        flag = True
    elif len(not_empty_responses) == 2:
        for g in not_empty_responses[1][1]:
            if g[0] == ' ':
                g.strip(' ')
            for c in not_empty_responses[0][1]:
                if c[0] == ' ':
                    c.strip(' ')
                if g in string_steam[not_empty_responses[1][0]] and c in string_steam[not_empty_responses[0][0]]:
                    flag = True
    elif len(not_empty_responses) == 1:
        for g in not_empty_responses[0][1]:
            if g[0] == ' ':
                g.strip(' ')
            if g in string_steam[not_empty_responses[0][0]]:
                flag = True
    if flag:
        return name
    else:
        return 0


with open(r'steam.csv') as f:
    with open('result.txt', 'w') as result:
        reader = csv.reader(f)
        print('Если вас интересует только один жанр(платформа,категория), то поставьте в конце запятую, '
              'иначе будет неправильный формат ввода')
        genres_response = input('Введите интересующие вас жанры через , ')
        categories_response = input('Введите категории игры через , ')
        platforms_response = input('Введите платформы, которые вас интересуют через , ')
        responses = {'categories': categories_response, 'genres': genres_response, 'platforms': platforms_response}
        fmt = re.compile(r'[\w -]+,')
        if not check_format(fmt, responses):
            print('Неправильный формат ввода')
        else:
            for key, value in responses.items():
                res = value.split(',')
                if '' in res:
                    res.remove('')
                responses[key] = res
            for i in reader:
                res = check(i, responses)
                if res != 0:
                    result.write(res)
                    result.write('\n')
