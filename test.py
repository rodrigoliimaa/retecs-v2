import numpy as np

x = ((0.015596001185296091, 1.0, 1, 1, 1, 1), (0.015596001185296091, 0.7317073170731707, 0, 1, 1, 1), (0.6090238462858123, 0.08536585365853659, 0, 1, 1, 1), (0.015596001185296091, 0.06097560975609756, 0, 0, 1, 1), (0.73505513186419, 0.012195121951219513, 0, 1, 1, 1), (0.6091330182941094, 0.0, 0, 1, 1, 1))
y = (0.0,0.0,0.0,0.0,0.0,0.0)

x = np.array(x)

x.reshape(-1, 1, 6)

x = np.reshape(x, (x.shape[0], x.shape[1], 1))

x

np.array(x).reshape(1, -1)
