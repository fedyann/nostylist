'''
def revers(input_i):
    out_e = []
    for input in input_i: 
 
         
 
 
        input_n = [] 
        if input.find('улица') == -1: 
            if input.find('площадь') == -1: 
                if input.find('переулок') == -1: 
                    if input.find('проспект') == -1: 
                        inp = input.replace('Проспект', '') 
                        input_n.append('Проспект') 
                        input_n.append(inp) 
                    else: 
                        inp = input.replace('проспект', '') 
                        input_n.append(inp) 
                        input_n.append('проспект') 
 
        elif input.find('переулок') == -1: 
            if input.find('площадь') == -1: 
                if input.find('проспект') == -1 or input.find('Проспект') == -1: 
                    inp = input.replace('улица', '') 
                    input_n.append(inp) 
                    input_n.append('улица') 
 
        elif input.find('переулок') == -1: 
            if input.find('улица') == -1: 
                if input.find('проспект') == -1 or input.find('Проспект') == -1: 
                    inp = input.replace('площадь', '') 
                    input_n.append(inp) 
                    input_n.append('площадь') 
 
        elif input.find('площадь') == -1: 
            if input.find('улица') == -1: 
                if input.find('проспект') == -1 or input.find('Проспект') == -1: 
                    inp = input.replace('переулок', '') 
                    input_n.append(inp) 
                    input_n.append('переулок') 

        for i in range(0,2):
            a = list(input_n[i])
            out = []
            for j in range(len(a)-1,-1,-1):
                out.append(a[j])
            
            out_e.append(out)
            out_e.append(' ')
            

    
    string = ''
    for el in out_e:
        for i in el:
            string += str(i)
        
    return  string

k = revers(['Невский проспект', 'Проспект науки'])

print(k)
'''

'''
import csv

def reader(file_path):

    file = open(file_path, encoding='utf-8')
    file_reader = csv.reader(file, delimiter = ",")
    out = []
    for i in file_reader:
        lines = []
        for j in i :
            lines.append(j)
        out.append(lines)



    a = int(input('Введи номер строки: '))
    b = int(input('Введи номер Элемента: '))

    print(out[a][b])



reader(r"C:\Users\79536\Downloads\train_dataset_Датасет\additional_data\area_20230808.csv") '''
