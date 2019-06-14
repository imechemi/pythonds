
def isPalindrome(st):
  if len(st) < 2:
    return True
  else:
    return (st[0] == st[-1]) and isPalindrome(st[1:-1])

print(isPalindrome(""))
print(isPalindrome("w"))
print(isPalindrome("we"))
print(isPalindrome("ww"))
print(isPalindrome("wow"))
print(isPalindrome("woow"))
print(isPalindrome("smilims"))
print(isPalindrome("smiliims"))
