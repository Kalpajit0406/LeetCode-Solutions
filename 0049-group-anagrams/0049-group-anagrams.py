from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initialize a default dictionary where values are lists
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Sort the string to create a unique key for anagrams
            # sorted("eat") -> ['a', 'e', 't']. We join it back to a string "aet"
            sorted_key = "".join(sorted(s))
            
            # Append the original string to the corresponding key
            anagram_map[sorted_key].append(s)
            
        # Return all the grouped lists
        return list(anagram_map.values())