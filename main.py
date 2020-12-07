import csv
import re


def check(x: list):
    q1 = question1
    q2 = question2
    q3 = question3
    flag = False
    name = x[1]
    platform = x[6].split(';')
    category = x[8].split(';')
    genres = x[9].split(';')
    if q1 != '' and q2 != '' and q3 != '':
        # print(1)
        for g in q1:
            if g[0] == ' ':
                g.strip(' ')
            for c in q2:
                if c[0] == ' ':
                    c.strip(' ')
                for p in q3:
                    if p[0] == ' ':
                        p.strip(' ')
                    if g in genres and c in category and p in platform:
                        flag = True
    elif q1 == '' and q2 != '' and q3 != '':
        # print(2)
        for c in q2:
            if c[0] == ' ':
                c.strip(' ')
            for p in q3:
                if p[0] == ' ':
                    p.strip(' ')
                if c in category and p in platform:
                    flag = True
    elif q1 != '' and q2 == '' and q3 != '':
        # print(3)
        for g in q1:
            if g[0] == ' ':
                g.strip(' ')
            for p in q3:
                if p[0] == ' ':
                    p.strip(' ')
                # print(g, p)
                # print(genres, platform)
                if g in genres and p in platform:
                    flag = True
    elif q1 != '' and q2 != '' and q3 == '':
        # print(4)
        for g in q1:
            if g[0] == ' ':
                g.strip(' ')
            for c in q2:
                if c[0] == ' ':
                    c.strip(' ')
                if g in genres and c in category:
                    flag = True
    elif q1 == '' and q2 == '' and q3 != '':
        # print(5)
        for p in q3:
            if p[0] == ' ':
                p.strip(' ')
            if p in platform:
                flag = True
    elif q1 == '' and q2 != '' and q3 == '':
        # print(6)
        for c in q2:
            if c[0] == ' ':
                c.strip(' ')
            if c in category:
                flag = True
    elif q1 != '' and q2 == '' and q3 == '':
        # print(7)
        for g in q1:
            if g[0] == ' ':
                g.strip(' ')
            if g in genres:
                flag = True
    if flag:
        return name
    else:
        return 0


with open(r'steam.csv') as f:
    result = open('result.txt', 'w')
    reader = csv.reader(f)
    print('Если вас интересует только один жанр(платформа,категория), то поставьте в конце запятую, '
          'иначе будет неправильный формат ввода')
    question1 = input('Введите интересующие вас жанры через , ')
    question2 = input('Введите категории игры через , ')
    question3 = input('Введите платформы, которые вас интересуют через , ')
    if ((not re.search(r'[A:Z - a:z - ,]', question1) and question1 != '') or
            (not re.search(r'[A:Z - a:z - ,]', question2) and question2 != '') or
            (not re.search(r'[A:Z - a:z - ,]', question3) and question3 != '')):
        print('Неправильный формат ввода')
    else:
        if question1 != '':
            question1 = question1.split(',')
            if '' in question1:
                question1.remove('')
        if question2 != '':
            question2 = question2.split(',')
            if '' in question2:
                question2.remove('')
        if question3 != '':
            question3 = question3.split(',')
            if '' in question3:
                question3.remove('')
        # print(question1)
        # print(question2)
        # print(question3)
        # k = 0
        for i in reader:
            res = check(i)
            # print(res)
            if res != 0:
                result.write(res)
                result.write('\n')
            # k += 1
            # if k == 10:
                # break
    result.close()
