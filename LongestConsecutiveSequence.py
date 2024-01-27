# https://leetcode.com/problems/longest-consecutive-sequence/description/

nums = [0,3,7,2,5,8,4,6,0,1]

# TLE: 1st solution is giving TLE.If you change nums to Set(nums) It won't give TLE.
def longestConsecutiveSequence(nums):
    max_res=0

    for i in range(len(nums)):
        temp=nums[i]
        res=0
        while temp in nums:
            res+=1
            temp-=1
        max_res=max(res,max_res)

    return max_res

def longestConsecutiveSequenceUsingSet(nums):
    max_res = 0
    numset = set(nums)

    for i in numset:
        if i + 1 not in numset:
            temp = 0
            while i - temp in numset:
                temp += 1
            max_res = max(temp,max_res)
    return max_res

print(longestConsecutiveSequence(nums))

