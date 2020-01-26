payments = {}
with open ('date.txt') as f:
    lines = f.readlines ()
    for line in lines:
        splitted = line.split(';')
        if len(splitted)<5:
            continue
        name, amount, date, p_type, *others = splitted
        if p_type!='out':
            continue
        amount = float(amount.split()[0].replace(',', '.'))
        if name in payments:
            payments[name].append (amount)
        else:
            payments[name] = [amount]    
print (payments)
# max count of perch
max_count_person = ''
max_count = 0
for name, sums in payments.items():
    if len (sums)>max_count:
        max_count = len (sums)
        max_count_person = name
print (max_count_person)
print ('Количество покупок: ' , max_count)
