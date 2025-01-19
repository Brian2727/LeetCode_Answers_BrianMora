from _heapq import heappush, heappop

from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:

        Rows, Cols = len(heightMap), len(heightMap[0])

        min_heap = []

        # We add all of the corner values to the MinHeap  in order to traverse the values that we know for sure do no have water.
        for r in range(Rows):
            for c in range(Cols):
                if r in [0, Rows - 1] or c in [0, Cols - 1]:
                    heappush(min_heap, (heightMap[r][c], r, c))
                    heightMap[r][c] = -1

        res = 0
        max_h = -1

        while min_heap:
            h, r, c = heappop(min_heap)
            max_h = max(max_h, h)
            res += max_h - h

            neighbors = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
            for nr, nc in neighbors:
                if nr < 0 or nc < 0 or nr == Rows or nc == Cols or heightMap[nr][nc] == -1:
                    continue
                else:
                    heappush(min_heap, (heightMap[nr][nc], nr, nc))
                    heightMap[nr][nc] = -1

        return res
