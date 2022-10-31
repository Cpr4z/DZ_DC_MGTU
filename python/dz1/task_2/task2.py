string = input()
sum = 0
while string != "":
    if int(string) % 2 == 0:
        sum += int(string)
    string = input()
print(sum)
