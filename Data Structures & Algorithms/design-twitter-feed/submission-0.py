from collections import defaultdict
from typing import List
import heapq


class Twitter:

    def __init__(self):
        self.follow_hash = defaultdict(list)
        self.tweet_hash = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_hash[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        res = []

        # User should see their own tweets too
        users = self.follow_hash[userId] + [userId]

        for user in users:
            if self.tweet_hash[user]:
                lastTweetIndex = len(self.tweet_hash[user]) - 1
                time, tweetId = self.tweet_hash[user][lastTweetIndex]

                heapq.heappush(
                    heap,
                    (-time, tweetId, lastTweetIndex, user)
                )

        while heap and len(res) < 10:
            neg_time, tweetId, tweetIndex, user = heapq.heappop(heap)

            res.append(tweetId)

            # Move backwards through this user's tweets
            if tweetIndex > 0:
                prevIndex = tweetIndex - 1
                time, tweetId = self.tweet_hash[user][prevIndex]

                heapq.heappush(
                    heap,
                    (-time, tweetId, prevIndex, user)
                )

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.follow_hash[followerId]:
            self.follow_hash[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_hash[followerId]:
            self.follow_hash[followerId].remove(followeeId)