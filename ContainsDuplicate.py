nums = [1,2,3,1]

def containsDuplicate(nums):
    return True if len(nums)==len(set(nums)) else False

print(containsDuplicate(nums))