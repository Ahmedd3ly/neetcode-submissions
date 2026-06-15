class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        deq = deque()
        l = 0

        for r in range(len(nums)):
            #Pop out the smaller value in deq
            while deq and nums[deq[-1]] < nums[r]:
                deq.pop()    
            deq.append(r)

            #Pop out out-ranged variables
            if l > deq[0]:
                deq.popleft()

            #check range and append to res
            if r + 1 >= k:
                res.append(nums[deq[0]])
                l += 1
                
        return res