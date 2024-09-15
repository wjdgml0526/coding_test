# 2017 하반기 오전 01번 - 조삼모사
from itertools import combinations, permutations

N = int(input())
P = [list(map(int, input().split())) for _ in range(N)]
WORK_indices = [i for i in range(N)]
min_gap = 1e9
# WORK_indices에서 뽑아서 할당하기 위한 리스트
morning, evening = [], []

def calc_permutation(selected):
    tot = 0
    # 계산해줍니다.
    for comp in list(combinations(selected, N//2)) :

        # 3개 이상 나올 수 있음 -> 다시 한번 더 돌려야 함 [0, 1, 2] -> [01 10 02 20 12 21]
        for candi in list(permutations(comp, 2)):
            i, j =  candi
            tot += P[i][j]

    return tot

# 뽑아진 morning에 대해서 각 일의 합의 차이를 구합니다.
def calc_P():
    global evening
    evening = list(set(WORK_indices) - set(morning))

    p_morning = calc_permutation(morning)
    p_evening = calc_permutation(evening)

    return abs(p_morning-p_evening)


# 뽑아서 morning, evening에 할당합니다.
def choose_task(cnt, cur_idx):
    global min_gap
    if len(morning) == N//2 :
        min_gap = min(min_gap, calc_P())
        return

    if cur_idx == len(WORK_indices):
        return

    morning.append(cur_idx)
    choose_task(cnt + 1, cur_idx+1)
    morning.pop()
    choose_task(cnt, cur_idx+1)

choose_task(0, 0)

print(min_gap)