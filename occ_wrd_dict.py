#occurance of word
word = input('Enter any string:')
d = {}
for ch in word:
    d[ch] = d.get(ch,0)+1
print(d)
for k,v in d.items():
    print(k,'occurs',v,'times')
    