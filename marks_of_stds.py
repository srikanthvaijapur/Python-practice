n = int(input('Enter no of students:'))
d = {}
for i in range(n):
    name = input('Enter name of student:')
    marks = int(input('Enter marks of student:'))
    d[name] = marks
print('_'*30)
print('Name','\t\t', 'marks')
print('_'*30)
for name in d:
    print(name,'\t\t',d[name])
    
