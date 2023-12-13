#state = [cannibals - left, missionaries - left]where_boat

boat_capacity = 2
all_cannibals = 3
all_missionaries = 3

def generate_moves(state):
    result = []
    if state[1] == "L":
        look = 
    for m in range(0, min(boat_capacity, ))        
    
            c = i - m
            if c <= state[0] and (c <= m or m == 0) and ((state[0]-c <= state[1]-m) or state[1]-m == 0):
                boat = [c,m]
                result.append(boat)
    print(result)

generate_moves([3,3])

def Prevoz(stav):
    def prevoz(stav, postup):
        if stav == [0,0]:
            return postup
        for i in range(1, kapacita+1):
            pass            