from openpose import coords_handler, points
import matplotlib.pyplot as plt

xs, ys = coords_handler(points)
plt.scatter(xs, ys)
plt.show()