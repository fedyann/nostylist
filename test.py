import xlrd
import random

workbook = xlrd.open_workbook("9466391.xls")
text = open('file.txt', 'w')

worksheet = workbook.sheet_by_index(0)
out = []
street = [' ул ', ' у ', " улица "]
p = [" п ", " пр ", " проспект "]
pl = [" пл ", " площадь "]
per = [" пер ", " переулок "]
citi = [" Спб ", " Питер ", " Санкт-Питербург "]
for i in range(0, 34):
    for j in range(0, 3):
        a = []
        if j == 0:
            text.write(worksheet.cell_value(i, j))
        elif j == 1:
            if worksheet.cell_value(i, j) == 'Улица':
                text.write(list(street)[random.randint(0, 2)])
            elif worksheet.cell_value(i, j) == 'Проспект':
                text.write(list(p)[random.randint(0, 2)])
            elif worksheet.cell_value(i, j) == 'Площадь':
                text.write(list(pl)[random.randint(0, 1)])
            elif worksheet.cell_value(i, j) == 'Переулок':
                text.write(list(per)[random.randint(0, 1)])
        elif j == 2:
            text.write(list(citi)[random.randint(0, 2)])

    text.write('\n')
print(out)
