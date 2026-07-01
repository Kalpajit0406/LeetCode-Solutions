class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> result;
        int n = nums.size();
        
        // 1. Sort the array to easily handle duplicates and use two pointers
        sort(nums.begin(), nums.end());
        
        // Fix the first element
        for (int i = 0; i < n - 3; i++) {
            // Skip duplicate values for the first element
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            
            // Fix the second element
            for (int j = i + 1; j < n - 2; j++) {
                // Skip duplicate values for the second element
                if (j > i + 1 && nums[j] == nums[j - 1]) continue;
                
                // Two pointers for the remaining two elements
                int left = j + 1;
                int right = n - 1;
                
                while (left < right) {
                    // Use long long to prevent integer overflow
                    long long sum = (long long)nums[i] + nums[j] + nums[left] + nums[right];
                    
                    if (sum == target) {
                        result.push_back({nums[i], nums[j], nums[left], nums[right]});
                        
                        // Skip duplicate values for the third element
                        while (left < right && nums[left] == nums[left + 1]) left++;
                        // Skip duplicate values for the fourth element
                        while (left < right && nums[right] == nums[right - 1]) right--;
                        
                        left++;
                        right--;
                    } 
                    else if (sum < target) {
                        left++; // Need a larger sum
                    } 
                    else {
                        right--; // Need a smaller sum
                    }
                }
            }
        }
        
        return result;
    }
};