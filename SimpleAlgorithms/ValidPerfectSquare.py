# if you want to know if something is a perfect square -> Perfect square is num / 2 is an int number
# Perfect square is for example 2^2 -> 4
# 1^2=1*1=1
# 2^2=2*2=4
# 3^2=3*3=9
# 4^2=4*4=16
# But if you have a number like 17 (example) -> Is not a perfect square
# We will try to use a binary search for this (2 values and a middle value) -> Time: O(log n), Space: O(1)

class Solution_PerfectSquare:
    def IsPerfectSquare(self, num: int):
        # For example num = 17
        l = 1 # Start value
        r = num # The number to check

        while l <= r:
            # Part1: Start value of m is 9
            # Part2: m is now changed to 4 
            # Part3: m is now changed to 6 
            # Part4: m is now changed to 5 
            m = (l+r) // 2 
            
            # Part1: Start value of m_squared is 81
            # Part2: m_squared is now changed to 16 
            # Part3: m_squared is now changed to 36 
            # Part4: m_squared is now changed to 25 
            m_squared = m * m 

            if num == m_squared:
                return True
            elif m_squared < num: 
                # Part2: 16 < 17 -> l is changed to 5
                l = m + 1
            else:
                # Part1: 81 > 17 -> r is changed to 8
                # Part3: 36 > 17 -> r is changed to 5
                # Part4: 25 > 17 -> r is changed to 4
                r = m - 1

        # Part5: the while loop is only if l is smaller then or equal to r
        #        Currenly r=4 and l=5, therefore while loop stops and this cannot be a perfect square
        return False 
    
    def IsPerfectSquare_with_prints(self, num: int):

        l = 1 
        print('Start value of l=', l)
        r = num 
        print('Start value of r=', r)

        while l <= r:
            m = (l+r) // 2
            print('Value of m= ', m)
            m_squared = m * m
            print('Value of m_squared=', m_squared)

            if num == m_squared:
                print('Value of num is equal to m_squared -> num =', num, ' == m_Squared=', m_squared)
                return True
            elif m_squared < num: 
                print('Value of m_squared is smaller then num -> m_squared =', m_squared, ' < num=', num)
                l = m + 1
                print('Therefore, change value of l to m+1 -> l =', l)
            else:
                print('Value of m_squared is larger then num -> m_squared =', m_squared, ' > num=', num)
                r = m - 1
                print('Therefore, change value of r to m-1 -> r=', r)

        print('Value of r is now smaller or equal to l -> r=', r, ' <= l=',l)
        print('Therefore it cannot be a perfect square')
        return False 
    
    def IsPerfectSquare_slow_example(self, num: int):
        # Go trough all int's to check if a squared of that is equal to the to check num.
        # If the squared it larger then the wanted num -> it is not a perfect square
        # !!! This is too slow. Better code above. !!!
        v = 1
        v_squared = 1

        while num > v_squared:
            v_squared = v * v
            print(v, '*', v, '=', v_squared)

            if v_squared == num:
                print(v_squared, 'is the same as the wanted num(=' , num, ') -> So it is a perfect square')
                return True
            else:
                v +=1

        print(v_squared, 'is larger then the wanted num(=' , num, ') -> So it is not a perfect square')
        return False


if __name__ == '__main__':
    solution = Solution_PerfectSquare()
    num = 17
    #result = solution.IsPerfectSquare(num=num)
    result = solution.IsPerfectSquare_with_prints(num=num)
    #result = solution.IsPerfectSquare_slow_example(num=num)
    print(result)