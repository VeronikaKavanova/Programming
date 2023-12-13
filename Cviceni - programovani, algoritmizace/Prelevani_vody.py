def generate_moves(config):
    """generates all of the situations we can get to from this position"""
    result = []
    for i in range(3):
        cont1 = config[i]
        #if the container isn't full, we can trasnfer water into it
        if cont1 != volumes[i]:
            for j in range(3):
                if j != i: 
                    cont2 = config[j]
                    #if the container isn't empty, we can trasnfer water from it    
                    if cont2 != 0:
                        #either we trasnfer all of the water from the second container, or the first one will fill up
                        new_cont1 = min(volumes[i], cont1 + cont2)
                        new_cont2 = cont2 - (new_cont1 - cont1)
                        new = list(config)
                        new[i] = new_cont1
                        new[j] = new_cont2
                        #if we haven't already achieved this state, we can add it as a potential move
                        new = tuple(new)
                        if new not in states:
                            result.append(new)
    return result

def all_states(queue):
    """uses BFS"""
    iteration = 1
    while queue != []:
        new_queue = []
        for config in queue:    
            possible_moves = generate_moves(config)
            # we want to save the first time we get to that state 
            # and therefore we need to save all the states before we go deeper in the recursion
            for move in possible_moves:        
                states[move] = iteration
                new_queue.append(move)
        iteration += 1
        queue = new_queue
    return True

user_input = input().split()
for i in range(6):
    user_input[i] = int(user_input[i])

volumes = tuple(user_input[:3])

start = user_input[3:]

#has in it all of the game states that we have already seen to prevent cycles
states = {tuple(start):0}

all_states([start])

volumes = {}
for state in states:
    for number in state:
        trasnfers = states[state]
        if number not in volumes:
            volumes[number] = trasnfers
        else:
            if volumes[number] > trasnfers:
                volumes[number] = trasnfers

for i in range(max(volumes)+1):
    if i in volumes:
        print(f"{i}:{volumes[i]}", end = " ")