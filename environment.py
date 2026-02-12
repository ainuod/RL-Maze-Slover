
# moves
ACTIONS = {
    "up": (-1,0),
    "right": (0,1),
    "down": (1,0),
    "left": (0,-1)
}

# the grid lol
class Grid:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.start = self.find_sym('S')
        self.goal = self.find_sym('G')
        self.reset()

    #function to look for a given symbol
    def find_sym(self, symbol):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] == symbol:
                    return (r,c)
        raise ValueError(f"{symbol} does not exist in the grid")

    #function to reset the agent's position
    def reset(self):
        self.agent_pos = self.start
        return self.agent_pos

    #function to check whether the current position is valid or not
    def valid_pos(self, r, c):
        if r >= 0 and r < self.rows and c >= 0 and c < self.cols:
            return True
        else:
            return False

    #function to see what actions possible are from the current state
    def get_valid_actions(self, state):
        actions = []
        r,c = state
        for action, (dr, dc) in ACTIONS.items():
            nr, nc = r + dc, c + dc
            if self.valid_pos(nr,nc):
                actions.append(action)
        return actions

    #function to run the given action and update the agent's position
    def step(self, action):
        dr, dc = ACTIONS[action]
        r, c = self.agent_pos
        nr, nc = r + dr, c + dc
        
        if not self.valid_pos(nr, nc):
            return self.agent_pos, -1, False

        self.agent_pos = (nr, nc)

        if self.agent_pos == self.goal:
            return self.agent_pos, 10, True

        return self.agent_pos, -1, False

    