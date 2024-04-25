class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

                stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping.keys():
                if not stack or mapping[char] != stack.pop():
                    return False
            else:
                return False
        
        return len(stack) == 0
    
        pass
    




# Example usage:
solution = Solution()
print(solution.isValid("()"))  # Output: True
print(solution.isValid("()[]{}"))  # Output: True
print(solution.isValid("(]"))  # Output: False
print(solution.isValid("([)]"))  # Output: False
print(solution.isValid("{[]}"))  # Output: True
