import numpy as np
import matplotlib.pyplot as plt

# lower_bound = -32.768
# upper_bound = 32.768
# x = np.random.uniform(low=lower_bound, high=upper_bound, size=1000)

mu, sigma = -15, 8  # mean and standard deviation
s = np.random.default_rng().normal(mu, sigma, 50)

# count, bins, ignored = plt.hist(s, 30, density=True)
# plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi))*np.exp( - (bins - mu)**2 / (2 * sigma**2) ),linewidth=2, color='r')

mu, sigma = 15, 8  # mean and standard deviation
x = np.random.default_rng().normal(mu, sigma, 50)
print(min(s))
print(max(x))
# count, bins, ignored = plt.hist(x, 30, density=True)
X = np.concatenate([s, x])
print(X)
plt.hist(X)
plt.show()


# mu, sigma = 12.5, 2  # mean and standard deviation
# p = np.random.default_rng().normal(mu, sigma, 1000)
# X = np.concatenate([s, p])
# print(X)
