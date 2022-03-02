#include <iostream>
#include <vector>

using namespace std;

class Solution {
    public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() - 1;
        
        while(nums[left] + nums[right] != target) {
            if (nums[right] > target) right -= 1;
            else if (nums[left] + nums[right] < target) left += 1;
        }
        
        return {left, right};
    }
};