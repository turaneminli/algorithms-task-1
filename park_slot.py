# n -> number of parked places
# cars[n] -> the parking spots where cars are parked
# k -> the number of cars that have to be covered by the roof
# res -> the minimum length of a roof that can cover k cars

from random import choice

def qsort(ls):
    if len(ls)<=1:
        return ls
    pivot = choice(ls)
    left= [i for i in ls if i < pivot]
    x = [i for i in ls if i == pivot]
    right = [ i for i in ls if i > pivot]
    return qsort(left) + x + qsort(right)
 

def carParkingRoof(cars:list, k:int) -> int:
    cars = qsort(cars) # overridden
    n = len(cars)
    res = float('inf')
    for i in range(n-k+1):
        res = min(res, cars[i+k-1] - cars[i])
        
    return res + 1

# Manual test:
# print(carParkingRoof([6, 2, 12, 7], 3))

if __name__ == "__main__":
    n = int(input())
    cars = list(map(int,input().strip().split()))[:n]

    k = int(input())
    
    # will print out result
    print(carParkingRoof(cars, k))