# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.qSort(pairs, 0, len(pairs)-1)
        return pairs

    def qSort(self, pairs: List[Pair], start, length):
        p_len = len(pairs)
        e = p_len - 1
        s = 0
        res = []
        pivot = pairs[e].key
        left = s

        if e - s + 1 <= 1:
            return res.append(pairs[:])

        for i in range(s, p_len):
            if (pairs[i].key < pivot):
                temp = pairs[i].key
                pairs[left].key = pairs[i].key
                pairs[i].key = temp
                left+=1
        
        pairs[left].key = pivot
        pairs[e].key = pairs[left].key

        self.quickSort(pairs[s:left-1])
        self.quickSort(pairs[left+1:e])

        return res.append(pairs[0:e])

# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    # Implementation of Quick Sort
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs) - 1)
        return pairs

    def quickSortHelper(self, arr: List[Pair], s: int, e: int) -> None:
        if e - s + 1 <= 1:
            return

        pivot = arr[e] # pivot is the last element
        left = s # pointer for left side

        # Partition: elements smaller than pivot on left side
        for i in range(s, e):
            if arr[i].key < pivot.key:
                tmp = arr[left]
                arr[left] = arr[i]
                arr[i] = tmp
                left += 1

        # Move pivot in-between left & right sides
        arr[e] = arr[left]
        arr[left] = pivot
        
        # Quick sort left side
        self.quickSortHelper(arr, s, left - 1)

        # Quick sort right side
        self.quickSortHelper(arr, left + 1, e)
    