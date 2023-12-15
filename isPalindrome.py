def isPalindrome(string):
    palindrome = ""
    for character in range(-1, -8, -1):
        palindrome += string[character]
    return palindrome

isPalindrome("abcdcba")

print([0,0,0][0] < -9999999)