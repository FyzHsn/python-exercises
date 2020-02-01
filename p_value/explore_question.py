"""In this script, I explore the evolution of p values in the cases where:

1. two distributions are the same
2. two distributions are different

and my hypothesis is that the two distributions are different.
"""

import numpy as np
from statsmodels.stats import weightstats as stests

mu_1, mu_2, mu_3, mu_4 = 0.0, 0.0, 1.0, 0.0
sigma_1, sigma_2, sigma_3, sigma_4 = 1.0, 1.0, 2.0, 1.0
N = 400000

# Hypothesis - s_1 and s_2 are different
s_1 = np.random.normal(mu_1, sigma_1, N)
s_2 = np.random.normal(mu_2, sigma_2, N)

p_1 = []

# Hypothesis - s_3 and s_4 are different
s_3 = np.random.normal(mu_3, sigma_3, N)
s_4 = np.random.normal(mu_4, sigma_4, N)

p_2 = []


for m in range(1, 101):
    sub_range = 4000 * m
    sub_s_1 = s_1[:sub_range]
    sub_s_2 = s_2[:sub_range]
    ztest, pval = stests.ztest(sub_s_1, x2=sub_s_2)
    p_1.append(pval)

    sub_s_3 = s_3[:sub_range]
    sub_s_4 = s_4[:sub_range]
    ztest, pval = stests.ztest(sub_s_3, x2=sub_s_4)
    p_2.append(pval)

print(p_1[-100:])
print(p_2[-100:])




