import os
r = r"D:\MY CODES\Python\Toph Problem solve"
arry = os.listdir(r)
for i in arry:
    if i[0] == '.':
        continue
    else :
        line = f'{i[0].upper()}{i[1:]}'
        a = "\\"
        os.rename(f"{r}{a}{i}",f"{r}{a}{line}")