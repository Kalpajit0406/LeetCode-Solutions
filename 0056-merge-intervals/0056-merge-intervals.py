from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Step 1: Sort the intervals by their start times
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        
        for interval in intervals:
            # If the list of merged intervals is empty or if the current 
            # interval does not overlap with the previous, append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # There is an overlap, so merge the current interval with the previous one
                # by updating the end time to the maximum of both end times.
                merged[-1][1] = max(merged[-1][1], interval[1])
                
        return merged