import random

def avg(len_num):
    sum = 0
    len_num = 0
    num_list = [0]
    while len(num_list) < len_num:
        num_list.append(random.randint(0,10))
        print(num_list)
    for i in num_list:
        i = random.randint(0,10)
        sum += i
        cred_sum = sum / len(num_list)
        print("Среднее арифметическое значение: ", cred_sum)
avg(7)