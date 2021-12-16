# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
class Solution:
	def longestCommonPrefix(self, strs: list[str]) -> str:
		common_prefix = ''
		smallest_word = min(strs, key=len)
		n_strs = [i for i in strs if i != smallest_word]
		for i in range(len(smallest_word)):
			is_common = True
			for j in n_strs:
				if 	j[i] != smallest_word[i]:
					is_common = False
			if is_common:
				common_prefix += smallest_word[i]
			else:
				break;
<<<<<<< HEAD
		return common_prefix
=======
		return common_prefix

print(Solution().longestCommonPrefix(["cir","car"]))
>>>>>>> 3ab3713944fa2ada8c42d620f24dab8ac6f2660c
