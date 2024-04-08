class Solution:
    def hIndex(self, citations: List[int]) -> int:
        ret = []
        citations.sort(reverse=True)

        for i in range(len(citations)):
            ret.append(min(citations[i], (i + 1)))

        return max(ret)