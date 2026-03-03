import time 

L = list(range(1000))

start = time.time()
for i in range(len(L)):
    if L[i] == max(L):
        print(i)
stop = time.time()
print(f"Alg 1: {stop-start}")

start = time.time()
maximum = max(L)
for i in range(len(L)):
    if L[i] == maximum:
        print(i)
stop = time.time()
print(f"Alg 2: {stop-start}")
