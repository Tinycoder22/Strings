# If a string is a palindrome or not and if it is symmetric or not
# Author: Reva Bhagwat

strone = input('Please type in a string: ')
half = int(len(strone)/2)

firststr =strone[:half]
secondstr = strone[half:]

if firststr == secondstr:
    print("It is symmetrical")
else:
    print("It is not symmetrical")

if firststr == secondstr[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
