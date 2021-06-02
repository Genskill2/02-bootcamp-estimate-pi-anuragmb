import math
import unittest
import random

class TestWallis(unittest.TestCase):
    def wallis(n):
        x=0.0
        for i in range(1,n+1):
            x+=((4 * (i ** 2))) / ((4 * (i ** 2)) - 1)
        return x
    
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def monte_carlo(n):
        c=0
        s=0
        pi=0.0
        for i in range(n):
            x=random.random()
            y=random.random()
            origin=((x**2)+(y**2))
            if(origin<=1):
                c+=1
            else:
                s+=1
            pi+=((4*c)/s)
        return pi
            
        
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
        
    
if __name__ == "__main__":
    unittest.main()
