letters, words , lines = 0,0,0
for line in open('input.txt'):
    words+=len(line.split())
    letters+=sum(map(str.isalpha, line))
    lines+=1
print('Input file contains:')
print(letters,'Letters')
print(words,'Words')
print(lines,'lines')