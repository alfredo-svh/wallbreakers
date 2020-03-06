class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        s = []
        s.append(['('] * n + [')'] * n)
        x = n
        y = n
        
        while x < 2 * n - 1:
            tmp = s[-1].copy()

            tmp[x - 1] = ')'
            tmp[y - 1] = '('
            x += 1
            y += 1
            if tmp[x - 1] == ')':
                if x == 2 * y - 2:
                    x += 1
                else:
                    tmp[x - 1] = '('
                    tmp[1] = ')'
                    x = 3
                    y = 2

            s[-1] = ''.join(s[-1])
            s.append(tmp)
            
        s[-1] = ''.join(s[-1])

        return s