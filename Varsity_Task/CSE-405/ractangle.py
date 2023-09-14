import matplotlib.pyplot as plt

# def dda(x1, y1, x2, y2):
#     dx = x2 - x1
#     dy = y2 - y1
#     steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
#     x_increment = dx / steps
#     y_increment = dy / steps
#     x = x1
#     y = y1
#
#     points = [(round(x), round(y))]
#     for _ in range(steps):
#         x += x_increment
#         y += y_increment
#         points.append((round(x), round(y)))
#
#     return points


def bresenham(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    x_sign = 1 if x2 > x1 else -1
    y_sign = 1 if y2 > y1 else -1

    if dy > dx:
        dx, dy = dy, dx
        interchange = True
    else:
        interchange = False

    p = 2 * dy - dx
    x, y = x1, y1
    points = [(x, y)]

    for _ in range(dx):
        if interchange:
            y += y_sign
        else:
            x += x_sign

        if p >= 0:
            if interchange:
                x += x_sign
            else:
                y += y_sign
            p -= 2 * dx

        p += 2 * dy
        points.append((x, y))

    return points


# Define the rectangle's coordinates
x1, y1 = 2, 2
x2, y2 = 8, 2
x3, y3 = 8, 6
x4, y4 = 2, 6

# Calculate the coordinates of the rectangle's edges using DDA
# dda_points = []
# dda_points.extend(dda(x1, y1, x2, y2))
# dda_points.extend(dda(x2, y2, x3, y3))
# dda_points.extend(dda(x3, y3, x4, y4))
# dda_points.extend(dda(x4, y4, x1, y1))

# Calculate the coordinates of the rectangle's edges using Bresenham
bresenham_points = []
bresenham_points.extend(bresenham(x1, y1, x2, y2))
bresenham_points.extend(bresenham(x2, y2, x3, y3))
bresenham_points.extend(bresenham(x3, y3, x4, y4))
bresenham_points.extend(bresenham(x4, y4, x1, y1))

# Extract x and y coordinates for plotting
# x_dda, y_dda = zip(*dda_points)
x_bresenham, y_bresenham = zip(*bresenham_points)

# Plot the results
# plt.plot(x_dda, y_dda, label="DDA")
plt.plot(x_bresenham, y_bresenham, label="Bresenham")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Rectangle Drawing: DDA vs Bresenham")
plt.legend()
# plt.grid()
plt.show()
