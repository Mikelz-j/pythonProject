f = open('sluj.txt', 'r')
str_num = [i for i in f.readlines()]
#print(str_num)
old = []
new = []
for i in str_num:
    k = i.split()
    #print(f'RewriteRule catalog/48/{k[0]}/$ https://seacomm.ru/catalog/morskaya-radiostanciya/{k[1]}/ [R=301,L]')
    old.append(f'https://seacomm.ru/catalog/48/{k[0]}/')
    new.append(f'https://seacomm.ru/catalog/morskaya-radiostanciya/{k[1]}/')
print(old)
print(new)