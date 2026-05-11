class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Step 1: Count frequencies
        count = {}

        for n in nums:
            count[n] = 1 + count.get(n,0)

        # Step 2: Create buckets
        freq = [[] for _ in range(len(nums) +1)]

        # Step 3: Fill buckets
        for n, c in count.items():
                freq[c].append(n)

        # Step 4: Collect top k
        res = []

        for i in range(len(freq) -1 , 0, -1):
            for n in freq[i]:
                res.append(n)

            if len(res) == k:
                return res
            
