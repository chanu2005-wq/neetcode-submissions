from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        if not rooms:
            return

        ROWS, COLS = len(rooms), len(rooms[0])
        INF = 2147483647

        # Queue for BFS
        q = deque()

        # Step 1: Add all gates to the queue
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append((r, c))

        # Four possible directions
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Step 2: Perform Multi-Source BFS
        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Check boundaries and only visit INF rooms
                if (
                    0 <= nr < ROWS and
                    0 <= nc < COLS and
                    rooms[nr][nc] == INF
                ):
                    rooms[nr][nc] = rooms[r][c] + 1
                    q.append((nr, nc))

