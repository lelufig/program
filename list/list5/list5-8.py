a = []
for i in range(5):
    a.append(int(input(f"x[{i}]:")))
a = a[::-1]



for i in range(5):
    print(f"x[{i}] = {a[i]}")