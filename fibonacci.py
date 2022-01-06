"""
TODO -- fix matrixfib to improve speed
"""
import sys
import time
import numpy as np

class Fibonacci:

    def __init__(self, n, verbose):
        """Constructor"""
        self.n = n
        self.verbose = verbose
    
    def expfib(self, n):
        """Gets fibonacci number using recursive, exponential method
        
        Keyword Arguments:
        n -- position of fibonacci number
        """

        if n == 0:
            return 0
        if n == 1:
            return 1
        
        return self.expfib(n-1) + self.expfib(n-2)
    
    def polyfib(self):
        """Gets fibonacci number using polynomial dynamic programming"""
        if self.n == 0:
            return 0
        elif self.n == 1:
            return 1
        else:
            fiblist = []
            fiblist.append(0)
            fiblist.append(1)
            for i in range(2, self.n + 1):
                fiblist.append(fiblist[i-1] + fiblist[i-2])
            return fiblist[self.n]
    
    def matrixfib(self):
        """Get fibonacci number using matrices"""
        relationship = [[0, 1],[1, 1]]
        initial = [0, 1]
        array = np.linalg.matrix_power(relationship, self.n)
        results = np.matmul(array, initial)
        return results[0]
    
    def timer(self, start):
        if self.verbose:
            end = time.time()
            print(end - start)

def execute(n):
    fib = Fibonacci(n, True)

    print("Exponential")
    start = time.time()
    print(fib.expfib(n))
    print(fib.timer(start))

    print("Polynomial")
    start = time.time()
    print(fib.polyfib())
    print(fib.timer(start))

    print("Matrix")
    start = time.time()
    print(fib.matrixfib())
    print(fib.timer(start))

if __name__ == "__main__":
    if len(sys.argv) == 1:
        execute(35)
    else:
        execute(int(sys.argv[1]))
