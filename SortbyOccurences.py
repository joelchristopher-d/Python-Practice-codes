def sortkey(item):
#     print(item,-item[1],item[2])
    return (-item[1],item[2])

s=str(input()).lower()
d={}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
# print(d)

chrdet=[(char,d[char],s.index(char)) for char in s]
# print(chrdet)
chrdet.sort(key=sortkey)
# print(chrdet)

for i in chrdet:
    print(i[0],end="")
