from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        sorted_count = dict(count.most_common())
        sorted_list = list(sorted_count.keys())

        res = []
        for i in range(k):
            res.append(sorted_list[i])
        return res