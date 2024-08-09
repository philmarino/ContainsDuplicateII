def containsNearbyDuplicate(nums, k):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]==nums[j] and abs(i - j) <= k:
                return True
    return False

# Example 1:
# Input: 
nums = [1,2,3,1]
k = 3
print(containsNearbyDuplicate(nums, k))
# Output: true

# Example 2:
# Input: 
nums = [1,0,1,1]
k = 1
print(containsNearbyDuplicate(nums, k))
# Output: true

# Example 3:
# Input: 
nums = [1,2,3,1,2,3]
k = 2
print(containsNearbyDuplicate(nums, k))
# Output: false
 