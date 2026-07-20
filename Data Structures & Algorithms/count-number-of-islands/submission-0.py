class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        number_islands = 0
        visited = set()
        queue = collections.deque()

        def bfs(spot, matrix):
            # print("Running BFS at ", spot)
            visited.add(spot)
            # add all the spots up, down, left, right to the back queue

            queue.append((spot[0] - 1 , spot[1]))
            queue.append((spot[0] + 1, spot[1]))
            queue.append((spot[0], spot[1] + 1))
            queue.append((spot[0], spot[1] - 1))

            # take off the front of the queue and if 
            # - (the spot is in the range of the matrix) and (not in visited) and (value is equal to 1)
            # run bfs on it
            while queue:
                spot_checking = queue.popleft()

                if (spot_checking[0] in range(len(grid))) and \
                   (spot_checking[1] in range(len(grid[0]))) and \
                   (spot_checking not in visited) and \
                   (matrix[spot_checking[0]][spot_checking[1]] == "1"):
                    bfs(spot_checking, matrix)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                spot = (i,j)

                if grid[i][j] == "1" and spot not in visited:
                    number_islands += 1
                    bfs(spot, grid)

        return number_islands