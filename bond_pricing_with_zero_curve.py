"""
Semiannual coupon bond with coupon rate 6%
maturity in 20 months and face value 100
interests are coumponded continuously

Assume zero rate is given by r(0,t) = 0.0525 + np.log(1 + 2*t) / 200

What is the price of the bond?
"""

import numpy as np

def PV(C, T, ts, F):
    B = 0
    for t in ts:
        B += C * np.exp(-rate(t) * t)
    B += (F + C) * np.exp(-rate(T) * T)
    return B

def rate(t):
    # Rate at time t
    return 0.0525 + np.log(1 + 2*t) / 200

# We will assume that the bond had been issued before time 0
# hence it has 4 semiannual coupons paid
# the last one at maturity, for T = 5/3

F = 100
C = 3
ts = [1/6, 3/4, 7/6]
T = 5/3

print(PV(C, T, ts, F))