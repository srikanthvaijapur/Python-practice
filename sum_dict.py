#sum of dictinary values
d = eval(input('Enter dictinary values:'))
sum = 0
for item in d.items():
    sum = sum + item[1]
print('sum of dict values:',sum)
#OR
#print('sum of dict values:',sum(d.values()))