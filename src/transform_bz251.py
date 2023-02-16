import csv
import pandas as pd

csv_reader = csv.reader(open("./resource/bz251_5.csv"))
inLine = []
xLine = []
times = []
for line in csv_reader:
    inLine.append(float(line[0][:6]))
    xLine.append(float(line[0][7:13]))
    times.append(float(line[0][14:]))

aTb = []
for i in range(len(inLine)):
    aTb.append([inLine[i], xLine[i]])

result_inLine = []
result_xLine = []
result_times = []

for i in range(255, 501):
    for j in range(460, 801):
        result_inLine.append(i)
        result_xLine.append(j)
        if [i, j] in aTb:
            result_times.append(times[aTb.index([i, j])])
        else:
            result_times.append(0)
        print([result_inLine[-1], result_xLine[-1], result_times[-1]])

# 字典中的key值即为csv中列名
dataframe = pd.DataFrame({'inLine': result_inLine, 'xLine': result_xLine, 'Times': result_times})

# 将DataFrame存储为csv,index表示是否显示行名，default=True
dataframe.to_csv("./resource/result2.csv", index=False, sep=',')
