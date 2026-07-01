class Solution {
private:
    // Mapping of digits to letters corresponding to telephone buttons
    const vector<string> mapping = {
        "",     // 0
        "",     // 1
        "abc",  // 2
        "def",  // 3
        "ghi",  // 4
        "jkl",  // 5
        "mno",  // 6
        "pqrs", // 7
        "tuv",  // 8
        "wxyz"  // 9
    };

    void backtrack(string& digits, int index, string& current, vector<string>& result) {
        // Base case: if the current combination is of the same length as digits, we found a valid combination
        if (index == digits.length()) {
            result.push_back(current);
            return;
        }

        // Get the letters corresponding to the current digit
        string letters = mapping[digits[index] - '0'];
        
        // Loop through each letter and recurse
        for (char c : letters) {
            current.push_back(c);                 // Choose
            backtrack(digits, index + 1, current, result); // Explore
            current.pop_back();                  // Unchoose (Backtrack)
        }
    }

public:
    vector<string> letterCombinations(string digits) {
        vector<string> result;
        
        // Edge case: if the input is empty, return an empty list
        if (digits.empty()) {
            return result;
        }
        
        string current = "";
        backtrack(digits, 0, current, result);
        return result;
    }
};