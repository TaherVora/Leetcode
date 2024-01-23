from collections import Counter

s = "anagram"
t = "nagaram"
def isAnagram(s,t):
    CounterS = Counter(s)
    CounterT = Counter(t)

    if CounterS == CounterT:
        return True
    return False

print(isAnagram(s,t))