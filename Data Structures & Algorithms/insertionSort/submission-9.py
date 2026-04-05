# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        # [(6, a), (5, b), 7c]
        
        res = []
        for i in range(0, len(pairs)):
            key = pairs[i].key
            value = pairs[i].value
            j = i-1
            while j >= 0 and pairs[j].key > pairs[j + 1].key:
                pairs[j], pairs[j + 1] = pairs[j + 1], pairs[j]
                j -= 1
            res.append(pairs[:])

        return res

        

        