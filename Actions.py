import numpy as np
def Action(action, state):
    stateArray = np.array(state)
    state2D = stateArray.reshape(3, 3)

    # Get the position of empty spot
    x = np.where(state2D == 0)
    # x is returned as tuple, need to map it to integer for row and column indexes
    row, col = map(int, x)

    if action == "UP":
        if(row <= 0):
            return
        # Temporary store the number to be switched
        temp = state2D[row-1][col]
        # Put the 0 in place of number to switch
        state2D[row-1][col] = 0

    elif action == "DOWN":
        if(row >= 2):
            return
        temp = state2D[row+1][col]
        state2D[row+1][col] = 0

    elif action == "LEFT":
        if(col <= 0):
            return
        temp = state2D[row][col-1]
        state2D[row][col-1] = 0

    elif action == "RIGHT":
        if(col >= 2):
            return
        temp = state2D[row][col+1]
        state2D[row][col+1] = 0
    else:
        print("Unknown action, nothing happened")
        return state

    # Put temp number in place of 0
    state2D[row][col] = temp
    newState = state2D.reshape(9).tolist()
    # Return changed state
    return newState