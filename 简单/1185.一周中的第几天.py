
# 轮子学习
# import datetime
#
# def dayOfTheWeek(year, month, day):
# 	any = datetime.datetime(year, month, day).strftime("%w")
# 	print(any)
#
# if __name__ == '__main__':
# 	dayOfTheWeek(2019, 11, 29)


"""
输入：day = 31, month = 8, year = 2019
输出："Saturday"
"""

import datetime


class Solution:
	def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
		week_day_dict = {
			0: "Sunday",
			1: "Monday",
			2: "Tuesday",
			3: "Wednesday",
			4: "Thursday",
			5: "Friday",
			6: "Saturday"
		}

		anyday = datetime.datetime(year, month, day).strftime("%w")

		return week_day_dict[int(anyday)]


# 作者：trklnejQEZ
# 链接：https: // leetcode - cn.com / problems / day - of - the - week / solution / pythoncong - bu - zao - lun - zi - by - trklnejqez /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。