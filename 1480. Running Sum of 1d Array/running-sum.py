# Question: Given an array `nums`, write a function that returns the running sum of the array. The running sum is defined as the cumulative sum of the elements from the start of the array to the current index.

# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.
# Example 1:

# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
# Example 2:

# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
# Example 3:

# Input: nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]
 

# Constraints:

# 1 <= nums.length <= 1000
# -10^6 <= nums[i] <= 10^6

# My Unrefined Solution:
class Solution(object):
    def runningSum(self, nums):
        arrTotal = []
        iterate = 0
        totalNum = 0
        for x in nums:
            if iterate == 0:
                arrTotal.append(x)
                iterate += 1
            else:
                for i in arrTotal:
                    totalNum = x + i
                arrTotal.append(totalNum)
                totalNum = 0
        return arrTotal