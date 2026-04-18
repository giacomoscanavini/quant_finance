"""
Find discount factors at different times using LU decomposition

Consider the following bonds with same face value of 100
Time to maturity        Coupone rate        Bond price
11 months semiannual    4%                  101.5
17 months annual        5%                  105.5
23 months semiannual    3%                  101
23 months annual        6%                  106.75 
"""

# The assumption is that each bond provides face value and coupon at maturity
# We can write equations given cash flow dates and discout each cash flow based on its date from bond purchase
# The first bond has a coupon with value 2% of 100 in 5 and 11 months
# The second bond has a coupon with value 5% of 100 in 5 and 17 months
# The third bond has a coupon with value 1.5% of 100 in 5, 11, 17, and 23 months
# The fourth bond has a coupon with value 6% of 100 in 11 and 23 months
# If we write all this as a system we have

import numpy as np
import scipy

# There are four cash flow dates (in year)
ts = np.array([5, 11, 17, 23]) / 12

def inversion_solve(A, b):
    # Complexity analysis
    # Inversion O(n^3)
    # Matrix-by-vector multiplication O(n^2)
    # Total complexity = O(n^3) + O(n^2) = O(n^3)

    # Solve the problem with the inverse of the matrix
    # Invest cash flow matrix 
    A_inv = np.linalg.inv(A)
    # Solve the system of linear equations
    # A @ x = b
    # x = A_inv @ b
    x = A_inv @ b
    return x

def LU_solve(A, b):
    # Complexity analysis
    # LU decomposition O(n^3)
    # Permuting vector O(n)
    # Forward-solve O(n^2)
    # Backward-solve O(n^2)
    # Total complexity = O(n^3) + 2 * O(n^2) + O(n) = O(n^3)

    # Solve the problem with LU decomposition of the cash flow matrix
    P, L, U = scipy.linalg.lu(A)
    # Permute the elements of B to match permuation of cash flow matrix A
    b_tilde = P @ b
    # Solve Ly = Pb
    y = scipy.linalg.solve_triangular(L, b_tilde, lower=True)
    # Solve Ux = y
    x = scipy.linalg.solve_triangular(U, y)
    return x

# Brond prices
b = np.array([101.5, 105.5, 101, 106.75])

# Cash flow matrix with columns each cash flow dates
A = np.array([[2,   102,  0,   0    ], 
              [5,   0,    105, 0    ], 
              [1.5, 1.5,  1.5, 101.5], 
              [0,   6,    0,   106  ]])


x1 = inversion_solve(A, b)
x2 = LU_solve(A, b)
# Note that the inverse method compute the whole inverse matrix which is not needed for this purpose
# LU tends to be more stable than matrix inversion

r1 = np.array([-np.log(r) for r in x1]) / ts
r2 = np.array([-np.log(r) for r in x2]) / ts

print(f"Interest rates at times: {ts}")
print(f"Inverse solve: {r1}")
print(f"LU solve: {r2}")