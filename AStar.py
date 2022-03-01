import heapq
from Node import Node
from PriorityEntry import PriorityEntry
from Actions import Action

initialState = [2, 3, 7, 1, 4, 8, 0, 5, 6]
# initialState = [0, 1, 3, 4, 2, 6, 7, 5, 8]
goalState = [1, 2, 3, 4, 5, 6, 7, 8, 0]
depth = 0

# Starting node
initialNode = Node(initialState, None, depth, goalState)

#  Function to recursively return the states from the start node to the supplied node
def Solution(node):
    if(node.parent != None):
        Solution(node.parent)
    node.showState()

# Use heap as frontier list for priority queue behaviour
frontier = []
heapq.heappush(frontier, (initialNode.fval, initialNode.state, initialNode))

# Put initial node into queue using fval of the node as priority 
# frontier.put(PriorityEntry(initialNode.fval, initialNode))

# Set of explored nodes
explored = []

if __name__ == "__main__":
    actions = ["UP", "DOWN", "LEFT", "RIGHT"]
    currentState = initialState


    while True:
        if len(frontier) == 0:
            break
        
        currentNode = heapq.heappop(frontier)[2]

        # If there are no more misplaced tiles, the state is returned
        if currentNode.IsGoal():
            Solution(currentNode)
            break

        # If node is not goal, add it to explored list
        explored.append(currentNode)

        # Loop through actions
        for action in actions:
            # Get new state from action
            currentState = Action(action, currentNode.state)
            # If action doesn't return a node, continue to next action
            if currentState == None:
                continue
            # Create child node with the new state
            childNode= Node(currentState, currentNode, currentNode.depth+1, goalState)
            # If child node doesn't exist in explored set or frontier, add it to the frontier
            if not(any(childNode.state == item.state for item in explored) or any(childNode.state in item for item in frontier)):
                heapq.heappush(frontier, (childNode.fval, childNode.state, childNode))
        
        
            
