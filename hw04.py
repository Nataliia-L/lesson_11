import this
# print ()
with open ('dzen.txt') as f:
    lines = f.read ()
    new_file = []
    for item in lines:
        # key = len (item)
        new_file.append(lines)
        new_file.sort()
print (new_file)
