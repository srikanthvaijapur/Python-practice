#TO find the vowels given in a word 
word = input('Enter any word:')
s = set(word)
V = {'a','e','i','o','u'}
result = s.intersection(V)
print('The different vowels present in {} are {} '.format(word,result))


