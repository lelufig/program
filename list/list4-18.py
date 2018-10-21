a = int(input("短辺："))
for i in range(a):
    for j in range(a):
        if i + j < 4:
            print(" ", end = "")
        else:
            print("*", end = "")
    print()