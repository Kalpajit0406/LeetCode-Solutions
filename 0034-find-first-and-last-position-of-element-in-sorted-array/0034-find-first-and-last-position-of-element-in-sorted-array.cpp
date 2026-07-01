class Solution {
private:
    // Helper function to find the first or last bound of the target
    int findBound(vector<int>& nums, int target, bool isFirst) {
        int low = 0;
        int high = nums.size() - 1;
        int bound = -1;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            
            if (nums[mid] == target) {
                bound = mid; // Record the index
                if (isFirst) {
                    high = mid - 1; // Keep searching left for the first occurrence
                } else {
                    low = mid + 1;  // Keep searching right for the last occurrence
                }
            } 
            else if (nums[mid] < target) {
                low = mid + 1;
            } 
            else {
                high = mid - 1;
            }
        }
        
        return bound;
    }

public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int first = findBound(nums, target, true);
        
        // If the element doesn't exist, no need to search for the last position
        if (first == -1) {
            return {-1, -1};
        }
        
        int last = findBound(nums, target, false);
        
        return {first, last};
    }
};