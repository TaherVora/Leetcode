# https://leetcode.com/problems/3sum/description/

nums = [-1,0,1,2,-1,-4]
def threesum(nums):
    op=[]
    nums.sort()
    for k in range(len(nums)-2):
        if k>0 and nums[k]==nums[k-1]:
            continue
        else:

            i,j=k+1,len(nums)-1
            while i<j:
                if nums[k]+nums[i]+nums[j]>0:
                    j-=1
                elif nums[k]+nums[i]+nums[j]<0:
                    i+=1
                else:
                    op.append([nums[k],nums[i],nums[j]])
                    i+=1
                    while i<j and nums[i]==nums[i-1]:
                        i+=1

    return op

print(threesum(nums))