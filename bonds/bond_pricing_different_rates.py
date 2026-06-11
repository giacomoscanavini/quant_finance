"""
Find the price of a bond with face value $100 and $5 annual coupons that matures in four years, given that the continuous compounding rate is 8%
Sketch the graph of the price of the bond as a function of the continuous compounding rate r
"""

import numpy as np
import matplotlib.pyplot as plt

F = 100
C = 5
T = 4
r = 0.08

def price(F, C, T, r):
    # We can find the price of the bond by discounting coupons and face accordingly
    B = 0
    # Discount coupons 
    for t in range(1, T):
        B += C * np.exp(-r * t)
    # Discount face value and final coupon
    B += (F + C) * np.exp(-r * T)

    return B

rates = np.linspace(0, 100, 100000)
prices = [price(F, C, T, r) for r in rates]

pv = price(F, C, T, r)

fig, ax = plt.subplots(1, 1, figsize=(6,4))
ax.plot(rates, prices, lw=2, color='black')
ax.axvline(r, lw=1, ls=':', color='grey', alpha=0.5)
ax.axhline(pv, lw=1, ls=':', color='red', alpha=0.5, label=f'PV = {round(pv, 2)} \nwith (F, C, T, r) = ({F}, {C}, {T}, {r})')
ax.set_xscale('log')
#ax.set_xlim(, 100)
ax.set_xlabel('Rate', loc='right')
ax.set_ylabel('Present Value (Bond price)', loc='top')
ax.legend()
plt.show()


"""
The plot shows us that 
    for r --> 0 we have no discount over time (discount factor is 1)
        so the price of the bond is equal to the face value + the value of all coupons = 100 + 4*5 = 120
        meaning that we pay up front what we will obtain later on

        There is no time value of money
        so future cash flows are valued exactly the same as present ones

    for r --> inf we have infinite discount over time (discount factor is 0)
        so the price of the bond is zero

        Future payments are infinitely discounted 
        So they have zero present value 
        The bond is worth zero today, because future cash flows are considered worthless.
        The market values future cash flows so little that no one is willing to pay for them today
"""