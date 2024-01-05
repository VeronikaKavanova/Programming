import time

seznam = [[2,1], [1,3], [2,5], [2,3], [6,7], [4,5]]

start = time.time()
seznam.sort()
print(time.time()-start)
print(seznam)