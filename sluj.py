f = open('sluj.txt', 'r')
str_num = [i for i in f.readlines()]
#print(str_num)
old = []
new = []
for i in str_num:
    k = i.split()
    s = k[0][20:]
    #print(s)
    #print(f'RewriteRule {s}$ {k[1]} [R=301,L]')
    old.append(k[0])
    new.append(k[1])
print(old)
print(new)