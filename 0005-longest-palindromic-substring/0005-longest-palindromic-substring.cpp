#include <string>
#include <algorithm>

class Solution {
public:
    std::string longestPalindrome(std::string s) {
        if (s.empty()) return "";
        
        int start = 0; // Tracks the starting index of the longest palindrome found
        int maxLength = 0; // Tracks the length of the longest palindrome found
        
        // Helper lambda function to expand around a given center
        auto expandAroundCenter = [&](int left, int right) {
            while (left >= 0 && right < s.length() && s[left] == s[right]) {
                left--;
                right++;
            }
            // Return the length of the palindrome found
            // (right - 1) - (left + 1) + 1 = right - left - 1
            return right - left - 1;
        };
        
        for (int i = 0; i < s.length(); ++i) {
            // Case 1: Odd length palindrome (centered at i)
            int len1 = expandAroundCenter(i, i);
            
            // Case 2: Even length palindrome (centered between i and i+1)
            int len2 = expandAroundCenter(i, i + 1);
            
            // Get the maximum length found at the current center
            int len = std::max(len1, len2);
            
            // If it's longer than our previous maximum, update boundaries
            if (len > maxLength) {
                maxLength = len;
                // Calculate the start index based on the center i and the length
                start = i - (len - 1) / 2;
            }
        }
        
        return s.substr(start, maxLength);
    }
};