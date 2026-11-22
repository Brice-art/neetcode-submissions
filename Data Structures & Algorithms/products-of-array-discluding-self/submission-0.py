class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)

        prefix = []
        postfix = []

        pre = 1
        for num in nums:
            pre *= num
            prefix.append(pre)
        post = 1
        for num in nums[::-1]:
            post *= num
            postfix.append(post)
        postfix.reverse()
        
        for i in range(len(nums)):
            if i == 0:
                res[i] = postfix[i+1]
            elif i == len(nums) - 1:
                res[i] = prefix[i-1]
            else:
                res[i] = prefix[i-1] * postfix[i+1]
        return res
