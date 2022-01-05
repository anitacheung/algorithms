import sys

class Fibonacci:

    def __init__(self, num):
        """Constructor"""
        self.num = num
    
    def fib(self):
        """Gets fibonacci number using dynamic programming"""
        if self.num == 0:
            return 0
        elif self.num == 1:
            return 1
        else:
            fiblist = []
            fiblist.append(0)
            fiblist.append(1)
            for i in range(2, self.num):
                fiblist.append(fiblist[i-1] + fiblist[i-2])
            return fiblist[self.num - 1]

if __name__ == "__main__":
    if len(sys.argv) == 1:
        fib = Fibonacci(6)
        print(fib.fib())
    else:
        fib = Fibonacci(int(sys.argv[1]))
        print(fib.fib())
