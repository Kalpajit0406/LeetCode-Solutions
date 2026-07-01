class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        
        for (char c : s) {
            // If it's an opening bracket, push it onto the stack
            if (c == '(' || c == '{' || c == '[') {
                st.push(c);
            } 
            // If it's a closing bracket, check for matching opening bracket
            else {
                if (st.empty()) return false; // Closing bracket with no opening bracket
                
                char top = st.top();
                if ((c == ')' && top == '(') ||
                    (c == '}' && top == '{') ||
                    (c == ']' && top == '[')) {
                    st.pop(); // Valid match, remove from stack
                } else {
                    return false; // Mismatched brackets
                }
            }
        }
        
        // If the stack is empty, all brackets were matched correctly
        return st.empty();
    }
};