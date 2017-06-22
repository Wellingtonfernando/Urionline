A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)
if (A > B and A > C):
    print('%d eh o maior' %A)
elif (B > A and B > C):
    print('%d eh o maior' %B)
elif (C > B and C > A):
    print('%d eh o maior' %C)

