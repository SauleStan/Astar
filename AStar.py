import heapq
from Node import Node
from Actions import Action

#  Function to recursively return the states from the start node to the supplied node
def Solution(node):
    if(node.parent != None):
        Solution(node.parent)
    print("Step: ", node.depth)
    node.showState()

# Function to check whether puzzle is solvable
# Inversion count on the state list should be even, then puzzle is solvable
def IsSolvable(state):
    inversions = 0
    for i in range(len(state)):
        if(state[i]==0):
            continue
        for j in range(i,len(state)):
            if(state[j]==0):
                continue
            if(state[i]>state[j]):
                inversions += 1
    
    # If inversions count is not even, puzzle is not solvable
    if (inversions % 2) != 0:
        return False
    else:
        return True

if __name__ == "__main__":
    initialState = [2, 3, 7, 1, 4, 8, 0, 6, 5]
    goalState = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    depth = 0

    # Starting node
    initialNode = Node(initialState, None, depth, goalState)

    # Use heap as frontier list for priority queue behaviour
    frontier = []
    heapq.heappush(frontier, (initialNode.fval, initialNode.state, initialNode))

    # Set of explored nodes
    explored = []

    # Availbale actions to perform on the game state
    actions = ["UP", "DOWN", "LEFT", "RIGHT"]
    
    # If initial state is unsolvable, stops the program
    solvable = IsSolvable(initialState)
    if (not solvable):
        print("Initial state is unsolvable.")
        quit()

    while True:
        # If frontier is empty, stops the program
        if len(frontier) == 0:
            break
        
        # Gets the smallest cost node from the frontier
        currentNode = heapq.heappop(frontier)[2]

        # If there are no more misplaced tiles, the solution is displayed
        if currentNode.IsGoal():
            Solution(currentNode)
            break

        # If node is not goal, add it to explored list
        explored.append(currentNode)

        # Perform actions
        for action in actions:
            # Get new state from action
            currentState = Action(action, currentNode.state)
            # When action is not possible, returns null, continue to next action
            if currentState == None:
                continue
            # Create child node with the new state
            childNode= Node(currentState, currentNode, currentNode.depth+1, goalState)
            # If child node doesn't exist in explored set or frontier, add it to the frontier
            if not(any(childNode.state == item.state for item in explored) or any(childNode.state in item for item in frontier)):
                heapq.heappush(frontier, (childNode.fval, childNode.state, childNode))