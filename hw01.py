import string
import random
lst = string.ascii_lowercase
step = 10
user_str = input ('Введите строку: ')
gener = []
for item in user_str:
    gener = gener + random.sample (lst, step)
    gener.append (item)
print (''.join(gener))   

# Вариант 2
# import string
# import random
# user_str = input ('Введите строку: ')
# result = ''
# for letter in user_str:
#     rand = ''.join(random.sample (string.ascii_lowercase, 10))
#     result = result + rand + letter
# print(result)
# print(result[10::11])
