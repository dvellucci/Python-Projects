import collections 
import queue
from Board import Board

#BFS search
def bfs(start_board):
    #queue to keep track of frontier
    frontier = collections.deque([start_board])

    #a set is used because we cannot easily check if a node is somewhere in a queue
    frontier_set = {start_board}

    #set to keep track of explored states
    explored = set()

    while len(frontier) > 0:
        #get the next node in the frontier for exploring
        node = frontier.popleft()

        #return the node if it passses the goal test
        if(node.goal_test()):
            return node

        #add the node to the explored set if it is not the goal 
        explored.add(node)

        for neighbor in node.successors():
            if neighbor not in explored and neighbor not in frontier_set:
                frontier.append(neighbor)
                frontier_set.add(neighbor)

    #no goal state could be found
    return None

def dfs(start_board):
    limit = 1

    #set to keep track of explored states
    closed = set()

    #frontier is a set that will be used like a stack
    frontier = [start_board]

    while frontier:
        node = frontier.pop()
        print(node.board)
        if node.depth <= limit:
            #check for goal node
            if(node.goal_test()):
                return node

            if node not in closed: 
                closed.add(node)
                for neighbor in node.successors() and neighbor not in frontier:   
                    frontier.append(neighbor)

    return None


#testing the BFS algorithm
starting_board = [1,4,2,6,5,8,7,3,0]
board = Board(starting_board, None, 0, 0)
result_bfs = bfs(board)
print("Staring Board for BFS:")
print(*starting_board, sep = ", ") 
print("Board result for BFS:")
print(*result_bfs.board, sep = ", ") 
print("Cost of path:", result_bfs.cost)
print("Path to goal:")
print(*result_bfs.actions, sep = ", ") 

#testing the DFS algorithm
starting_board_dfs = [2,8,3,1,6,4,7,0,5]
board_dfs = Board(starting_board_dfs, None, 0, 0)
result_dfs = dfs(board_dfs)
print("Staring Board for DFS:")
print(*starting_board_dfs, sep = ", ") 
print("Board result for DFS:")
print(*result_dfs.board, sep = ", ")
print("Cost of path:", result_dfs.cost)
print("Path to goal:")
print(*result_dfs.actions, sep = ", ") 