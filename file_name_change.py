import os
folderPath = r"D:\MY CODES\Python\Toph Problem solve"
arry = os.listdir(folderPath)
for i in arry:
    if i[0] == '.':
        continue
    else :
        line = f'{i[0].upper()}{i[1:]}' #or you can user lower() for lower case letter
        a = "\\"
        os.rename(f"{folderPath}{a}{i}",f"{folderPath}{a}{line}")