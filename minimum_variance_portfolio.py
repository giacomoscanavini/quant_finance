"""
Among all attainable portfolios constructed using three securities with
expected returns μ1 = 0.20, μ2 = 0.13, μ3 = 0.17, standard deviations of
returns σ1 = 0.25, σ2 = 0.28, σ3 = 0.20, and correlations between returns
ρ12 = 0.30, ρ23 = 0.00, ρ31 = 0.15, find the minimum variance portfolio.
What are the weights in this portfolio? Also compute the expected return
and standard deviation of this portfolio.
"""

import numpy as np

m = np.array([0.2, 0.13, 0.17])
s1, s2, s3 = 0.25, 0.28, 0.20
p12, p23, p13 = 0.3, 0, 0.15
c11 = s1**2
c22 = s2**2
c33 = s3**2
c12 = p12*s1*s2
c21 = p12*s1*s2
c13 = p13*s1*s3
c31 = p13*s1*s3
c23 = p23*s2*s3
c32 = p23*s2*s3

Sigma = np.array([[c11, c12, c13],
                  [c21, c22, c23],
                  [c31, c32, c33]])

u = np.sum(np.eye(3), axis=1).flatten()

# Invert covariance matrix 
Sigma_inv = np.linalg.inv(Sigma)

# Weights to minimize variance of porfolio with Lagrange multipliers method
w = (u @ Sigma_inv) / (u @ Sigma_inv @ u.T)

# Expected return and standard deviation
mu_v = m @ w.T
var = w @ Sigma @ w.T 
s = np.sqrt(var)

print(f'Weights for minimum variance portfolio: w = {w}')
print(f'Portfolio expected return: mu_v = {round(mu_v, 4)}')
print(f'Portfolio risk: sigma = {round(s, 4)}')