class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anaMap=defaultdict(list)
        for s in strs:
            sortStr=''.join(sorted(s))
            anaMap[sortStr].append(s)
        return list(anaMap.values())