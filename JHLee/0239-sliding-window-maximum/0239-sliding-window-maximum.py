class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        w_idx = deque()
        result = []
        pl = 0
        for pr in range(len(nums)):
            # nums[pr]보다 작은 값은 모두 window에서 삭제
            while w_idx and nums[w_idx[-1]] < nums[pr]:
                w_idx.pop()
            w_idx.append(pr)

            # window 범위에 들어가지 않는 index 삭제
            if pl > w_idx[0]:
                w_idx.popleft()
            
            # result에 가장 큰 값 저장
            if (pr + 1) >= k:
                result.append(nums[w_idx[0]])
                pl += 1
        return result