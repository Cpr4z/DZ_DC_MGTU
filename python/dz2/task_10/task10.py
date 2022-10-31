import datetime


def gift_count(budget, month, birthdays):
    dic = {}
    for i, j in birthdays.items():
        if int(j.month) == month:
            dic[i] = j
    if len(dic) == 0:
        print('В этом месяце нет именинников.')
    else:
        sorted(dic.items(), key=lambda dic: int(dic[1].day))
        result = lambda dic: ', '.join(f'{k} ({datetime.datetime.strftime(dic[k],"%d.%m.%Y")})' for k in dic)
        print(f'Именинники в месяце {month}: {result(dic)}.'
              f' При бюджете {budget} они получат по {budget // len(dic)} рублей.')
