a = int(input("整数は何個ですか："))
sum = 0

for i in range(1,a+1):
    b = int(input(f"No.{i}："))
    sum += b
print(f"合計値：{sum}")
print(f"平均値：{sum/a:.0f}")
    
