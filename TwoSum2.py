# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

numbers = [2,3,4]
target = 6

def twoSum2(numbers,target):
    i,j=0,len(numbers)-1
    while i<j:
        if numbers[i]+numbers[j]<target:
            i+=1
        elif numbers[i]+numbers[j]>target:
            j-=1
        else:
            return [i+1,j+1]

print(twoSum2(numbers,target))

# github_pat_11AQVLEWY0UtNIw2SJV2sm_hJY
