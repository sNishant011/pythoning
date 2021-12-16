class Solution:
	def isValid(self, s:str) -> bool:
		# dict1 = {"(":False, "{":False, "[": False, ")": False, "}": False, "]": False}
		if (s.count("(") == s.count(")")) and (s.count("{") == s.count("}")) and (s.count("[") == s.count("]")):
			...
		else:
			return False
print(Solution().isValid("())("))