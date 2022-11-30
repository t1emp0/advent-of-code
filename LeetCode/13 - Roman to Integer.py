# Leetcode problems

# 13. Roman to Integer
# https://leetcode.com/problems/roman-to-integer/
# Easy

#%%
numbers_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
subtract_pairs = ["IV", "IX", "XL", "XC", "CD", "CM"]


def romanToInt(num: str) -> int:
    subs_chars = [p[0] for p in subtract_pairs if p in num]
    subs_idxs = [num.index(t) for t in subs_chars]
    subs = [numbers_values[t] for t in subs_chars]
    adds = [numbers_values[t] for (idx, t) in enumerate(num) if idx not in subs_idxs]
    return sum(adds) - sum(subs)


#%%
test = ["III", "LVIII", "MCMXCIV"]
# expected = [3, 58, 1994]

for num in test:
    print(romanToInt(num), "\t", num)
