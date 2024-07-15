class Solution:
    def reverseParentheses(self, s: str) -> str:
        size = len(s)
        result = ''
        queue = []
        num_char_inside = 0
        close_p = 0
        open_p = s.count('(')
        for p in range(open_p):
            print(s)
            for index, c in enumerate(reversed(s)):
                if c == ')':
                    close_p = 1
                    queue = []
                    num_char_inside = 0
                elif close_p >= 1 and c != '(':
                    queue.append(c)
                    num_char_inside += 1
                elif c == '(':
                    for x in range(num_char_inside):
                        result += queue.pop(0)
                    close_p -= 1
                    queue = []
                    rs = len(result)
                    buffer = size - rs
                    s = s.replace(s[index - rs - 1:index + 1], result)
                    result = ""
                    break

        return s