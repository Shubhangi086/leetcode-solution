class Solution:
    def atMostNGivenDigitSet(self, digits: list[str], n: int) -> int:
        int_digits = list(map(int, digits))
        num = list(map(int, str(n)))

        @cache
        def dp(pos: int, tight: int, has_first: bool) -> int:
            if pos == len(num): return int(has_first)
            res = 0
            bound = num[pos] if tight else int_digits[-1] + 1
            for d in int_digits:
                if d == bound: res += dp(pos + 1, True, True)
                elif d < bound: res += dp(pos + 1, False, True)
            if not has_first: res += dp(pos + 1, False, False)

            return res
        
        return dp(0, True, False) 