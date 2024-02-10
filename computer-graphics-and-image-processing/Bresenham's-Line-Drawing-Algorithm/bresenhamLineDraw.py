import matplotlib.pyplot as plt

def bresenhamLineDrawingAlgorithm(x0, y0, x1, y1):
    points = []
    dx = x1 - x0
    dy = y1 - y0

    if abs(dy) < abs(dx):  # slope m is less than ONE and greater than ZERO: 0 < m < 1
        label_string = '0 < m < 1'
        if x0 > x1:
            x0, y0, x1, y1 = x1, y1, x0, y0
        yi = 1  # to go upwards along with Y-axis
        if dy < 0:
            yi = -1  # to go downwards along with Y-axis
            dy = -dy
        D = 2 * dy - dx  # base case
        y = y0

        for x in range(x0, x1 + 1):  # incrementing x by 1 in each iteration
            points.append((x, y))
            if D >= 0:
                y = y + yi
                D = D + 2 * dy - 2 * dx
            else:
                # y remains the same here
                D = D + 2 * dy

    else:  # slope, m > 1
        label_string = 'm > 1'
        if y0 > y1:
            x0, y0, x1, y1 = x1, y1, x0, y0
        xi = 1  # to go right along with X-axis
        if dx < 0:
            xi = -1  # to go left along with X-axis
            dx = -dx
        D = 2 * dx - dy  # base case
        x = x0

        for y in range(y0, y1 + 1):  # incrementing y by 1 in each iteration
            points.append((x, y))
            if D >= 0:
                x = x + xi
                D = D + 2 * dx - 2 * dy
            else:
                # x remains the same here
                D = D + 2 * dx

    return (points, label_string)


def main():
    # x0, y0 = 1, 1
    # x1, y1 = 8, 4
    print("""Please enter the co-ordinates of the two end points
of the line you want to draw(using Bresenham's Line Drawing Algorithm)""")
    x0 = int(input("Enter x0: "))
    y0 = int(input("Enter y0: "))
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))

    # Now you can use x0, y0, x1, y1 in your further code
    print(f"You entered: x0={x0}, y0={y0}, x1={x1}, y1={y1}")

    points_to_draw = []
    x_values = []
    y_values = []
    (points_to_draw, label) = bresenhamLineDrawingAlgorithm(x0, y0, x1, y1)
    for point in points_to_draw:
        x_values.append(point[0])
        y_values.append(point[1])

    print("x-coordinates of the points: ", x_values)
    print("y-coordinates of the points: ", y_values)

    plt.title("Bresenham's Line Drawing Algorithm")
    plt.xlabel('x')
    plt.ylabel('y')

    plt.plot(x_values, y_values, marker='X', label=label)

    plt.grid(True)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
