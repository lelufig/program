while True:
    a = int (input("人数を入力してください："))
    if 1 <= a <= 80:
        break
    else:
        print("1~80で入力してください")
print(f"{a}人の点数を入力してください。")
b = []
for i in range(1,a+1):
    b.append(int(input(f"{i}番：")))

score = []
for i in range(11):
    score.append(0)

for i in b:
    score[int(i / 10)] += 1

print("-------分布グラフーーーーーーーーーーーーー")
for i in range(10):
    print(f"{i*10:2} - {i*10+9:3}:", end="")
    for j in range(score[i]):
        print("*", end="")
    print()

print(f"{100:8}:", end="")
for j in range(score[10]):
    print("*", end="")
print()