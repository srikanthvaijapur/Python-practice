#approach 1
'''l = [10,20,30,10,40,20,10]
s = set(l)
print(s)
l1 = list(s)
print(l1)'''

#aproach 2
l = [10,20,30,40,10,50,10,20]
l1 = []
for x in l:
    if x not in l1:
        l1.append(x)
print(l1)