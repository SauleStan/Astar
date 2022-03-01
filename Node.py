class Node:
    def __init__(self, state, parent, depth, goalState):
        self.state = state
        self.parent = parent
        self.depth = depth
        self.misplacedNumbers = 0
        self.fval = self.Eval( goalState)
    
    def showState(self):
        output = list(zip(*[iter(self.state)]*3))
        for line in output:
            print(line)
        print("\n")
    
    # Calculates misplaced numbers
    def Misplaced(self, goalState):
        misplaced = 0
        for i in range(len(self.state)):
            if self.state[i] != goalState[i]:
                misplaced += 1
        return misplaced
        
    # Evaluation function.
    # Returns the sum of misplaced numbers and step amount
    def Eval(self, goalState):
        self.misplacedNumbers = self.Misplaced(goalState)
        return self.misplacedNumbers + self.depth

    # Function to check if node is goal node
    def IsGoal(self):
        if self.misplacedNumbers == 0:
            return True

    # When both items in queue are equal, node gives priority to another node
    def __lt__(self, other):
        return self.fval < other.fval
