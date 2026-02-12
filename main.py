from environment import Grid
from agent import QLAgent
import config

grid = [
    ['S', '.', '.'],
    ['.', '.', '.'],
    ['.', '.', 'G']
]

env = Grid(grid)

agent = QLAgent(
    actions=['UP', 'DOWN', 'LEFT', 'RIGHT'],
    alpha=config.alpha,
    gamma=config.gamma,
    epsilon=config.epsilon_full
)

arrows = {
    "up": "↑",
    "down": "↓",
    "left": "←",
    "right": "→"
}

path_file = open("path_log.txt", "w")

for episode in range(config.eps):
    state = env.reset()
    total_reward = 0
    path = []
    
    for step in range(config.max_steps):
        valid_actions = env.get_valid_actions(state)
        action = agent.choose_action(state, valid_actions)

        next_state, reward, done = env.step(action)
        arrow = arrows[action]
        path.append(arrow)
        next_actions = env.get_valid_actions(next_state)

        agent.learn(state, action, reward, next_state, next_actions)

        state = next_state
        total_reward += reward

        if done:
            break

    agent.epsilon = max(
        config.epsilon_min,
        agent.epsilon * config.epsilon_decay
    )

    path_file.write(f"Episode: {episode+1}\n")
    path_file.write(f"Steps: {len(path)-1}\n")
    path_file.write(f"Total reward: {total_reward}\n")
    path_file.write(f"Path:")
    for p in path:
        path_file.write(p)
    path_file.write("\n")
    path_file.write("="*70)
    path_file.write("\n")

path_file.close()
    #if episode % 5 == 0:
    #    print(f"Episode {episode}, reward: {total_reward}")