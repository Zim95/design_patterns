'''
The open close principle suggests that when you add functionality to a class.
You add it through an extension and not via modifications.

In product filter by adding filter by color, we have done a modification.

OCP = open for extension, closed for modification.

Now, in ProductFilter, we did a modification to the original class.
Right now we have size and color, so we have three combinations:
- size
- color
- size and color
But if there were size, color and weight then we would have 7 filter combos:
- size
- color
- weight
- size and color
- size and weight
- color and weight
- size, weight and color
If we follow the pattern we currently follow, we will have 7 methods in total.
So you clearly see that this is a problem.

So now we will add things through an extension and we will look at
an enterprise pattern.
So we have design patterns which are the core patterns.
On top of that, we have enterprise patterns which is not covered here.
The enterprise pattern we need to implement here is the Specification Pattern.

We will create two different classes:
- Specification: A class which determines whether or not a particular item
                 satisfies a particular criteria.
- Filter: Filters based on the specification passed to it.
'''


import enum


class Color(enum.Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(enum.Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:

    def __init__(self, name, color, size):
        self.name = name
        self.color = Color(color)
        self.size = Size(size)


class ProductFilter:

    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color:
                yield p

    # adding this has violated the open close principle
    # we will need to add filter by size
    # we will need to add filter by color and size, and so on...
    def filter_by_color(self, products, size):
        for p in products:
            if p.size == size:
                yield p


# Better approach
class Specification:
    '''
    Base class for further specification conditions
    '''

    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        return AndSpecification(self, other)


class Filter:
    '''
    Base filter class for further filter conditions
    '''

    def filter(self):
        pass


class ColorSpecification(Specification):
    '''
    Specification based on color
    '''

    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return self.color == item.color


class SizeSpecification(Specification):
    '''
    Specification based on size
    '''

    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return self.size == item.size


class AndSpecification(Specification):
    '''
    Combination of specifications
    '''

    def __init__(self, *specs):
        self.specs = specs

    def is_satisfied(self, item):
        return all(
            map(
                lambda x: x.is_satisfied(item),
                self.specs
            )
        )


class BetterFilter(Filter):
    '''
    Filter condition
    '''

    def __init__(self, items, spec):
        self.items = items
        self.spec = spec

    def filter(self):
        for item in self.items:
            if self.spec.is_satisfied(item):
                yield item


if __name__ == "__main__":
    apple = Product('Apple', Color.GREEN, Size.SMALL)
    tree = Product('Tree', Color.GREEN, Size.LARGE)
    house = Product('House', Color.BLUE, Size.LARGE)
    products = [apple, tree, house]

    # filter by color
    green = ColorSpecification(Color.GREEN)
    green_filter = BetterFilter(products, green)
    print('Green products are:')
    for green_item in green_filter.filter():
        print(f'{green_item.name} is green')

    # filter by size
    large = SizeSpecification(Size.LARGE)
    large_filter = BetterFilter(products, large)
    print('Large products are:')
    for large_item in large_filter.filter():
        print(f'{large_item.name} is large')

    # filter by color and size
    large_green = AndSpecification(green, large)
    large_green_filter = BetterFilter(products, large_green)
    print('Large green products are:')
    for large_green_item in large_green_filter.filter():
        print(f'{large_green_item.name} is green and large')

    '''
    BONUS: We can also overwrite the and operator and use that
           instead of the AndSpecification. For that we need to
           overwrite that on the main Specification class.
           We will use the AndSpecification on the __and__
           method and that should give us the condition.
           Bear in mind, we are not overwriting and operator
           but rather the bitwise & operator.
    '''
    lg = large & green
    lg_filter = BetterFilter(products, lg)
    print('Large green products are:')
    for lg_item in lg_filter.filter():
        print(f'{lg_item.name} is green and large')
