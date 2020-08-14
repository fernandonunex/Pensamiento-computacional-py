import time
start_time = time.time()

target = 4
epsilon = 0.0001
step = epsilon**2
result = 0.0

while abs(result**2 -target) >= epsilon and result <= target :
    print(f'{result**2 -target}',result)
    result += step

if abs(result**2) == target >= epsilon:
    print('The squared root couldnt be found')
else:
    print(f'The squared root is: {result}')

print("--- %s seconds ---"%(time.time()-start_time))