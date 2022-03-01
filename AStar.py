import heapq
from Node import Node
from PriorityEntry import PriorityEntry
from Actions import Action

# initialState = [2, 3, 7, 1, 4, 8, 0, 5, 6]
initialState = [1, 2, 3, 4, 5, 6, 7, 0, 8]
goalState = [1, 2, 3, 4, 5, 6, 7, 8, 0]
step = 0

#  Function to recursively return the states from the start node to the supplied node
def Solution(node):
    if(node.parent != None):
        node.parent.showState()
    node.showState()

# Starting node
initialNode = Node(initialState, None, step, goalState)
# Priority queue of the nodes to be explored

# Use heap as frontier list for priority queue behaviour
frontier = []
heapq.heappush(frontier, (initialNode.fval, initialNode.state, initialNode))

# Put initial node into queue using fval of the node as priority 
# frontier.put(PriorityEntry(initialNode.fval, initialNode))

frontier.append(initialNode)

# Set of explored nodes
explored = []

if __name__ == "__main__":
    actions = ["UP", "DOWN", "LEFT", "RIGHT"]
    currentState = initialState
    while(True):
        if len(frontier) == 0:
            break
        
        currentNode = heapq.heappop(frontier)[2]
        
        # If there are no more misplaced tiles, the state is returned
        if currentNode.IsGoal():
            Solution(currentNode)
            # node.showState()

        # If node is not goal, add it to explored list
        explored.append(currentNode)

        # Loop through actions
        for action in actions:
            # Get new state from action
            currentState = Action(action, currentState)
            # Create child node with the new state
            childNode= Node(currentState, currentNode, currentNode.depth+1, goalState)
            
            # If child node doesn't exist in explored set or frontier, add it to the frontier
            if not((childNode.state == item.state for item in explored) or any(childNode.state in item for item in frontier)):
                frontier.put(PriorityEntry(childNode.fval, childNode))
            
