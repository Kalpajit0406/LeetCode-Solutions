from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        target_counts = Counter(char.lower() for char in licensePlate if char.isalpha())
        
        best_word = None
        for word in words:
            word_counts = Counter(word)
            if all(word_counts[char] >= count for char, count in target_counts.items()):
                if best_word is None or len(word) < len(best_word):
                    best_word = word
                    
        return best_word