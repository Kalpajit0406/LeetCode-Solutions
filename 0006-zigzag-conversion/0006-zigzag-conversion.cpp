#include <string>
#include <vector>

class Solution {
public:
    std::string convert(std::string s, int numRows) {
        // Base case: if numRows is 1 or greater than/equal to the string length, 
        // the zigzag pattern matches the original string.
        if (numRows == 1 || numRows >= s.length()) {
            return s;
        }
        
        // Create a vector of strings to hold characters for each row
        std::vector<std::string> rows(std::min(int(s.length()), numRows));
        int currRow = 0;
        bool goingDown = false;
        
        for (char c : s) {
            rows[currRow] += c;
            
            // Turn around if we hit the top or bottom row boundary
            if (currRow == 0 || currRow == numRows - 1) {
                goingDown = !goingDown;
            }
            
            // Move up or down based on the current direction flag
            currRow += goingDown ? 1 : -1;
        }
        
        // Combine all individual rows into a single string
        std::string result;
        for (const std::string& row : rows) {
            result += row;
        }
        
        return result;
    }
};