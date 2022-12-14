import math
n=int(input('Enter a number:'))
i=2 #considering 'i' to be our max prine factor.
k=0
while n%2==0:
    i=2
    n=n//i
    for i in range(3,int(math.sqrt(n)+1),2):
        while n%i==0:
            k=i
            n=n/i
        if n>2:
            k=n
print(k)
    