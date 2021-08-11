- Sometimes the object creation logic becomes too convoluted (complex).
- Initializers are not always descriptive.
    - Name is always __init__
    - Cannot overlead the initializers with different sets of arguements.
    - Can turn into optional parameter hell

So in factory pattern we are talking about. Wholesale object creation (not peicewise like Builder).
We have the following choices in factory:
    - A separate method (Factory method).
    - They may exist as a separate class (Factory class).
    - Can create a heirarchy of Abstract Factories (Abstract factory).