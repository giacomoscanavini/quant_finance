"""
Built Markowitz bullet for the following securities
μ1 = 0.20, μ2 = 0.13, μ3 = 0.17
σ1 = 0.25, σ2 = 0.28, σ3 = 0.20
ρ12 = 0.30, ρ23 = 0.00, ρ31 = 0.15
"""

import numpy as np
import matplotlib.pyplot as plt

# Build return vector and covariance matrix
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

# Built Markowitz bullet
def bullet_entry_no_short(m, Sigma):
    # Weights satisfying the constraint
    w = []
    max_val = 1
    for _ in range(len(m)-1):
        w_dummy = np.random.uniform(0, max_val)
        w.append(w_dummy)
        max_val -= w_dummy
    w.append(1 - sum(w))

    w = np.array(w)

    mu_v = m @ w.T
    var  = w @ Sigma @ w.T
    std  = np.sqrt(var)

    return std, mu_v, w

def bullet_entry_short(m, Sigma, bound=5):
    # Weights satisfying the constraint
    w = []
    for _ in range(len(m)-1):
        w.append(np.random.uniform(-bound, bound))
    w.append(1 - sum(w))
    w = np.array(w)

    mu_v = m @ w.T
    var  = w @ Sigma @ w.T
    std  = np.sqrt(var)

    return std, mu_v, w

def bullet_min_variance_line(m, Sigma, Sigma_inv, mu_v):
    # For a given imposed expeted return we can find the weights associated to the minimum variance line
    u = np.array([1] * len(m))
    
    A = u @ Sigma_inv @ u.T
    B = u @ Sigma_inv @ m.T
    C = m @ Sigma_inv @ m.T
    w = (u @ Sigma_inv) * (C - mu_v * B)/(A*C - B**2) + (m @ Sigma_inv) * (mu_v*A - B)/(A*C - B**2)

    mu_v = m @ w.T
    std = np.sqrt(w @ Sigma @ w.T)
    return std


fig, ax = plt.subplots(1, 1, figsize=(6, 4))
'''
N = 100000
bullet_coords = np.zeros((N, 2))
w_all = []
for i in range(N):
    bullet_coords[i, 0], bullet_coords[i, 1], w = bullet_entry_short(m, Sigma, bound=2)
    w_all.append(w)
ax.scatter(bullet_coords[:, 0].flatten(), bullet_coords[:, 1].flatten(), color='gold', alpha=0.2, s=3, label='Short selling allowed')
'''
N = 10000
bullet_coords = np.zeros((N, 2))
w_all = []
for i in range(N):
    bullet_coords[i, 0], bullet_coords[i, 1], w = bullet_entry_no_short(m, Sigma)
    w_all.append(w)
ax.scatter(bullet_coords[:, 0].flatten(), bullet_coords[:, 1].flatten(), color='grey', alpha=0.2, s=3, label='Short selling not allowed')


Sigma_inv = np.linalg.inv(Sigma)
mu_vs = np.linspace(0, 0.3, 1000)
efficient_front = []
for mu_v in mu_vs:
    efficient_front.append(bullet_min_variance_line(m, Sigma, Sigma_inv, mu_v))

ax.scatter(efficient_front, mu_vs, color='red', s=5, label='Efficient frontier')


ax.set_xlim(0.14, 0.30)
ax.set_ylim(0.12, 0.22)
ax.set_xlabel(r'Risk $\sigma$', loc='right')
ax.set_ylabel(r'Expected return $\mu$')

ax.scatter(s1, m[0], s=10, color='black', label='w = (1, 0, 0)')
ax.scatter(s2, m[1], s=10, color='green', label='w = (0, 1, 0)')
ax.scatter(s3, m[2], s=10, color='blue', label='w = (0, 0, 1)')

ax.legend()
plt.show()