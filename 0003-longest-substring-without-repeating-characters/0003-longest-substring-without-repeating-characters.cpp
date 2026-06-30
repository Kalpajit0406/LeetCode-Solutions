#include <string>
#include <vector>
#include <algorithm>

class Solution {
public:
    int lengthOfLongestSubstring(std::string s) {
        // Vector to store the last seen index of each ASCII character.
        // Initialized to -1 to indicate that no characters have been seen yet.
        std::vector<int> charIndex(128, -1);
        
        int maxLength = 0;
        int left = 0; // Left boundary of the sliding window
        
        for (int right = 0; right < s.length(); ++right) {
            // If the character was seen inside the current window, move the left boundary
            if (charIndex[s[right]] >= left) {
                left = charIndex[s[right]] + 1;
            }
            
            // Update the last seen position of the current character
            charIndex[s[right]] = right;
            
            // Calculate and update the maximum length of the valid window
            maxLength = std::max(maxLength, right - left + 1);
        }
        
        return maxLength;
    }
};