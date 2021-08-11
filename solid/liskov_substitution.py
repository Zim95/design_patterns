'''
Here we will create a Rectangle class. But we will create it differently,
i.e. by using initializers. @property, @setter

We first create the Rectangle class with properties.
- width
- height
- area
Each of which are set by property decorators.

We have a function called use it, which purposefully changes the height
of the rectangle to 10.
It then calculates the expected area and the actual area.

For a rectangle, it works, no problem.

Now we create a square class which inherits the Rectangle.

Since, the width and height of a square should be the same.
We do the same for it.
We set the width and height to the constructor.
Since, we already have width, height and area properties,
we can simply overwrite the behaviour of these properties by
using the setter of the super class.

So, we do that and set the width and the height to equal values.

However
While doing this the square class, has a different expected result
and a different actual result. Why?

The area is basically width * height.
In a square we set width = height,
So when we did rc.height = 10,
we effectively changed the width of it as well.
So the actual area will be 100.
But since we passed the width to be 5, we expected the output to be 50.
Not 25, because our expected area is w * h, meaning 5 * 10 = 50.
Despite it being a square. Think of this as a test case.

So what should have been done:
1. There was no need of a square class. There could have been a boolean
    data member indicating is_square or not.
2. We could have used factory methods as well (Talk about those later).

Ultimately it was the setters that directly caused the failure and
violated the Liskov's Substitution Principle.

But this example shows how the implementation of a base class
failed the child class.
This is what the Liskov substitution principle is.
'''


class Rectangle:

    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value    

    @property
    def area(self):
        return self.width * self.height

    def __str__(self):
        return f'Width: {self.width} and Height: {self.height}'


class Square(Rectangle):

    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        self.width = self.height = value

    @Rectangle.height.setter
    def width(self, value):
        self.width = self.height = value


def use_rectangle(rc):
    w = rc.width
    rc.height = 10
    expected_area = int(w * 10)
    print(f'Expected area: {expected_area}, Actual area: {rc.area}')


if __name__ == "__main__":
    rc = Rectangle(5, 10)
    use_rectangle(rc)
    sq = Square(5)
    use_rectangle(sq)
