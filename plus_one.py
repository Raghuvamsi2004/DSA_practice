class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        new_list = []
        n=len(digits)
        for i in range(len(digits)):
            a = digits[i]*(10**(n-1-i))
            num += a
        new_num = num+1
        while new_num > 0:
            new_list.append(new_num%10)
            new_num//=10
        new_list.reverse()
        return new_list
