class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        ds = []
        n = len(candidates)
        candidates.sort()
        
        def combinationSum2Help(ind, t, ds, ans, arr, n):
            if t == 0:
                ans.append(ds[:])
                return
            for i in range(ind, n):
                if i!=ind and arr[i]==arr[i-1]:
                    continue
                if arr[i]>t:
                    break
                ds.append(arr[i])
                combinationSum2Help(i+1, t-arr[i], ds, ans, arr, n)
                ds.pop()
        combinationSum2Help(0, target, ds, ans, candidates, n)
        return ans