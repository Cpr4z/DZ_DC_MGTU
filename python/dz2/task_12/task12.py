def get_balance(name, transactions) -> int:
    balance = 0
    for i in transactions:
        if i['name'] == name:
            balance += i['amount']
        else:
            continue
    return balance


def count_debts(names, amount, transactions) -> dict:
    sum = amount * len(names)
    sum_balance = 0
    debt_dic = {}
    set_of_names = set()
    for i in transactions:
        set_of_names.add(i['name'])
    #print(set_of_names)
    for i in set_of_names:
        sum_balance += get_balance(i, transactions)
    #print(sum_balance)
    if sum <= sum_balance:
        for i in names:
            debt_dic[i] = 0
    else:
        #debt_sum = sum - sum_balance
        for i in names:
            if get_balance(i, transactions) < amount:
                #print(get_balance(i, transactions))
                debt_dic[i] = amount - get_balance(i, transactions)
                #debt_sum -= amount - get_balance(i, transactions)
            else:
                debt_dic[i] = 0
    #print(debt_dic)
    return debt_dic
