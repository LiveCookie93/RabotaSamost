file = open("text.txt", "rt")
data = file.read()
lens = data.split()
print(len(lens))

s_text = set(data.split())

MyData = sorted(zip([lens.count(w) for w in s_text], s_text), reverse=True)
for txt1 in MyData:
    if (txt1[0] >= MyData[0][0]):
        ResData = txt1
print(ResData)