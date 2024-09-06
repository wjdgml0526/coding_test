class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #lst = []
        # 파이썬 중복 제거 배열 만들기
        #rm_dup_nums = list(set(nums))
        #print(rm_dup_nums)

        #dict_tmp = {}
        #for i in rm_dup_nums :
        #    dict[i] = nums.count(i)

        # 오름차순 정렬 예시
        #sorted_dict = dict(sorted(dict_tmp.items(), key=lambda x: x[1]))

        #for j in range(k) :
        #    lst.append(sorted_dict)

    # Step 1: Create a dictionary to store the frequency of each number
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
    
    # Step 2: Sort the dictionary items based on their frequency in descending order
        sorted_items = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)
    
    # Step 3: Return the first k keys from the sorted dictionary items
        return [item[0] for item in sorted_items[:k]]
 
    # Test cases
    #print(topKFrequent([1,1,1,2,2,3], 2))  # [1,2]
    #print(topKFrequent([1], 1))  # [1]
            
        