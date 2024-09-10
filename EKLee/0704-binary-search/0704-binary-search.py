class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        tf_idx = -1
        for idx in range(len(nums)) :
            if nums[idx] == target :
                tf_idx = idx
                break
        return tf_idx

        