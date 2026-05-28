class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequencies
        count = {}

        for c in nums:
            count[c] = 1 + count.get(c, 0)

        heap = []

        # Maintain min-heap of size k
        for num, freq in count.items():

            heapq.heappush(heap, (freq, num))

            if len(heap) > k:
                heapq.heappop(heap)

        # Extract numbers
        return [num for freq, num in heap]
