Q) How classes work and what classes are?
-> In python you can do something crazy like this

def hello():
    class Hi:
        pass
    return Hi

The reason why you can do something like this in python and not in other languages, is that:

EVERYTHING IN PYTHON IS AN OBJECT.

Meaning you can pass them around, return them and even modify them.

Q) So how is a class an object? I thought classes created objects for us?
-> Very true, classes do create objects for us but that doesnt mean they're not objects themselves.

The class is an object, (We'll prove it later). This would also mean that we have another higher level class that created this object.

So remember this:
1. A class defines the rules for an object. (Datamembers, methods).
2. A metaclass defines rules for the class.

Now move into the metaclass.py
