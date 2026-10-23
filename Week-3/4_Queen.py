
# Name: Ashish Kumar Gupta
# USN: 1WA24CS063
# Experiment: 4-Queens using Hill Climbing

import random

N = 4


def calculate_cost(state):
    cost = 0

    for i in range(N):
        for j in range(i + 1, N):
            if state[i] == state[j]:
                cost += 1
            elif abs(state[i] - state[j]) == abs(i - j):
                cost += 1

    return cost


def display_board(state):
    for row in range(N):
        for col in range(N):
            if state[col] == row:
                print(" Q ", end="")
            else:
                print(" . ", end="")
        print()

    print("Cost:", calculate_cost(state))


def get_neighbors(state):
    neighbors = []

    for col in range(N):
        for row in range(N):
            if row != state[col]:
                neighbor = state.copy()
                neighbor[col] = row
                neighbors.append(neighbor)

    return neighbors


def hill_climbing():
    restart = 0

    while True:
        restart += 1
        current = [random.randrange(N) for _ in range(N)]

        print("\nRestart:", restart)
        print("Initial State:", current)
        print("Initial Cost:", calculate_cost(current))

        while True:
            current_cost = calculate_cost(current)

            if current_cost == 0:
                print("\nGoal State Found!")
                print("Final State:", current)
                display_board(current)
                return current

            neighbors = get_neighbors(current)

            print("\nNeighbor States and Costs:")

            for neighbor in neighbors:
                print(neighbor, "Cost:", calculate_cost(neighbor))

            best_state = min(neighbors, key=calculate_cost)
            best_cost = calculate_cost(best_state)

            if best_cost >= current_cost:
                print("Local minimum reached.")
                print("Restarting...")
                break

            current = best_state

            print("\nNext State:", current)
            display_board(current)


print("=" * 40)
print("4-QUEENS PROBLEM - HILL CLIMBING")
print("=" * 40)
print("Name: Ashish Kumar Gupta")
print("USN: 1WA24CS063")
print("=" * 40)

solution = hill_climbing()

print("\nFinal Solution:", solution)
print("Final Cost:", calculate_cost(solution))
