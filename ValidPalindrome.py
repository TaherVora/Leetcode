# https://leetcode.com/problems/valid-palindrome/description/

s = "Aman, a plan, a canal: Panama"

def validPalindrome(s):
    s=s.lower()
    l,r= 0,len(s)-1

    while l<r:
        if not s[l].isalnum():
            l+=1
        elif not s[r].isalnum():
            r-=1
        elif s[l]!=s[r]:
            return False
        else:
            l+=1
            r-=1
    return True

print(validPalindrome(s))