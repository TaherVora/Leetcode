from collections import defaultdict

strs = ["eat","tea","tan","ate","nat","bat"]
# [["bat"],["nat","tan"],["ate","eat","tea"]]

def groupAnagrams(strs):
    dic=defaultdict(list)
    for i in strs:
        l=[0]*26
        for j in i:
            var=ord(j)-ord('a')
            l[var]+=1
        dic[tuple(l)].append(i)
    return dic.values()

print(groupAnagrams(strs))
