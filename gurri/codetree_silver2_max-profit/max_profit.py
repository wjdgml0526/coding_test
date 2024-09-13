

n = int(input())

given_time_profits = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

times = [
    (i, i + time -1 ) # - 1을 해준다 ? 
    for i, (time, _) in enumerate(given_time_profits, start = 1)
]

profits = [
    profit 
    for _, profit in given_time_profits
]

selected_jobs = []
max_profit = 0

def get_profit():
    return sum(
        [profits[job_idx] for
        job_idx in selected_jobs]
    )

# 가능여부 검사하기
def is_available():
    for i in range(len(selected_jobs) -1):
        _, end_time = times[selected_jobs[i]]
        start_time, _ = times[selected_jobs[i+1]]
        if end_time >= start_time:
            return False
    
    for job_idx in selected_jobs:
        _, end_time = times[job_idx]
        if end_time > n:
            return False
            
    return True

def find_max_profit(curr_idx):
    global max_profit

    if curr_idx == n : 
        if is_available():
            max_profit = max(max_profit, get_profit())
        return
    
    find_max_profit(curr_idx + 1)

    selected_jobs.append(curr_idx)
    find_max_profit(curr_idx + 1)
    selected_jobs.pop()

find_max_profit(0)
print(max_profit)