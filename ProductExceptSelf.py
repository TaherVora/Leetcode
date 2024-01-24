# https://leetcode.com/problems/product-of-array-except-self/description/

nums = [1,2,3,4]
# Output: [24,12,8,6]

def productExceptSelf(nums):
    op=[1]*len(nums)

    prefix=1
    for i in range(len(nums)):
        op[i]=op[i]*prefix
        prefix = prefix * nums[i]


    postfix=1
    for i in range(len(nums)-1,-1,-1):
        op[i]=op[i]*postfix
        postfix = postfix * nums[i]

    return op

print(productExceptSelf(nums))