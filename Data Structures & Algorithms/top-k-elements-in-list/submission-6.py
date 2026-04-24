class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict(Counter(nums))
        out = []

        while len(out)<k:
            keys = [k for k, v in d.items() if v == max(d.values())]
            d.pop(keys[0])
            out.append(keys[0])
        return out
        