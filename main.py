import csv
import re


def check_format(fmt, responses):
    return all(r == '' or fmt.search(r) for r in responses.values())


def check_if_response_suits(responses, string_steam):
    answer = []
    fl = False
    for key, value in string_steam.items():
        if key in responses:
            fl = False
            for i in responses[key]:
                if i in value:
                    fl = True
        answer.append(fl)
    if False in answer:
        return False
    else:
        return True


def needed_game(file_string: list, responses):
    not_empty_responses = {}
    name = file_string[1]
    string_steam = {'categories': file_string[8].split(';'), 'genres': file_string[9].split(';'),
                    'platforms': file_string[6].split(';')}
    for key, value in responses.items():
        if value:
            not_empty_responses[key] = value
    if check_if_response_suits(not_empty_responses, string_steam):
        return name
    else:
        return 'not this game'


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
            # эта проверка нужна потому, что у нас разделитель запятая и ее же нужно ставить в конце запроса, если
            # вводится только одно слово и при split получатся, что последним элементом массива будет пустая строка,
            # она не нужна и мешает, я ее убираю
            for key, value in responses.items():
                res = [v.strip() for v in value.split(',')]
                if '' in res:
                    res.remove('')
                responses[key] = res
            for i in reader:
                res = needed_game(i, responses)
                if res != 'not this game':
                    result.write(res)
                    result.write('\n')
