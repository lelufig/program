a = []
sum = 0
for i in range(1,6):
    a.append(int(input(f"{i}番：")))
for i in a:
    sum += i
print(f"合計値：{sum}")
print(f"平均値：{sum/5:.1f}")





