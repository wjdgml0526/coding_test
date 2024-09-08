class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # numSet = set(nums) # 체크를 위해 set를 사용
        # longest = 0 

        # for num in nums : 
        #     length = 0
        #     # 시작점의 여부를 체크합니다. 
        #     if (num - 1) not in numSet : 
        #         while (num + length) in numSet:
        #             length += 1 

        #     # 최댓값 갱신
        #     longest = max(longest, length)

        # return longest

        if len(nums) == 0 :
            return 0

        conseq = set()
        nums = sorted(set(nums))
        length = 1
        # print(nums)
        for i in range(1, len(nums)): 
            print(length)
            if nums[i] - nums[i-1] == 1 : 
                length += 1

            else : 
                conseq.add(length)
                length = 1

        conseq.add(length)
        
        return max(conseq)

        