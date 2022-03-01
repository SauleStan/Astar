import heapq
from Node import Node

# from Node import Node
initialState = [2, 3, 7, 0, 4, 8, 1, 5, 6]
goalState = [1, 2, 3, 4, 5, 6, 7, 8, 0]
state2 = [2, 0, 7, 3, 4, 8, 1, 5, 6]

step = 0
# node = Node(initialState, None, 0)

# node.showState()

# Starting node
initialNode = Node(initialState, None, step, goalState)
anotherNode = Node(state2, None, step, goalState)

# Priority queue of the nodes to be explored
frontier = []
heapq.heappush(frontier, (initialNode.fval, initialNode.state, initialNode))
heapq.heappush(frontier, (anotherNode.fval, anotherNode.state, anotherNode))

# Put initial node into queue using fval of the node as priority 


node3 = Node(initialState, None, step, goalState)
# print(any(anotherNode.state in item[1].state for item in frontier))

# for item in frontier:   
#     print(anotherNode.state)
#     print(item[1].state)
#     print(anotherNode.state == item[1].state)
# if(any(node3.state in item for item in frontier)):
#     print(heapq.heappop(frontier)[2])

explored = []
explored.append(initialNode)
explored.append(anotherNode)

print(any(node3.state == item.state for item in explored))

x= heapq.heappop(frontier)[2]
print(x.state)

