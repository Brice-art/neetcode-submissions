class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for str in strs:
            org = ''.join(sorted(str))
            if org in group:
                group[org].append(str)
            else:
                group[org] = [str]
        return list(group.values())
            

        