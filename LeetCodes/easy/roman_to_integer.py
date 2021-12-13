
class Solution:
	def romanToInt(self, x: str) -> int:
		dict_r = {"I": 1, "V": 5, "X": 10, "L":50, "C": 100, "D": 500, "M": 1000}
		xl = [i for i in x]
		sum1 = 0
		while xl:
			if len(xl) > 1:
				prev = xl[0]
				nxt = xl[1]
				if (prev == "I" and (nxt == "V" or nxt == "X")) or (prev == "X" and (nxt == "L" or nxt == "C")) or (prev == "C" and (nxt == "D" or nxt == "M")):
					sum1 += (dict_r[nxt] - dict_r[prev])
					xl.pop(0)
					xl.pop(0)
				else:
					sum1 += dict_r[prev]
					xl.pop(0)
			else:
				sum1 += dict_r[xl[0]]
				xl.pop(0)
		return sum1


test_cases = ["III", "IV", "LVIII", "IX", "MCMXCIV"]
for i in test_cases:
	print("The value of", i, "in integer is", Solution().romanToInt(i))