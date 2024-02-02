class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        table = {}
        table[0] = []

        for c in candidates:
            for t in range(target + 1):    
                if c == t:
                    if t not in table:
                        table[t] = []
                    table[t].append([c])
                elif t - c in table:
                    for combination in table[t - c]:
                        if t not in table:
                            table[t] = []
                        table[t].append(combination + [c])
            
        if target not in table:
            return []
        else:
            return table[target]

        