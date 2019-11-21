import numpy as np
x = np.array(([2,4,6],[8,10,12],[14,16,18]))
y = np.zeros(x.shape)
run_sum = 0
n_rows = x.shape[0]
n_cols = x.shape[1]
for i in range(n_rows):
    run_sum = 0
    for j in range(n_cols):
        run_sum += x[i,j]
        y[i,j] = run_sum
print(y)