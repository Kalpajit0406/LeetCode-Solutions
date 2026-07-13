class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memo = {}
        
        def backtrack(start):
            if start in memo:
                return memo[start]
            if start == len(s):
                return [""]
                
            res = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    sub_sentences = backtrack(end)
                    for sub in sub_sentences:
                        if sub:
                            res.append(word + " " + sub)
                        else:
                            res.append(word)
                            
            memo[start] = res
            return res
            
        return backtrack(0)