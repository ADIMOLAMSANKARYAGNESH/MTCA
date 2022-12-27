def palindrome(a):
    if a==a[ : :-1]:
        return 'yes'
    else:
        return 'no'
a=input("Enter an element:")
print(palindrome(a))
