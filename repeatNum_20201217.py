# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

from typing import List

class Solution2:
    def findRepeatNumber(self, nums: List[int]) -> int:
        dictionary = set()
        for each in nums:
            if each in dictionary:
                return each
            else:
                dictionary.add(each)
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] != i:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                else:
                    tmp = nums[nums[i]]
                    nums[nums[i]] = nums[i]
                    nums[i] = tmp

begin = input()
begin = begin.strip('[]')
arr = begin.split(',')
arr_res = list()
for each in arr:
    arr_res.append(int(each))
solu = Solution()
print(solu.findRepeatNumber(arr_res))
