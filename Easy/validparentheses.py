class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        top = '#'
        hashmap = {')': '(', '}': '{', ']': '['}

        for i, char in enumerate(s):
            
            if char in hashmap:

                if not stack:
                    top = '#'
                else:
                    top = stack.pop()

                if top != hashmap[char]:
                    return False

            else:
                stack.append(char)
                
        if not stack:
            return True
        else:
            return False
