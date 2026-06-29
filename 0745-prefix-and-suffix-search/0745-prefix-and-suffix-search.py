class TrieNode:
    def __init__(self):
        self.children = {}
        self.weight = -1

class WordFilter:

    def __init__(self, words: List[str]):
        self.root = TrieNode()
        for index, word in enumerate(words):
            n = len(word)
            for i in range(n + 1):
                suffix = word[i:]
                combined = suffix + '#' + word
                curr = self.root
                curr.weight = index
                for char in combined:
                    if char not in curr.children:
                        curr.children[char] = TrieNode()
                    curr = curr.children[char]
                    curr.weight = index  # <-- Fixed: Update the weight for every character node

    def f(self, pref: str, suff: str) -> int:
        curr = self.root
        search_str = suff + '#' + pref
        for char in search_str:
            if char not in curr.children:
                return -1
            curr = curr.children[char]
        return curr.weight