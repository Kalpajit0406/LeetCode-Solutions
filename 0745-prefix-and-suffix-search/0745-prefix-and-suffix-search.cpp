#include <vector>
#include <string>
#include <unordered_map>

using namespace std;
struct TrieNode {
    unordered_map<char, TrieNode*> children;
    int weight = -1; 
};

class WordFilter {
private:
    TrieNode* root;

public:
    WordFilter(vector<string>& words) {
        root = new TrieNode();
        
        for (int index = 0; index < words.size(); ++index) {
            string word = words[index];
            int n = word.length();
            for (int i = 0; i <= n; ++i) {
                string suffix = word.substr(i);
                string combined = suffix + '#' + word;
                
                TrieNode* curr = root;
                curr->weight = index;
                for (char c : combined) {
                    if (curr->children.find(c) == curr->children.end()) {
                        curr->children[c] = new TrieNode();
                    }
                    curr = curr->children[c];
                    curr->weight = index; 
                }
            }
        }
    }
    
    int f(string pref, string suff) {
        TrieNode* curr = root;
        string search_str = suff + '#' + pref;
        for (char c : search_str) {
            if (curr->children.find(c) == curr->children.end()) {
                return -1;
            }
            curr = curr->children[c];
        }
        
        return curr->weight;
    }
};