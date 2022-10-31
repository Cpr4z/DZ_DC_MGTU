import datetime
string = input().split('-')
if int(string[1]) < 10:
    string[1] = string[1][-1]
if int(string[0]) < 10:
    string[0] = string[0][-1]
#print(string)
day_of_week = datetime.date(int(string[2]), int(string[1]), int(string[0])).weekday()
#print(day_of_week)
if day_of_week == 0:
    if int(string[1]) < 10:
        string[1] = '0' + string[1]
    if int(string[0]) < 10:
        string[0] = '0' + string[0]
    string = '-'.join(string)
    print(string)
else:
    count = 0
    while day_of_week != 0:
        day_of_week -= 1
        count += 1
    string[0] = str(int(string[0]) - count)
    if int(string[1]) < 10:
        string[1] = '0' + string[1]
    if int(string[0]) < 10:
        string[0] = '0' + string[0]
    string = '-'.join(string)
    print(string)
