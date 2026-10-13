<<<<<<< HEAD
1. Two Sum
You are given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

class Solution:
    def twoSum(self, nums, target):
        num_map = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in num_map:
                return [num_map[complement], i]

            num_map[num] = i

        return []
=======

>>>>>>> 28c367dedff31018f9b80f69d93180698ee3920c

