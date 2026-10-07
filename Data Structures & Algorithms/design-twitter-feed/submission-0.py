from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.time=0
        self.tweets=defaultdict(list)
        self.following=defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1
        self.tweets[userId].append((self.time,tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap=[]

        users=set(self.following[userId])
        users.add(userId)

        feed=[]

        for user in users:
            for time,tweetId in self.tweets[user]:
                heapq.heappush(heap,(-time,tweetId))

        feed=[]

        while heap and len(feed)<10:
            _,tweetId=heapq.heappop(heap)
            feed.append(tweetId)

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId!=followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
