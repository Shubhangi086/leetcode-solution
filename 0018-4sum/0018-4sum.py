class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        ans, n = [], len(nums)-1
        if not nums[0]*4 <= target <= nums[n]*4:
            return []
        for i in range(n-2):
            pref_sum1 = target - nums[i]
            if i > 0 and nums[i] == nums[i-1] or not nums[i+1]*3 <= pref_sum1 <= nums[n]*3 :
                continue
            for j in range(i+1, n-1):
                l, r, pref_sum2 = j+1, n, pref_sum1 - nums[j]
                if j > i+1 and nums[j] == nums[j-1] or not nums[l]+nums[l+1] <= pref_sum2 <= nums[n]+nums[n-1]:
                    continue
                while l < r:
                    r = bisect_right(nums, pref_sum2 - nums[l], lo= l, hi= r+1) - 1
                    if l >= r:
                        break
                    l = bisect_left(nums, pref_sum2 - nums[r], lo= l, hi= r+1)
                    if nums[l] + nums[r] == pref_sum2 and l != r:
                        ans.append((nums[i], nums[j], nums[l], nums[r]))
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        l += 1
        return ans