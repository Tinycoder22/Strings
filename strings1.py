# If a string is a palindrome or not is checked using a while loop
# Author: Reva Bhagwat
def palindrome(a):
    mid = len(a)-1/2
    start = 0
    last = len(a)-1
    flag = 0
    while start <= mid:
        if a[start] == a[last]:
            start += 1
            last -= 1
        else:
            flag = 1
    if flag == 0:
        print("Given string is a palindrome")
    else:
        print("Given string is a not palindrome")


palindrome("amabama")
