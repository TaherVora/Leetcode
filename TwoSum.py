def twosum(nums,target):
    dic={}
    for i in range(len(nums)):
        diff=target-nums[i]
        if diff in dic:
            return [dic[diff],i]
        else:
            dic[nums[i]]=i

nums = [2,7,11,15]
target = 9
print(twosum(nums,target))