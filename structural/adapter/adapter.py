class Point:

    def __init__(self, x, y):
        self.y = y
        self.x = x


def draw_point(p):
    print('.', end='')

# Scenario: You are given this api to work with. No chances of change.

# Scenario: Your code looks the following way.
class Line:

    def __init__(self, start, end):
        self.start = start
        self.end = end


class Rectanlge(list):

    def __init__(self, x, y, width, height):
        super().__init__()
        self.append(
            Line(
                Point(x, y),
                Point(x + width, y)
            )
        )
        self.append(
            Line(
                Point(x + width, y),
                Point(x + width, y + height)
            )
        )
        self.append(
            Line(
                Point(x + width, y + height),
                Point(x, y + height)
            )
        )
        self.append(
            Line(
                Point(x, y + height),
                Point(x, y)
            )
        )


def draw(rcs):
    print('\n\n--- Drawing some  stuff ---\n')
    for rc in rcs:
        for line in rc:


class LineToPointAdapter(list):

    count = 0
    def __init__(self):
        super().__init__()
        self.count += 1

    


if __name__ == "__main__":
    rs = [
        Rectanlge(1, 1, 10, 10),
        Rectanlge(2, 2, 5, 5)
    ]