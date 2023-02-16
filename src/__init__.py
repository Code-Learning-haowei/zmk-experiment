from time import sleep

a = [255, 255, 255, 256]
b = [400, 401, 402, 400]
c = [5.1, 5.2, 5.3, 5.4]

aTb = []
for i in range(len(a)):
    aTb.append([a[i], b[i]])

temp_a = []
temp_b = []
temp_c = []
for i in range(255, 257):
    for j in range(400, 403):
        temp_a.append(i)
        temp_b.append(j)
        if [i, j] in aTb:
            temp_c.append(c[aTb.index([i, j])])
        else:
            temp_c.append(0)

sleep(10)