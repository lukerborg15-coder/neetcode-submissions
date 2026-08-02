class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        multiple = []

        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

        sortcount = sorted(
            count.items(),
            key=lambda pair: pair[1],
            reverse=True
        )

        for pair in sortcount[:k]:
            multiple.append(pair[0])

        return multiple