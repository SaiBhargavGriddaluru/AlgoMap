class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Dictionary to store the number and its index
        num_dict = {}

        # Loop through the list of numbers
        for i, num in enumerate(nums):
            # Calculate the complement
            complement = target - num

            # If the complement exists in the dictionary, return the indices
            if complement in num_dict:
                return [num_dict[complement], i]

            # Otherwise, store the current number and its index in the dictionary
            num_dict[num] = i
