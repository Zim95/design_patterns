1. Some components in your system, it makes sense to have only only one.
    - Database repository (Loading from db at the beginning).
    - Object factory (Do you really need to instantiate object factory if we can have only one class with static methods).

E.g, the initializer call is expensive.
    - We only do it once.
    - We provide everyone with the same instance.

-> Want to prevent anyone from creating additional copies.
-> Need to take care of lazy instantiation. (Nothing really instantiates the singleton until needed).
