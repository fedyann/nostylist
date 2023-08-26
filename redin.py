import csv


def reader(file_path):
    file = open(file_path, encoding='utf-8')
    file_reader = csv.reader(file, delimiter=",")
    out = []
    for i in file_reader:
        lines = []
        for j in i:
            lines.append(j)
            if lines.index(j) == 0:
                print("id: ", j)

            elif lines.index(j) == 1:
                print("индекс: ", j)

            elif lines.index(j) == 2:
                print("город: ", j)

            elif lines.index(j) == 3:
                print("улица: ", j)

            elif lines.index(j) == 4:
                print("дом: ", j)

            elif lines.index(j) == 5:
                print("корпус: ", j)

            elif lines.index(j) == 6:
                print("литера: ", j)

        out.append(lines)


reader(r"C:\Users\79536\Downloads\train_dataset_Датасет\datasets\dataset_1.csv")
