class Solution:
    def isValid(self, s: str) -> bool:
        stack = [None] * len(s)
        pointer = 0

        opening_braces = {'(', '[', '{'}
        closing_braces = {')', ']', '}'}
        relations = {'}': '{', ']': '[', ')': '('}
        
        for i in s:
            if i in opening_braces:
                # if its an opening brace then just add it to the stack
                stack[pointer] = i
                pointer += 1
            if i in closing_braces:
                print(f"{i} is a closing brace")
                if pointer == 0: # if the stack is empty
                    print(f"empty stack")
                    return False
                if relations[i] != stack[pointer-1]: # if the current stack value is not equal to the opening brace of i
                    return False
                else:
                    pointer -=1

        if pointer != 0: return False
        return True
