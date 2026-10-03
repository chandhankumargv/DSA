from collections import deque
from typing import List  # 1. Add this import

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:  # 2. Capitalize List
        result = []
        queue = deque([("", 0, 0)])
        
        while queue:
            current_str, open_cnt, close_cnt = queue.popleft()
            
            if open_cnt == n and close_cnt == n:
                result.append(current_str)
                continue
                
            if open_cnt < n:
                queue.append((current_str + "(", open_cnt + 1, close_cnt))
                
            if close_cnt < open_cnt:
                queue.append((current_str + ")", open_cnt, close_cnt + 1))
                
        return result
  