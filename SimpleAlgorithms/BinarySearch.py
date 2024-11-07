# Example:
#   target = 0
#   array: [-1,0,3,5,7]
# O(log N) time

from typing import List

class Solution:
    def search(self, nums: List[int], target: int):
        l = 0 # at the start in this example this will be pos0,value'-1'
        r = len(nums)-1 # at the start in this example this will be pos4,value'7'

        while l <= r:
            m = (l+r) // 2 # at the start in this example this will be in the middle pos2,value'3'

            if target == nums[m]: # is middle value equal to the target?
                # Part3: Explanation of example
                # At the last iteration m will be equal to target
                return m
            elif target < nums[m]: # is our middle value bigger then the target? "0 < 3"
                # Part1: Explanation of example
                # Change r to a smaller position than m -> pos1,value'0'
                # m will be at pos0,value'-1'
                r = m - 1
            elif target > nums[m]: # is our middle value smaller then the target? 
                # Part2: Explanation of example
                # After the previous changing of m, m will be smaller then the target "0 > -1"
                # So we increase l to pos1,value'0' (same as r)
                l = m + 1

        return -1 # -1 Means that the target is not in the array

    def search_with_prints(self, nums: List[int], target: int):
            print('Start values: nums = ', nums, ' - target = ', target)

            l = 0
            print('start value of l = ', l)

            r = len(nums)-1
            print('start value of r = ', r)

            while l <= r:
                m = (l+r) // 2 
                print('value of m = ', m)

                if target == nums[m]:
                    print('value of m is not equal to target')
                    return m
                elif target < nums[m]: 
                    print('target is smaller then value of m')
                    r = m - 1
                    print('changed value of r to' , r)
                elif target > nums[m]: 
                    print('target is larger then value of m')
                    l = m + 1
                    print('changed value of l to' , l)

            print('Target is not in the array')
            return -1 


if __name__ == '__main__':
    solution = Solution()
    nums = sorted([-1,5,3,0,7]) # -> Binary search algoritm needs a sorted list
    result = solution.search(nums=nums, target=0)
    result = solution.search_with_prints(nums=nums, target=0)
    print(result)
