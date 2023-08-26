import pandas as pd


def reader(file_path):
    csvframe = pd.read_table(file_path, sep='\s+')
    print(csvframe)
    out = []

    for i in csvframe:
        print(i)
        """out.append(i.split())
    print(out)"""


reader(r'C:\Users\79536\Downloads\train_dataset_Датасет\additional_data\building_20230808.csv')

df = pd.DataFrame(reader(r"C:\Users\79536\Downloads\train_dataset_Датасет\additional_data\building_20230808.csv"))

df.to_excel('./teams.xlsx')
