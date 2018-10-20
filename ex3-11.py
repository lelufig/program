print("二つの整数を入力して下さい")
a=int(input("整数a："))
b=int(input("整数b："))
if -10 <= a-b <= 10:
    print("それらの差は１０以下です")
else:
    print("それらの差は１１以上です")