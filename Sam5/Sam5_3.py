one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

a1 = min(one)
b1 = min(two)
c1 = min(three)
s1 = (a1 + b1 + c1) / 2
area1 = (s1*(s1-a1)*(s1-b1)*(s1-c1)) **0.5
print(area1)

a2 = max(one)
b2 = max(two)
c2 = max(three)
s2 = (a2 + b2 + c2) / 2
area2 = (s2*(s2-a2)*(s2-b2)*(s2-c2)) **0.5
print(area2)