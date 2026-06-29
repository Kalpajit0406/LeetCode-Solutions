class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        m, n = len(isInfected), len(isInfected[0])
        total_walls = 0
        
        while True:
            visited = [[False] * n for _ in range(m)]
            regions = []
            frontiers = []
            perimeters = []
            
            # Step 1: Find all distinct infected components
            for r in range(m):
                for c in range(n):
                    if isInfected[r][c] == 1 and not visited[r][c]:
                        # Start a BFS/DFS for the current region
                        region = []
                        frontier = set()
                        perimeter = 0
                        
                        queue = [(r, c)]
                        visited[r][c] = True
                        
                        while queue:
                            curr_r, curr_c = queue.pop(0)
                            region.append((curr_r, curr_c))
                            
                            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                                nr, nc = curr_r + dr, curr_c + dc
                                if 0 <= nr < m and 0 <= nc < n:
                                    if isInfected[nr][nc] == 1 and not visited[nr][nc]:
                                        visited[nr][nc] = True
                                        queue.append((nr, nc))
                                    elif isInfected[nr][nc] == 0:
                                        frontier.add((nr, nc))
                                        perimeter += 1
                                        
                        if region:
                            regions.append(region)
                            frontiers.append(frontier)
                            perimeters.append(perimeter)
            
            # If no active viral regions are found, containment is complete
            if not regions:
                break
                
            # Step 2: Find the region that threatens the most uninfected cells
            max_threat_idx = 0
            for i in range(1, len(frontiers)):
                if len(frontiers[i]) > len(frontiers[max_threat_idx]):
                    max_threat_idx = i
                    
            # If the worst region threatens 0 cells, no more walls are needed
            if len(frontiers[max_threat_idx]) == 0:
                break
                
            # Quarantine the most threatening region (-1 signifies quarantined)
            total_walls += perimeters[max_threat_idx]
            for r, c in regions[max_threat_idx]:
                isInfected[r][c] = -1
                
            # Step 3: Spread the remaining active viral regions
            for i in range(len(regions)):
                if i == max_threat_idx:
                    continue
                for r, c in frontiers[i]:
                    isInfected[r][c] = 1
                    
        return total_walls