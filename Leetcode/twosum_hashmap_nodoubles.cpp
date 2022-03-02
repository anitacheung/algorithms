#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
    public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map;
        int index = 0;
        int first, second = 0;
        int diff = 0;
        
        for (int n:nums) {
            map[n] = index;
            index += 1;
        }
        
        for (int i = 0; i < nums.size(); i++) {
            diff = target - nums[i];
            if ((map.count(diff) > 0) & (diff != nums[i])) {
                first = i;
                second = map[diff];
                break;
            }
        }
        
        return {first, second};
    }
};