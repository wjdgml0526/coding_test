class Solution {
public:
    int maxArea(vector<int>& height) {
        // 두개의 선을 선택 - 가장 많은 물을 담을 수 있는 용기를 찾기
        // 용기의 너비 - 두선 사이의 거리 / 높이 - 낮은 선의 높이

        int maxArea = 0;
        int left =0;
        int right = height.size() - 1;

        while (left < right){
            maxArea = max(maxArea, (right - left) * min(height[left], height[right]));

            if (height[left] < height[right]){
                left++;
            } else{
                right --;
            }


        }      
        return maxArea;
    }
};