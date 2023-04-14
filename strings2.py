# If a string is a palindrome or not is checked using a while loop
# Author: Reva Bhagwat


def symmetry(b):
    n = len(b)
    flag = 0
    start1 = 0
    if n % 2 == 0:
        mid = n // 2
        print("it is even, mid is ", mid)
    elif n % 2 != 0:
        mid = n // 2 + 1
        print("it is odd, mid is ", mid)
    start2 = mid
    while start1 < mid and start2 < n:
        if b[start1] == b[start2]:
            start1 += 1
            start2 += 1
        else:
            flag = 1
            break
    if flag == 0:
        print("Given string is symmetrical")
    else:
        print("Given string is  not symmetrical")


bro = "abcabc"
symmetry(bro)
