items = open('dataset_3380_5.txt', 'r')
list_study = [i.strip() for i in items.readlines()]
ll = []
dc = {str(i): [0, 1] for i in range(1,12)}
for i in list_study:
    ll.append(i.split())

for i in ll:
    dc[i[0]][0] += int(i[2])
    dc[i[0]][1] += 1

r = open("r.txt", "w")
for i in dc:
    if dc[i][0] == 0:
        r.write(f'{i} -\n')
    else:
        sr = round((dc[i][0]/dc[i][1]), 1)
        r.write(f'{i} {sr}\n')


#print(dc)