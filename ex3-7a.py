a = int(input())
b = int(input())
c = int(input())
d = int(input())
maxi = a
maxi = b if b > maxi else maxi
maxi = c if c > maxi else maxi
maxi = d if d > maxi else maxi
print(maxi) 

