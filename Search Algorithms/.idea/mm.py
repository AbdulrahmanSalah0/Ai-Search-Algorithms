import numpy as np
import matplotlib.pyplot as plt
# Limits
a = 0 # lower
b = np.pi # upper
# Number of iterations (for 10K ≈ 2 sec, for 100K it takes 10*10 more time ≈ 3 minutes on my PC)
N = 10_000
# var to store the results
areas =[]
# This one is slighlty faster and recalls the LateX formula above; it takes about 2 seconds for 10_000
for _ in range(N):
    # Apply the approximation formula
    answer = (b-a)/N * np.sin(np.random.uniform(a,b,N)).sum()
    areas.append(answer)
fig, ax = plt.subplots(figsize=(10,8))

mu = np.array(areas).mean()
sigma = np.array(areas).std()
textstr = '\n'.join((
    f'$\mu=${mu:.2f}',
    f'$\sigma=${sigma:.2f}' ))

ax.hist(areas, bins=31, ec='b')
# these are matplotlib.patch.Patch properties
props = dict(boxstyle='round', facecolor='blue', alpha=0.1)

# place a text box in upper left in axes coords
ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=props)
plt.title("Distribution of calculated areas")
plt.xlabel("Areas")

plt.show()
