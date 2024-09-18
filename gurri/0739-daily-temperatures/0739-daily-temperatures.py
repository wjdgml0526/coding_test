class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)
        # 초기화 
        stack = []
        # 역방향 탐색을 하면서 스택을 사용
        for i in range(len(temperatures)-1, -1, -1):

            # 스택이 비어있지않고, 맨위의 온도가 현재보다 작거나 같으면
            while stack and temperatures[i]>= temperatures[stack[-1]]:
                # 해당인덱스 제거
                stack.pop()            

            # 비어있지 않으면
            if stack :
                # 현재 날짜에서 스택 맨 위 날짜 차이를 기록
                res[i] = stack[-1] - i

            # 현재 인덱스 추가
            stack.append(i)
        
        # 결과 반환
        return res

        # Timeout : 32/48
        # ans = []
        # # 따뜻해질 날 ?
        # for i, temp1 in enumerate(temperatures):
        #     cnt = 0
        #     for j, temp2 in enumerate(temperatures):
        #         if j<=i: continue
        #         cnt += 1
        #         if temp1 < temp2: 
        #             ans.append(cnt)
        #             break
                
        #     else :
        #         ans.append(0)
        # return ans



