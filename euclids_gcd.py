"""
"""

import sys
import time

class EuclidsGCD:

    def __init__(self, x, y):
        """Constructor"""
        self.x = x
        self.y = y

    def gcd(self, x, y):
        """"""
        if y == 0:
            return 1, 0, x
        
        x_prime, y_prime, d = self.gcd(y, x % y)
        return y_prime, x_prime - (x/y) * y_prime, d


if __name__ == "__main__":
    if (len(sys.argv) == 3):
        x = sys.argv[1]
        y = sys.argv[2]
    else:
        x = 1035
        y = 759
    
    euclid = EuclidsGCD(x, y)
    print(euclid.gcd(x, y))