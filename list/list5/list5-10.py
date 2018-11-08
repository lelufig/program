a = []
# max = 0
# min = 
for i in range(1,6):
    a.append(int(input(f"{i}番:")))
max = a[0]
min = a[0]
for i in a:
    if i > max:
        max = i
    if i < min:
        min = i
print(max)
print(min)