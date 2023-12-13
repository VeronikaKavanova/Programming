def generate_seq(current, N):
    print(current[1:])
    for number in range(current[-1] + 1,N+1):
        current.append(number)
        generate_seq(current, N)
        current.pop()

def generate_seq_alt(current, N):
    print(current[1:])
    for number in range(current[-1] + 1,N+1):
        generate_seq(current + [i], N) #pro každou úroveň vyrobím nový seznam, ty tam zůstavají

generate_seq([0],5)