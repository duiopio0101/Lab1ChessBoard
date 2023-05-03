import random
import math

def initial_state(n):
    state = list(range(n))
    random.shuffle(state)
    return state

def conflicts(state):
    n = len(state)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if state[i] == state[j] or abs(state[i]-state[j]) == abs(i-j):
                count += 1
    return count

def anneal(n, initial_temp, cooling_rate, max_iterations):
    current_state = initial_state(n)
    current_energy = conflicts(current_state)
    best_state = current_state.copy()
    best_energy = current_energy
    temperature = initial_temp

    for i in range(max_iterations):
        if current_energy == 0:
            break

        new_state = current_state.copy()
        a, b = random.sample(range(n), 2)
        new_state[a], new_state[b] = new_state[b], new_state[a]
        new_energy = conflicts(new_state)

        if new_energy == 0:
            current_state = new_state
            current_energy = new_energy
            best_state = new_state
            best_energy = new_energy
        else:
            delta_energy = new_energy - current_energy
            if delta_energy < 0:
                current_state = new_state
                current_energy = new_energy
            else:
                p = math.exp(-delta_energy / temperature)
                if random.random() < p:
                    current_state = new_state
                    current_energy = new_energy

        temperature *= cooling_rate

    return best_state

n = 8
initial_temp = 100
cooling_rate = 0.95
max_iterations = 10000

initial_board = initial_state(n)

print('Початкова дошка:')
for row in range(n):
    line = ''
    for col in range(n):
        if initial_board[row] == col:
            line += 'Q '
        else:
            line += '- '
    print(line)

solution = anneal(n, initial_temp, cooling_rate, max_iterations)

print('Кінцева дошка:')
for row in range(n):
    line = ''
    for col in range(n):
        if solution[row] == col:
            line += 'Q '
        else:
            line += '- '
    print(line)