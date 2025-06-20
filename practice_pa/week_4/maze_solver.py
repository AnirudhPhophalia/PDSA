# Alice wants to find the key in a maze and get out of it. The maze representation is given below, where X represents walls, space represents the allowed tiles Alice can walk on and 🗝 represents the tile that has the key.

# There is only one tile opening in the left-most vertical wall, where Alice is initially standing.

# Similarly there is only one tile opening in the right-most vertical wall, from which Alice has to exit.

# Alice can travel horizontally or vertically, but cannot travel diagonally. Moving to adjacent tile vertically or horizontally is counted as a step.

# There are three possible outcomes, either you can exit the maze after getting the key, or the key is not reachable or the finish tile is not reachable.

# Print the minimum number of steps Alice requires to reach the finish tile traveling through tile having the key.

# If the key tile is not reachable then print -1.

# If the key tile is reachable but finish tile is not reachable then print -2.



from collections import deque
import sys

def bfs(start, target, maze):
    R, C = len(maze), len(maze[0])
    queue = deque([(start[0], start[1], 0)])
    visited = [[False]*C for _ in range(R)]
    visited[start[0]][start[1]] = True
    directions = [(0,1), (0,-1), (1,0), (-1,0)]

    while queue:
        x, y, dist = queue.popleft()
        if (x, y) == target:
            return dist
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and maze[nx][ny] in [' ', '*']:
                visited[nx][ny] = True
                queue.append((nx, ny, dist+1))
    return -1

def find_positions(maze):
    R, C = len(maze), len(maze[0])
    entrance = exit = key = None

    for i in range(R):
        if maze[i][0] == ' ':
            entrance = (i, 0)
        if maze[i][C-1] == ' ':
            exit = (i, C-1)
        for j in range(C):
            if maze[i][j] == '*':
                key = (i, j)
    return entrance, key, exit

# Read maze input and pad all lines to the max width
lines = [line.rstrip('\n') for line in sys.stdin if line.strip()]
max_len = max(len(line) for line in lines)
maze = [list(line.ljust(max_len)) for line in lines]

entrance, key, exit = find_positions(maze)

if key is None or entrance is None or exit is None:
    print(-1)
else:
    steps_to_key = bfs(entrance, key, maze)
    if steps_to_key == -1:
        print(-1)
    else:
        steps_to_exit = bfs(key, exit, maze)
        if steps_to_exit == -1:
            print(-2)
        else:
            print(steps_to_key + steps_to_exit)
