class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;
        int n = nums.size();
        
        // 1. Sort the array to use the two-pointer technique and skip duplicates
        sort(nums.begin(), nums.end());
        
        for (int i = 0; i < n - 2; i++) {
            // If the current starting number is greater than 0, 
            // no three numbers can sum up to 0 anymore.
            if (nums[i] > 0) break;
            
            // Skip duplicate values for the first element
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            
            int left = i + 1;
            int right = n - 1;
            
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                
                if (sum == 0) {
                    result.push_back({nums[i], nums[left], nums[right]});
                    
                    // Skip duplicates for the second element
                    while (left < right && nums[left] == nums[left + 1]) left++;
                    // Skip duplicates for the third element
                    while (left < right && nums[right] == nums[right - 1]) right--;
                    
                    // Move both pointers after finding a valid triplet
                    left++;
                    right--;
                } 
                else if (sum < 0) {
                    // Sum is too small, move the left pointer to increase the value
                    left++;
                } 
                else {
                    // Sum is too large, move the right pointer to decrease the value
                    right--;
                }
            }
        }
        
        return result;
    }
};