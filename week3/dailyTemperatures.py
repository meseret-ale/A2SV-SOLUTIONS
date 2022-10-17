class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        s, answer = [], [0] * len(temperatures)
        for i in range(len(temperatures)):
            t = temperatures[i]
            while s and t > s[-1][0]:
                _, day = s.pop()
                answer[day] = i - day
            s.append((t, i))
            
        return answer




        
                        
