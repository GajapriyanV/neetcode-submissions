class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        q = deque()  # stores (value, index)
        res = []

        for i, n in enumerate(nums):

            # Maintain decreasing deque
            while q and n >= q[-1][0]:
                q.pop()

            q.append((n, i))

            # Remove max if it's outside the current window
            if i - q[0][1] >= k:
                q.popleft()

            # Only record once window size reaches k
            if i >= k - 1:
                res.append(q[0][0])

        return res