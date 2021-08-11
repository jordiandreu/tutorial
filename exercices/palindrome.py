
def palindrome(word):
    right = list(word)
    reverse = right.copy()
    #reverse.reverse()
    reverse = reverse[::-1]
#    print(right)
#    print(reverse)
    return right == reverse
