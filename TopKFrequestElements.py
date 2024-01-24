# https://leetcode.com/problems/top-k-frequent-elements/description/

import heapq
from collections import Counter

nums = [1,1,1,2,2,3]
k = 2


def topKFrequentElements(nums,k):
    heap = []
    ans = []
    count = Counter(nums)

    for i,v in count.items():
        heapq.heappush(heap,[-v,i])

    while k > 0:
        x = heapq.heappop(heap)
        ans.append(x[1])
        k -= 1

    return ans


print(topKFrequentElements(nums,k))
