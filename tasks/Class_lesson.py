#Seminar 23/09/2020
#Task_1
from math import *

s = '1 2 3 4 5'
x = [sin(int(a)) if a.isdigit() else 'error' for a in input().split()]

s = input()
arr = s.split()
for a in arr:
    if a.isdigit():
        print(a)

#Task_2
L = [10, 4, 120, 5, 8, 6, 7]
nums = [int(i) for i in input().split()]
L.sort()
print(L)

#Task_3
print([[1 if j==i else 0 for j in range(3)] for i in range(3)])

print([[2 if 1<=j<=2 and 1<=i<=2 else 1 for j in range(4)] for i in range(4)])

#Task_4
N = int(input())

L = [[ j*(2**i) if i%2 == 1 else (4-j) for j in range(4)] for i in range(N)]

for l in L:
    print(l)