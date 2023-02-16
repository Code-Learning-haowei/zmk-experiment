import csv
import pandas as pd

csv_reader = csv.reader(open("./resource/G02-8.csv"))
DEPTH = []
GR = []
AC = []
AC_REC = []
DEN = []

for line_list in csv_reader:
    for line in line_list:
        item_list = line.split()
        DEPTH.append(item_list[0])
        GR.append(item_list[1])
        AC.append(item_list[2])
        AC_REC.append(1/float(item_list[2]))
        DEN.append(item_list[10])
        if float(item_list[10]) != -9999.000:
            print(len(DEPTH))
        print(len(DEPTH))
# 字典中的key值即为csv中列名
dataframe = pd.DataFrame({'DEPTH': DEPTH, 'GR': GR, 'AC': AC, 'AC_REC': AC_REC, 'DEN': DEN})

# 将DataFrame存储为csv,index表示是否显示行名，default=True
dataframe.to_csv("./resource/G02-8-result.las", index=False, sep=" ")