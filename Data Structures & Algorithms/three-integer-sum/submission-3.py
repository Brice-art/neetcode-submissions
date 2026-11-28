class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = set()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    if nums[j] == nums[j+1]:
                        j += 1
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    if nums[k] == nums[k-1]:
                        k -= 1
                    k -= 1
                else:
                    res.add(tuple([nums[i], nums[j], nums[k]]))
                    if nums[k] == nums[k-1]:
                        k -= 1
                    if nums[j] == nums[j+1]:
                        j += 1
                    j += 1
                    k -= 1
        return [list(item) for item in res]


