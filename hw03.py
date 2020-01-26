funcs = [len, min, max]
import random
user_input = ''
while user_input!='stop' and funcs:
    print (f'funcs:{funcs}')
    func = random.choice (funcs)
    print(func, func.__doc__)
    funcs.remove (func)
    user_input = input ('Enter something. ')
    print (user_input)
