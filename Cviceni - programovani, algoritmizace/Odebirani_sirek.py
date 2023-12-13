#gets an array - game state - and creates all the different game states that can result from that one in one move
def generate_moves(config):
    result = []
    for i in range(len(config)):
        for n in range(config[i]): #what stays 
            l = list(config)
            l[i] = n
            result.append(l)
    return result

def minmax(config, player):
    """finds out what's the best possible outcome for the player who's move it is"""
    if sum(config) == 0:
        return player
    else:
        next_moves = generate_moves(config)
        for move in next_moves:
            winner = minmax(move, (-1)*player)
            if winner == player:
                return player
        return (-1)*player

print(minmax([2,2],1))