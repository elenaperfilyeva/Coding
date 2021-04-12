#412 Fizz Buzz
# Given an integer n, return a string array answer (1-indexed) where:
#
# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i if non of the above conditions are true.

class Solution(object):
    def fizzBuzz1(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        fizz_buzz_arr = []
        for i in range(n):
            if (i+1)%15 == 0:
                fizz_buzz_arr.append('FizzBuzz')
                continue
            elif (i+1)%3 == 0:
                fizz_buzz_arr.append('Fizz')
                continue
            elif (i+1)%5 == 0:
                fizz_buzz_arr.append('Buzz')
                continue
            else:
                fizz_buzz_arr.append(str(i+1))
        return fizz_buzz_arr

    def fizzBuzz2(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        fizz_buzz_dict = {3: "Fizz", 5: "Buzz"}

        res = []
        for i in range(1, n + 1):
            res_str = ''
            for key in fizz_buzz_dict:
                if i % key == 0:
                    res_str += fizz_buzz_dict[key]
            if res_str == '': res_str = str(i)
            res.append(res_str)
        return res
