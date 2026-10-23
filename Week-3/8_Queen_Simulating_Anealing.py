
# Name: Ashish Kumar Gupta
# USN: 1WA24CS063
# Experiment: 8-Queens using Simulated Annealing

import random
import math

N = 8


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


def get_random_neighbor(state):
    neighbor = state.copy()

    col = random.randrange(N)
    new_row = random.randrange(N - 1)

    if new_row >= neighbor[col]:
        new_row += 1

    neighbor[col] = new_row
    return neighbor


def simulated_annealing():
    max_restarts = 100
    max_steps = 20000

    for restart in range(1, max_restarts + 1):
        current = [random.randrange(N) for _ in range(N)]
        current_cost = calculate_cost(current)

        temperature = 10.0
        cooling_rate = 0.995

        print("\nRestart:", restart)
        print("Initial State:", current)
        print("Initial Cost:", current_cost)

        for step in range(1, max_steps + 1):

            if current_cost == 0:
                print("\nGoal State Found!")
                print("Steps:", step)
                print("Final State:", current)
                display_board(current)
                return current

            neighbor = get_random_neighbor(current)
            neighbor_cost = calculate_cost(neighbor)

            delta_e = current_cost - neighbor_cost

            if delta_e > 0:
                current = neighbor
                current_cost = neighbor_cost
            else:
                probability = math.exp(delta_e / temperature)

                if random.random() < probability:
                    current = neighbor
                    current_cost = neighbor_cost

            temperature *= cooling_rate

            if temperature < 0.0001:
                break

        print("Cost after restart:", current_cost)

    print("\nNo solution found within the restart limit.")
    return None


print("=" * 45)
print("8-QUEENS PROBLEM - SIMULATED ANNEALING")
print("=" * 45)
print("Name: Ashish Kumar Gupta")
print("USN: 1WA24CS063")
print("=" * 45)

solution = simulated_annealing()

if solution is not None:
    print("\nFinal Solution:", solution)
    print("Final Cost:", calculate_cost(solution))
    print("All queens are safe!")
