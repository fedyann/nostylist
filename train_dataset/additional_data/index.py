import csv
import re
import pandas as pd

town=[]
with open("towns.csv", encoding='utf-8') as r_file:
        reader = csv.reader(r_file, delimiter = ",")
        for row in reader:
            print(row[1])
            town.append(row[1])
placec=[]
with open("area.csv", encoding='utf-8') as r_file:
        reader = csv.reader(r_file, delimiter = ",")
        for row in reader:
            print(row[6])
            placec.append(row[6])


with open('adreses.csv', mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        employee_writer.writerow(['id','target_address','zone','smalltown','area', 'street','house','litera','korp','stroenie','isactive','type'])
        with open("building.csv", encoding='utf-8') as r_file:
            # Создаем объект reader, указываем символ-разделитель ","
            file_reader = csv.reader(r_file, delimiter = ",")
            # Счетчик для подсчета количества строк и вывода заголовков столбцов
            count = 0
            # Считывание данных из CSV файла

    #г.Санкт-Петербург, Репищева улица, дом 14, литера Р
    #г.Санкт-Петербург, Петергофское шоссе, дом 11/21, литера Б
    #город Сестрорецк, улица Николая Соколова, дом 19а
            pattern = re.compile(r'\w+')
            for row in file_reader:
                target_address,zone,smalltown,street,house,litera,korp,stroenie,iscative,types,area,place='','','','','','','','','','','',''
                target_address=row[8]
                r=target_address.split(",")
                standart=1
                if (r[0]=="Санкт-Петербург" or r[0]=="г.Санкт-Петербург"):
                    zone="Санкт-петербург"
                else:
                    if (r[0] in town):
                        zone=r[0]
                    else:
                        zone="неизвестно"
                        standart-=1
                if (len(r)>1-standart):
                    if (r[1-standart] in placec):
                        place=r[1-standart]
                        standart+=1
                if (len(r)>2+standart):        
                    if (r[standart+2] in r):
                        standart+=1
                        street=r[standart]
                        print(street)
                if (len(r)>2+standart):
                    if (r[standart+2] in r):
                        standart+=1
                        house=pattern.findall(r[standart])[1]
                print(street)
                print(zone)
                n=0
                while (n<0):
                    if (pattern.findall(r[1+standart+n])[0]=='литера'):
                            litera=pattern.findall(1+standart+n)[1]
                    if (pattern.findall(r[1+standart+n])[0]=='корпус'):
                            korp=pattern.findall(r[1+standart+n])[1]
                    if (pattern.findall(r[1+standart+n])[0]=='строение'):
                            stroenie=pattern.findall(r[1+standart+n])[1]
                    n+=1

                        
                if (len(row)>=10):
                    if (row[10]=='false'):
                        row[10]=0
                    else:
                        row[10]=1
                if (len(row)>10):
                    iscative=row[10]
                if (len(row)>11):
                    types=row[11]

                    
                employee_writer.writerow([row[0],target_address,zone,smalltown,place,street,house,litera,korp,stroenie,iscative,types])
                count +=1

