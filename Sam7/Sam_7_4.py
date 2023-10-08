text = "Hello, world! Python IS the programming language of thE future. My EMAIL is....PYTHON is awesome!!!!"
with open('input1.txt', 'r') as file:
    spis = file.read().split(' ')
    low = text.lower()

for b in spis:
    low = low.replace(b, '*' * len(b))

res = ''

for i, b in enumerate(low):
    if text[i].lower() == b:
        res += text[i]
    else:
        res += b

print(res)