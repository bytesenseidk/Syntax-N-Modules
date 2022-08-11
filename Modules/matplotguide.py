from matplotlib import pyplot as plt

plt.style.use("ggplot")

x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

y1 = [2849, 3200, 3675, 3932, 4320,
         4600, 5231, 5492, 5731, 5874, 6375]

y2 = [3781, 4351, 4682, 4929, 5343,
            5637, 6237, 6667, 6874, 6874, 7458]

y3 = [4537, 4887, 5385, 5728, 6301,
            6599, 7000, 7080, 7149, 7537, 8364]


plt.plot(x, y1, color="k", linestyle="--", marker="o", label="Line 1")
plt.plot(x, y2, color="b", marker="o", linewidth=3, label="Line 2")
plt.plot(x, y3, color="r", marker="x", linewidth=3, label="Line 3")

plt.xlabel("X-Angle")
plt.ylabel("Y-Angle")
plt.title("Matplotlib Guide")
plt.grid(True)
plt.legend()
plt.show()

