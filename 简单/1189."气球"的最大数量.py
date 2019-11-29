"""
输入：text = "nlaebolko"
输出：1

考察 一串特殊字符串在一串长的字符中能够至多获取多少个特殊字符串
"""

from collections import Counter
def maxNumberOfBalloons(text):
	text_count = Counter(text)
	ballon_dict = {
		'a': 1,
		'b': 1,
		'n': 1,
		'l': 2,
		'o': 2,
	}
	result = []
	for key in ballon_dict.keys():
		if key in text_count:
			result.append(int(text_count[key] / ballon_dict[key]))
		else:
			return 0
	return min(result)

print(maxNumberOfBalloons("loonbalxballpoon"))