class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        num2freq = defaultdict(int)
        n = len(nums)
        out = []
        for num in nums:
            num2freq[num]+=1

        def backtrack(seq, hashMap):
            if len(seq) == n:
                out.append(seq[:])
                return

            for num in hashMap:
                if hashMap[num]>0:
                    seq.append(num)
                    hashMap[num]-=1

                    backtrack(seq, hashMap)

                    seq.pop()
                    hashMap[num]+=1

        backtrack([], num2freq)
        return out

        