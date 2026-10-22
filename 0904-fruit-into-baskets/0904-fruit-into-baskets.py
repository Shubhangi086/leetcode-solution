class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        cnt = defaultdict(int); l = ans = 0
        for r, f in enumerate(fruits):
            cnt[f] += 1
            while len(cnt) > 2:
                cnt[fruits[l]] -= 1
                if cnt[fruits[l]] == 0: del cnt[fruits[l]]
                l += 1
            ans = max(ans, r - l + 1)
        return ans