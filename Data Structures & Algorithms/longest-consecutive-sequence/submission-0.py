class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set(nums)
        longest = 0

        for num in nums:
            
            if num - 1 in mySet:
                continue
            else:
                length = 0
                while num + length in mySet:
                    
                    length += 1
                    longest = max(longest, length)
        return longest 