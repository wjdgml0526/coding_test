n = int(input())
nums=list(map(int, input().split()))
ops=list(map(int, input().split()))
import sys

maxi, mini = -sys.maxsize, sys.maxsize

op_dict = {0:'+', 1:'-', 2:'*'}

# 정수 nums는 순서를 바꿀 수 없음
# 연산자 배치는 변경 가능 
# 1 5 3 => 1+5-3 = 3 , 1-5+3 = -1;
# 시간복잡도 : 11개 정수 : 10개의 연산자 칸
selected = []

def calc(selected):
    val = nums[0]
    
    for idx, num in enumerate(nums[1:]):
        equ = ""
        equ += str(val)
        op = op_dict[selected[idx]]
        equ += op
        equ += str(num)
        # print(equ)
        val = eval(equ)

    return val

def backtracking(cnt:int) -> None:
    global maxi, mini
    # base cond
    if cnt == n-1 : 
        val = calc(selected)
        maxi, mini = max(maxi, val), min(mini, val)
        return
    
    for idx in range(len(ops)):
        if ops[idx] > 0 : 
            selected.append(idx)
            ops[idx] -= 1
            backtracking(cnt+1)
            selected.pop()
            ops[idx] += 1

# backtracking
backtracking(0) # 인수 : 선택 된 연산자의 수
print(mini, maxi)