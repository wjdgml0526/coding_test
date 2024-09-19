class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        // 요구사항 : 주어진 배열에서 합이 0 되는 세개의 숫자를 모두 찾기

        // 정렬 진행 - O(nlogn)
        sort(nums.begin(), nums.end());
        vector<vector<int>> ans;
        // O(n^2)
        for (int i=0; i<nums.size();i++){

            if (i>0 && nums[i] == nums[i-1]) continue;
            int j = i+1;
            int k = nums.size() -1;

            while (j<k)
            {
                int sum = nums[i] + nums[j] + nums[k];
                if (sum < 0) j++;
                else if (sum > 0) k--;
                else // 같을 경우
                {
                    vector<int>temp = {nums[i], nums[j], nums[k]};
                    ans.push_back(temp);
                    j++;
                    k--;
                    while (j<k && nums[j] == nums[j-1])j++;
                    while (j<k && nums[k] == nums[k+1])k--;
                }   
            }    
        }
        return ans;
    }
};