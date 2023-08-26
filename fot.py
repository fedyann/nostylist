import pandas as pd
file_path = r"C:\Users\79536\Downloads\train_dataset_Датасет\additional_data\building_20230808.csv"
csvframe = pd.read_csv(file_path)
citi = open('citi.txt', 'w', encoding='utf=8')
street = open('street.txt', 'w', encoding='utf=8')
house = open('house.txt', 'w', encoding='utf=8')
k = open('k.txt', 'w', encoding='utf=8')
l = open('l.txt', 'w', encoding='utf=8')

for i in range(10):

    m = csvframe.loc[i][8].split(',')
    if len(m) == 5:
        if m[1] == 'Дюна':
            citi.write(m[0] + ' ')
            street.write(m[2] + ' ')
            house.write(m[3].split()[1] + ' ')
            x = m[3].find('литера')
            if x != -1:
                l.write(m[3].split()[1]  + ' ')

            else: 
                k.write(m[3].split()[1] + ' ') 

        else:
            citi.write(m[0] + ' ')
            street.write(m[1] + ' ')
            house.write(m[2].split()[1] + ' ')
            try:
                k.write(m[3] + ' ') 
                l.write(m[4] + ' ')

            except: continue

    elif len(m) == 4:
        citi.write(m[0] + ' ')
        try:
            print(m[1].index('улица'))
            street.write(m[1].replace('улица', '') + ' ')
        except:
            street.write(m[1].replace('проспект', '') + ' ')

        house.write(m[2].split()[1] + ' ')
        x = m[3].find('литера')
        if x != -1:
            l.write(m[3].split()[1]  + ' ')

        else: 
            k.write(m[3].split()[1] + ' ') 
    


    if len(m) == 3:
        citi.write(m[0] + ' ')
        street.write(m[1] + ' ')
        house.write(m[2].split()[1] + ' ')



citi.close()
street.close()
house.close()
k.close()
l.close()