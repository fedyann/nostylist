import pandas as pd
import random
file_path = r"building.csv"
csvframe = pd.read_csv(file_path)
citi = open('citi.txt', 'w', encoding='utf=8')
street = open('street.txt', 'w', encoding='utf=8')
house = open('house.txt', 'w', encoding='utf=8')
k = open('k.txt', 'w', encoding='utf=8')
l = open('l.txt', 'w', encoding='utf=8')
district = open('district.txt', 'w', encoding='utf=8')
def generate(string):
    z=random.randint(0, 1) 
    if z==0:
        n=random.randint(0, 2)
        if n==0:
            string = string.replace("проспект", "пр")
            string = string.replace("шоссе", "шосе")
            string = string.replace("переулок", "пер")
            string = string.replace("линяя", "лин")
            string = string.replace("улица", "ул.")
            string = string.replace("проспект", "просп")
            string = string.replace("литера", "лит")
            string = string.replace("г.Санкт-Петербург", "Питербург")
        if n==1:
            string = string.replace("проспект", "просп")
            string = string.replace("шоссе", "шос")
            string = string.replace("переулок", "периулок")
            string = string.replace("линяя", "лин")
            string = string.replace("улица", "ул")
            string = string.replace("проспект", "пр")
            string = string.replace("литера", "л")
            string = string.replace("город", "гор")
            string = string.replace("г.Санкт-Петербург", "Питер")
        if n==2:
            string = string.replace("проспект", "прос")
            string = string.replace("шоссе", "шосср")
            string = string.replace("переулок", "переулк")
            string = string.replace("улица", "у")
            string = string.replace("проспект", "пр")
            string = string.replace("литера", "л.")
            string = string.replace("город", "гор")
            string = string.replace("г.Санкт-Петербург", "СПБ")
    return string
for i in range(80):

    m = csvframe.loc[i][8].split(',')
    if len(m) == 5:
        if m[1].find('улица') == -1 and m[1].find('проспект') == -1 and m[1].find('шоссе') == -1 and m[1].find('переулок') == -1 and m[1].find('линия') == -1:
            district.write(generate(m[1]) + ', ')
            citi.write(generate(m[0]) + ', ')
            street.write(generate(m[2]) + ', ')
            house.write(generate(m[3]) + ', ')

            if m[4].find('литера') == -1:
                k.write(generate(m[4]) + ', ')

            else:
                l.write(generate(m[4]) + ', ')

        else:
            citi.write(generate(m[0]) + ', ')
            street.write(generate(m[1]) + ', ')
            house.write(generate(m[2]) + ', ')

            if m[3].find('литера') == -1:
                k.write(generate(m[3]) + ', ')
                l.write(generate(m[4]) + ', ')

            else:
                l.write(generate(m[3]) + ', ')
                k.write(generate(m[4]) + ', ')

    elif len(m) == 4:
        if m[1].find('улица') == -1 and m[1].find('проспект') == -1 and m[1].find('шоссе') == -1 and m[1].find('переулок') == -1 and m[1].find('линия') == -1:
            citi.write(generate(m[0]) + ', ')
            street.write(generate(m[2]) + ', ')
            house.write(generate(m[3]) + ', ')
            district.write(generate(m[1]) + ', ')

        else:
            citi.write(generate(m[0]) + ', ')
            street.write(generate(m[1]) + ', ')
            house.write(generate(m[2]) + ', ')
            x = m[3].find('литера')
            if x == -1:
                k.write(generate(m[3]) + ', ')

            else:
                l.write(generate(m[3]) + ', ')

    if len(m) == 3:
        citi.write(generate(m[0]) + ', ')
        street.write(generate(m[1]) + ', ')
        house.write(generate(m[2]) + ', ')


citi.close()
street.close()
house.close()
k.close()
l.close()
district.close()
arr.close()