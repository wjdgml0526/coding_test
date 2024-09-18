class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Car fleet - 차량 군집 
        # 선두 차량이 느리면, 뒤의 차들이 합류해서 속도가 같아지는 그룹임.

        # 1. 자동차 정렬 - 위치 기준
        cars = sorted(zip(position, speed), reverse=True)

        # 2. 각 차의 도착시간 계산 - (목적지 - 현재위치) / 속도
        # 3. 스택을 통해 군집을 계산합니다. - 각 자동차의 도착 시간을 계산해서 스택에 넣음
        # 가장 가까운 차 부터 도착시간을 기록하고,
        # 각 자동차가 스택에 있는 차와 비교해서 더 느리다면, 군집 형성
        # 더 빠른 차라면 새로 군집 생성 - 스택에 추가
        
        stack = []
        for pos, spd in cars:
            time = (target - pos) / spd
            # 새로운 군집이라면 스택에 넣기
            if not stack or time > stack[-1]:
                stack.append(time)
        
        # 최종 군집 수 반환
        return len(stack)


