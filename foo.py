import sys
import math

def foo(arr):
    x = 0
    y = 0
    z = 0
    for i in range(0, len(arr)-1):
        x = x + arr[i]
        y = 0
        for j in range(0, len(arr)-1):
            y = y + arr[j]
            z = 0
            for k in range(0, len(arr)-1):
                z = 3
        x = x + y
    return x + z + y  

def boo(arr):
    x = 0
    y = 0
    for i in range(0, len(arr)-1):
        x = x + arr[i]
        y = 0
        for j in range(0, len(arr)-1):
            y = y + arr[j]
        x = x + y
    return x + y + 3  

def doo(arr):
    x = 0
    for i in range(0, len(arr)-1):
        x = (len(arr)+1) * arr[i]
    return x + 3 

def bar(arr):
    x = 0
    for i in range(0, len(arr)):
        x += arr[i]
    return (len(arr)+2) * x + 3

def main():
    array = [1, 2, 3]
    print(bar(array))

if __name__ == '__main__':
    sys.exit(main())      



